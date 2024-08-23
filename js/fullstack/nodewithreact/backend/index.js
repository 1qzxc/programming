const express = require ('express');
const passport = require('passport');
const GoogleStrategy = require('passport-google-oauth20');
const keys = require('./config/keys');

const app = express();

app.get('/', (req, res) => {
  res.send({ h1: 'dummy' });
});

app.get('/auth/google', 
        passport.authenticate('google', {
      scope: ['profile', 'email']
    })
);

passport.use(new GoogleStrategy({ 
    clientID: keys.googleClientID,
    clientSecret: keys.googleClientSecret,
    callbackURL: '/auth/google/callback'
    }, (accessToken) => {
        console.log(accessToken);
    })
);


//getting port from environment variable PORT or 5001
const PORT = process.env.PORT || 5001;

app.listen(PORT , function(){
    console.log('Server running on 5001...');
});
