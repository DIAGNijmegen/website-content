# Overview Developer Docs

## Overview
### part 1
- userdocs
- installation
- pelican
- jinja2
- javascript
- content

- templates
    - blocks
    - static (see themes first)
    - critical css (see themes first)
- websites
  - publishconfig
  - pelicanconfig
- custom-page
- custom-template
- drafts
- npm
- themes
- custom-css
- design resources

### part 2
- scripts
    - copy_content
    - parse_content -> see plugins/content-aggregator
    - parse_publication -> see publication pipeline
- above-the-fold
- plugins
    - bootsrapify
    - content aggregator
    - bibtex loader 
    - edit-url
    - fileutil
    - imgutil
    - inline extend
    - pagehierachy
- publication pipeline
    - diag-literature
    - parse publications
    - bibliography
- imgoptim
    - optimize images

  
### part 3
- netlify
- hosting (yourhosting)
- dns
- assets
- deploy
- github actions
- webteam deploy bot
    - webteam deplot bot, used for deploying the wesbites
     - two secrets 
        1. curl diag.bib (used in parse publications)
        2. workflow dispatch (used in github action diag-literature)

- development branch / deploy
- security
- google analytics
- colofon
- techdocs and documentation website 
 
---

## Part 1

### User docs
The user documentation can be found in docs/. This documentation explains user how to add/change content. In addtiotion is includes some advanced topics about css, redirects and website configuration. A new webteam member should become familiar with all the user documentions. 

### Installation 
Installation for developers can be done in two ways: 

#### Locally 
To get website local running, the following steps need to be taken

    - clone repository 
    - install requirements (recommendation is to use a conda/virtual environment)

#### Docker
A dockerfile is provided to to build a container (in progress)

### pelican
Pelican is a static site generator that requires no database or server-side logic.
Some of Pelican’s features include:
- Write content in reStructuredText or Markdown markup
- Completely static output is easy to host anywhere
- Themes that can be customized via Jinja templates
- Publish content in multiple languages
- Atom/RSS feeds
- Code syntax highlighting
- Import from WordPress, RSS feeds, and other services
- Modular plugin system and corresponding plugin repository

### jinja2
Jinja is a fast, expressive, extensible templating engine. Special placeholders in the template allow writing code similar to Python syntax. Then the template is passed data to render the final document.

### javascript
JavaScript is a scripting or programming language that allows you to implement complex features on web pages — every time a web page does more than just sit there and display static information for you to look at — displaying timely content updates, interactive maps, animated 2D/3D graphics, scrolling video jukeboxes, etc. — you can bet that JavaScript is probably involved. Even though we use a relatively stimple static website build (pelican) some javascript is used.  

### content
We have 2 types of content folders
- Content folder in main folder (website-content)
- Content folders in separate website folders (e.g., website-pathology).  
The copy_content.sh script copies content from the main folder to a website folder (this is also one of the first scipts you need to run in order to build a website locally). Within the copy_content.sh script, the default website pages are copied (such as the home page, 404 and the colofon), the content bib files are copied, and the parse_content.sh script is called which copies only the relevant site specific content to the website folder. Later down the website building pipeline some of the files of the websites' content folders are generated automatically by --BY WHAT--?.  
### templates
The radboudumc-template folder contains the website page templates, as well as subfolders for recurring blocks of code, css (page and text layout style sheets). 

The html templates provide backbones of the web pages. They contain many jinja placeholders that are filled in automatically when the websites are built. -- NOT SURE HOW THESE ARE USED

#### blocks
Blocks are pieces of code that can be used in multiple pages. For example there is a code block that can be used to show the website viewer where he/she is in our sites (called breadcrumbs). For example, it shows: Home / Members / -Member name-
Using these blocks of code on websites are optional (for example this breadcrumb option is used in www.computationalpathologygroup.eu but not in www.diagnijmegen.nl)

#### static folder (see themes first)
This contains some default css and js files
-- Not sure how these relate to critical css

#### critical css (see themes first)
When a site is rendering, it may take quite some time to load all defined css assest, while maybe only a part of all these assest are being used. Therefore, we extract the critical css assets (automatically?), and only these css assets are laoded in the header of the page. Other non-critical css assets can then be loaded uin the footer. 

More information here: website-content/docs/critical-above-the-fold-css.md 

### websites
general info here. Separate folders containthing the main structure 
Websites also contain the following files that are essential for the build of these sites: 

#### pelicanconfig
The pelican_config.py files contain the site-wide settings that control the build of the website.
For example the NAV_SECTIONS control which site pages are shown in the navigation bar on thop of the website.

More infor here: website-content/docs/website-configuration.md

#### publishconfig
The publishconfig also contains pelican configurations, just like the pelicanconfig. The configurations from this script, however, are only used when the websites are published, not when built locally. For example, the publish config script contains the site url, which is not needed when built locally. Thus the need for this additional config file. 

### custom-page
Custom pages are 'stand alone' pages such as https://www.diagnijmegen.nl/doing-a-phd-at-diag/

Custom pages can be made by (1) overwriting a default page, or (2) by creating an independent page. More info here: website-content/docs/create-custom-page.md

### custom-template

