Automticaly pulls the latest master branch from the website-content repository when starting a new docker instance. An additional argument can be given to automatically build and host a specific website. To do so: provide the name of the directory without the "website-" prefix. 

For instance, to automatically build and run the ai-for-health website:
./c-submit [put your c-submit arguments here] --interactive doduo1.umcn.nl/webteam/website:latest ai-for-health

Or for the diag website: 
./c-submit [put your c-submit arguments here] --interactive doduo1.umcn.nl/webteam/website:latest diag

Go to port 8000 (which opens automatically) to view the website on your local machine when running the docker instance. The github repository is located in /home/user/source/website-content.

You can always build and host a specific website manually, by leaving out the additional argument in the c-submit command. 
