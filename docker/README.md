## Build and deploy the website in a docker container

Automticaly pulls the latest master branch from the website-content repository when starting a new docker instance. An additional argument can be given to automatically build and host a specific website. To do so: provide the name of the directory without the "website-" prefix. 

## Build and run the docker image locally
To build the docker image, run: `docker build --tag website .`
To use the docker image to auto build and host a website use: `docker run --publish=8000:8000 website:latest [website-name]`
Example: `docker run --publish=8000:8000 website:latest diag` for the DIAG website.

## Build and run the docker image on the DIAG cluster
The given docker image is maintained on the image registry of the DIAG cluster. Those with access to the DIAG cluster can simply submit an interactive job and refer to the image-registry-website/webteam/website:latest to run the docker image on the cluster (ports are automatically exposed).
