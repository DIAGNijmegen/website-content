Dockers used to automatically build and host a specific website. 

## Building the docker for local development.
To build the docker locally, run:
```
docker build . -f docker/docker_local/Dockerfile --tag website
```
**The -f command points to the relative path of the Dockerfile, therefore make sure to run this command from the main folder of the repository.**

## Running the docker for local development.
Execute the following:
```
docker run --tty -p 8000:8000 -v </path/to/local/website-content>:/home/user/website-content website:latest <website-name>
```
Replace `</path/to/local/website-content>` with the correct path to your local repository and replace `<website-name>` with one of the following: `ai-for-health, base, diag, pathology, rse, rtc`.

## Development workflow - local
1. Run the docker, example command: `docker run --tty -p 8000:8000 -v /home/user/documents/website-content:/home/user/website-content website:latest diag`
2. Visit `0.0.0.0:8000` to see the local hosted website. 
3. Start developing locally, all changes in your local folder (in the example: /home/user/documents/website-content) will result in an automatic rebuild of the locally hosted website.

## Build the docker and push to diag online repository.
```
0. cd website-content/docker/docker_remote
1. docker build . --tag website
2. docker run --interactive --tty --user root website:latest diag master
3. docker ps --latest # (to get the image-id, check first column)
4. docker commit <image-id> /path/to/remote/repository/webteam/website:latest
5. docker push /path/to/remote/repository/webteam/website:latest
```

## Host the website (for demo'ing purposes only) on the diag cluster.
```
~/c-submit <arguments for c-submit> /path/to/remote/repository/webteam/website:latest <website-name> <branch-name>
```

Replace `</path/to/remote/repository>` with the correct path to our online repository, replace `<website-name>` with one of the following: `ai-for-health, base, diag, pathology, rse, rtc` and replace `<branch-name>` with any name of the branch you want to host, for instance use the main branch: "master".

