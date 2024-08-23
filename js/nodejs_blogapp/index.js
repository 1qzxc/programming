'use strict'

const path = require('path');
const express = require('express');
const Prometheus = require('prom-client');
const expressEdge = require('express-edge');
const app = express();
const port = process.env.PORT || 8080;
const metricsInterval = Prometheus.collectDefaultMetrics();
const mongoose = require('mongoose');
const connectMongo = require('connect-mongo');
const bodyParser = require('body-parser');
const Post = require('./database/models/Post');
const User = require('./database/models/User');
const fileUpload = require("express-fileupload");
const bcrypt = require('bcrypt');
const auth = require("./middleware/auth");
const storePost = require('./middleware/storePost')
const redirectIfAuthenticated = require('./middleware/redirectIfAuthenticated');
const edge = require("edge.js");
const expressSession = require('express-session');
const httpRequestDurationMicroseconds = new Prometheus.Histogram({
  name: 'http_request_duration_ms',
  help: 'Duration of HTTP requests in ms',
  labelNames: ['method', 'route', 'code'],
  buckets: [0.10, 5, 15, 50, 100, 200, 300, 400, 500]  // buckets for response time from 0.1ms to 500ms
});

// Runs before each requests
app.use((req, res, next) => {
  res.locals.startEpoch = Date.now();
  next();
});

const mongoStore = connectMongo(expressSession);
 
app.use(expressSession({
    secret: 'secret',
    store: new mongoStore({
        mongooseConnection: mongoose.connection
    })
}));

app.use(expressSession({
    secret: 'secret'
}));
app.use(fileUpload());
app.use(express.static('public'));
app.use(expressEdge);
mongoose.connect('mongodb://mongodb:27017/node-blog', { useNewUrlParser: true })
    .then(() => 'You are now connected to Mongo!')
    .catch(err => console.error('Something went wrong', err))

app.use('*', (req, res, next) => {
    edge.global('auth', req.session.userId)
    next()
});


app.set('views', __dirname + '/views');


app.use(bodyParser.json())
app.use(bodyParser.urlencoded({
    extended: true
}));

app.use('/store', storePost)

//app.get('/', async (req, res, next) => {
//  const posts = await Post.find({})
//  setTimeout(() => {
//    res.render('index', {posts} );
//    //next();
//  }, Math.round(Math.random() * 200))
//});

app.get('/', async (req, res) => {
    const posts = await Post.find({})
    res.render('index', {
        posts
    })
});


app.get('/test', function (req, res) {
	res.send('hello world');
});

app.get('/bad', (req, res, next) => {
  next(new Error('My Error'));
});

app.get('/new', (req, res, next) => {
         
    if (req.session.userId) {
         res.render('create');
    } 
    else { 
         res.redirect('/auth/login')
    }

});


app.post('/store', auth, storePost, (req, res) => {
    const {
        image
    } = req.files

    image.mv(path.resolve(__dirname, 'public/', image.name), (error) => {
    Post.create({
	...req.body, 
	image: `${image.name}`
    }, (error, post) => {
        res.redirect('/');
    });
  })
});


app.get('/post/:id', async (req, res) => {
    const post = await Post.findById(req.params.id)
    res.render('post', {
        post
    })
});

app.get('/auth/register', redirectIfAuthenticated, (req,res) => {
        res.render('register')
});


app.post('/users/register', redirectIfAuthenticated, (req,res) => {
        User.create(req.body, (error, user) => {
        if (error) {
            return res.redirect('/auth/register')
        }
        res.redirect('/')
    })

});


app.get('/auth/login', redirectIfAuthenticated, (req, res) => {
        res.render('login');
});

app.post('/users/login', redirectIfAuthenticated, (req, res) => {
        const {
        email,
        password
    } = req.body;
	User.findOne({
        email
    }, (error, user) => {
        if (user) {
            // compare passwords.
            bcrypt.compare(password, user.password, (error, same) => {
                if (same) {
                    // store user session.
                    req.session.userId = user._id
		    res.redirect('/')
                } else {
                    res.redirect('/auth/login')
                }
            })
        } else {
            return res.redirect('/auth/login')
        }
    })
});


app.get('/auth/logout', (req, res) => {
	req.session.destroy(() => {
        res.redirect('/');
    })
});


app.get('/metrics', (req, res) => {
  res.set('Content-Type', Prometheus.register.contentType)
  res.end(Prometheus.register.metrics())
});

// Error handler
app.use((err, req, res, next) => {
  res.statusCode = 500
  // Do not expose your error in production
  res.json({ error: err.message });
  next();
});

// Runs after each requests
app.use((req, res, next) => {
  const responseTimeInMs = Date.now() - res.locals.startEpoch

  httpRequestDurationMicroseconds
    .labels(req.method, req.path, res.statusCode)
    .observe(responseTimeInMs)

  next();
});

const server = app.listen(port, () => {
  console.log(`Example app listening on port ${port}!`)
});

// Graceful shutdown
process.on('SIGTERM', () => {
  clearInterval(metricsInterval)

  server.close((err) => {
    if (err) {
      console.error(err)
      process.exit(1)
    }

    process.exit(0)
  });
});


module.exports = app;
