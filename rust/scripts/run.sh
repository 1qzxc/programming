#!/bin/bash

# todo: 
#if not args(1), then: 
project_dir=../hello_world
#else project_dir=$1
cd $project_dir && cargo run

# expose on ips
#ROCKET_ENV=staging cargo run
