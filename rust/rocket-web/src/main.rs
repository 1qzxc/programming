// #![feature()] flag to enable the unstable decl_macro
#![feature(decl_macro)]
#[macro_use] extern crate rocket; //This imports the macros from the rocket crate
//Alternatively, we can use 'use rocket::*;'
//
// We’ll need it when creating routes for our web app.
//

use rocket::response::content::Json;
// import the Json type from the rocket::response::content macro. 
// We’ll use this to send a response when our route is called
//


//attribute to tell Rocket that our function expects a GET request to the /hello route
#[get("/hello")]

              // return type as Json with a <&'static str> argument
fn hello() -> Json<&'static str> {
  Json("{
    'status': 'success',
    'message': 'Hello API!'
  }")
}


fn main() {
    //This uses the ignite() method from the rocket crate to create a new instance of Rocket, and then mounts our hello route with the mount() method and base path /api
  rocket::ignite()
    .mount("/api", routes![hello])
    .launch(); // Finally, we used the launch() method to start the application server and listen for requests.
}