### drafts

### npm
"Node Package Manager" is an online repository for the publishing of open-source Node. js projects; second, it is a command-line utility for interacting with said repository that aids in package installation, version management, and dependency management.

### themes

### custom-css

### design resources



## part 2

### scripts

#### copy_content and parse_content -> see plugins/content-aggregator
The copy_content.sh script copies content from the main folder to a website folder (this is also one of the first scipts you need to run in order to build a website locally). Within the copy_content.sh script, the default website pages are copied (such as the home page, 404 and the colofon), the content bib files are copied, and the parse_content.sh script is called which copies only the relevant site specific content to the website folder. Later down the website building pipeline some of the files of the websites' content folders are generated automatically by --BY WHAT--?.  

#### parse_publication -> see publication pipeline
-- Not sure where this is called

More info here: website-content/docs/publications-pipeline-developers.md

### above-the-fold
Above the fold content is what is shown to the website viewer when he/she enters our website (without scrolling). -- not sure what we do with this

### plugins
Plugins are functionalities that are addedd to pelican. Below a list and the description of the used plugins:

#### bootsrapify
The bootstrap plugin contains many predefined classes for html, which makes it easy to set upt the desired layout of our websites.

#### content aggregator
The content aggregator loops over all content, and adds it to the pelican configurations, so we can use it in our webesites. 

#### bibtex loader
The bibtex loader does the same for the bib files from our publications. While all content already exists, the bib files are automatically generated later down the line, therefore, we use a separate script to parse the bibfiles to pelican. 

#### edit-url
This is a small functionality that is added as a button on our pages with markdown content. Clicking this button allows you to directly edit the markdown file in our github repo.  

#### fileutil
This plugin adds a few python functions that can be used in html files. For example, it contains a function that sorts group members based on their name.

#### imgutil
This plugin adds a functionality that forces images to be rendered in a specific size. The image optimization script makes different versions (with different sizes) of the same image. Normally the size of the rendered images are determined by the size of the screen on which the website is rendered. In specific cases we want to hardcode this, with this plugin.  --Not sure if 100% correct 

#### inline extend
This plugin allows us to make klickable links on our website with relative ease. --double check how we use this

#### pagehierachy
This plugin helps us by setting up the url hierarchy in the same manner as our website folders are organised in our repo. For example, just like the website-pathology folder has a /projects and /members folder, its site has the following urls: https://www.computationalpathologygroup.eu/projects/, and https://www.computationalpathologygroup.eu/members/

### publication pipeline
#### diag-literature
#### parse publications
#### bibliography

### imgoptim
#### optimize images
The images on our website are optimized to make our websites more lightweight. The script makes different versions with different sizes of the same image. When the website is rendered, the images used are determined by the size of the screen, to prevent rendering unnecessarily big images while only displayed small. This makes our websites load more quickly. Google likes this and therefore puts our website higher in the seach results. 

## part 3

### netlify
Netlify is used to build an deploy our websites. We trigger this with GitHub actions. 
### hosting (yourhosting)
yourhosting.nl hosts our domain names. 
### dns
DNS links our domain names to our websites deployed by Netlify
### assets

### deploy

### github actions / website deployment pipeline
In the .github folder > workflows the github actions are stored. Within the repo's README file there is a button on top that whows whether the master branch deploys succesfully (green) or not (red). If built unsuccessfully, you can start debugging by inspecting the github actions tab, and check the error messages within the corresponding failed build. If a build fails, websites will still remain online since it will continue to show the last successful build.

#### deploy-master.yml 
The "deploy-master.yml" file describes how the master branch is deployed using netlify. This github action is triggered when changes are comitted/pushed to the master branch. 

Roughly, this script first cancels all running actions, then runs the defined steps for all of the websites defined in the matrix (like a for loop). In these steps, first some dependencies are installed using yarn (similar to npm/ pip/ conda install) including netlify, then it calls the build-and-deploy's action.yml (.github folder > workflows > actions > build-and-deploy > action.yml). 

Within this action.yml file, python dependencies are installed via pip and the requirements.txt file. Then, it executes parse_publications.sh, and copy_content.sh. Then it builds the website using the deploy.sh script. The main thing the deploy.sh script does is: pelican content -s publishconf.py. This adds the publishconf pelican configurations (for example containing the corresponding website's domain url) to pelican, and then builds the website. Once the website is built, it is deployed to netlify.

#### deploy-develop.yml
The "deploy-develop.yml" is used to deploy the develop branch. This is for example used to check out big layout changes of our websites, which is generally not a task for the webteam.

#### images.yml
The "images.yml" file is used to optimize the images used on our sites to make our sites more lightweight. Ofcouse a faster loading site is better, but another side effect of a well optimized site is that google will like your site and make it more findable (show your site higher in google's search results)

### webteam deploy bot
#### webteam deploy bot, used for deploying the wesbites
#### two secrets 
    1. curl diag.bib (used in parse publications)
    2. workflow dispatch (used in github action diag-literature)

### development branch / deploy

### security

### google analytics

### colofon
The colofon is linked on the bottom of our websites, and shows which packages and projects are used to build our websites. 

### techdocs and documentation website 
 
---
