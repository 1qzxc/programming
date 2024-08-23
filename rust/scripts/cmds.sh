#!/bin/bash

rustup --version
cargo new <appname> --bin 
#The --bin flag tells Cargo to generate this as a binary-based project.

rustup override set nightly
#configure Rust nightly as our project toolchain
#Rocket uses unstable features of Rust, like its syntax extensions.


