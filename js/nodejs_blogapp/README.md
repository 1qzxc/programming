# nodejs_blogapp
This is a nodejs blogging app that may be run using: 

## Docker 
- healthcheck feature

In order to run:

```
sudo docker build -t <username>/node-web-app .
sudo docker run -p 8080:8080 -d <username>/node-web-app
```

## docker-compose 
In case if you would want to have prometheus and grafana monitoring the performance 

```
sudo docker-compose up
```
Nodejs app is accessible on port 8080
Prometheus is accessible on port 9090
Grafana is accessible on port 3000

## minikube 

```
sudo docker build -t <username>/node-web-app .
kubectl apply -f deployment-kube.yml
```
