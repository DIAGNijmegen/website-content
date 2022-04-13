Docker used to automatically build and host a specific website. To do so, provide the name of the directory (without the "website-" prefix). 

## Building the docker
To build the docker locally, run:
```
docker build . -f docker/Dockerfile --tag website
```
**The -f command points to the relative path of the Dockerfile, therefore make sure to run this command from the main folder of the repository.**

## Running the docker
Execute the following:
```
docker run --tty -p 8000:8000 -v </path/to/local/repository>:/home/user/website-content website:latest <website-name>
```
Replace `</path/to/local/repository>` with the correct path and replace `<website-name>` with one of the following: `ai-for-health, base, diag, pathology, rse, rtc`.

## Development Workflow
1. Run the docker, example command: `docker run --tty -p 8000:8000 -v /home/user/documents/website-content:/home/user/website-content website:latest diag`
2. Visit `0.0.0.0:8000` to see the locally hosted website. 
3. Start developing locally, all changes in your local folder (in the example: /home/user/documents/website-content) will result in an automatic rebuild of the locally hosted website.

## Bibfiles
The bibfiles subdirectory contains a version of the required bibfiles. For the most up-to-date version, download the files from the corresponding repository.
