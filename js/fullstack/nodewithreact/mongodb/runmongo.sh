docker build -t my-mongo
docker run --name my-mongo -d -v /tmp/mongodb:/data/db -p 27017:27017 hello-mongo
