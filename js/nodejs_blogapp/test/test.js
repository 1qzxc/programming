var request = require('supertest');
var app = require('../server.js');
describe('GET /test', function() {
	 it('respond with hello world', function(done) {
		  //navigate to root and check the the response is "hello world"
         request(app).get('/test').expect('hello world', done);
	 });
});
