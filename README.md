# Teachers Yellow Pages

## About

A simple teachers directory app.

## Demo
 - To see a demo version of the project download and install Docker
 - Pull the docker image of the project from Dockerhub
 ```shell 
 docker pull nshefeek/teachers:latest
 ```
 - Run the downloaded docker image with administrator name and password
 ```shell
 docker run -it -p 8020:8020 \
     -e DJANGO_SUPERUSER_USERNAME=admin \
     -e DJANGO_SUPERUSER_PASSWORD=sekret1 \
     -e DJANGO_SUPERUSER_EMAIL=admin@example.com \
     nshefeek/teachers
```
 - Go to http://localhost:8020 in your browser.
 - To import data load CSV file and zip file containing profile images from your file system


## Further Improvements:
 - Using CDN to deliver static files
 - Caching
 - Error logging
 - Cleaning up files
 - Event logging
 - Live search
