//By default, Rust brings only a few types into the scope of every program in the prelude. If a type you want to use isn’t in the prelude, you have to bring that type into scope explicitly with a use
use std::io;  // io lib for terminal interraction, hw1: need to read list of methods, namespaces and deeper interaction


fn main() {   // typical function definition for rust, regular syntax 

    println!("Guess the number!");  // println! - exclamation mark means it is a macro 
    //The term macro refers to a family of features in Rust: declarative macros with macro_rules! and three kinds of procedural macros

    println!("Please input your guess.");

    //let is used to create a variable
    let mut guess = String::new(); //growable, UTF-8 encoded bit of text
                         // :: syntax in the ::new line indicates that new is an associated function of the String type.
    //In Rust, variables are immutable by default

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    println!("You guessed: {}", guess);

}
