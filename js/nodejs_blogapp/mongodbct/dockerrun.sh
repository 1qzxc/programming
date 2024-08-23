docker build -t mymongo .
docker run --name mongo-dev -d -v $PWD/data/db:/data/db -p 27017:27017 mymongo
