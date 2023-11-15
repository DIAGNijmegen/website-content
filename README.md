# DIAG Website content

[![Build and Deploy](https://github.com/DIAGNijmegen/website-content/workflows/Build%20and%20Deploy/badge.svg)](https://github.com/DIAGNijmegen/website-content/actions)
[![Optimize Images](https://github.com/DIAGNijmegen/website-content/actions/workflows/images.yml/badge.svg)](https://github.com/DIAGNijmegen/website-content/actions/workflows/images.yml)

This repository stores all the content and source code for the DIAG websites. From this repository multiple Pelican-powered websites are built, based on a central content database.


## Websites

Live websites:

- Pathology: https://www.computationalpathologygroup.eu
- RSE: https://rse.diagnijmegen.nl
- AI for Health: https://www.ai-for-health.nl
- RTC: https://rtc.diagnijmegen.nl
- DIAG (main website): https://www.diagnijmegen.nl

## Updating the content

Please see the [documentation](https://github.com/DIAGNijmegen/website-content/tree/master/docs) for guides on updating the sites.

## Building the website locally

Requirements: Linux environment (on Windows via WSL) and Python 3  (we use Ubuntu with conda/miniconda istalled and a conda environment with PYTHON=3.9)

Preparations:
1. Clone website content (if on windows, do this from WSL/ubuntu commandline). cd into website-content
3. Install dependencies: `pip install -r requirements.txt`
4. Run `bash ./parse_publications.sh` to download and parse the publication files.
5. Run: `LOCAL=1 WEBSITE=website-pathology bash ./copy_content.sh` to copy files for any website. If you get an error `cp: cannot create directory 'website-pathology/output/images': No such file or directory`, then you should make this folder: `mkdir -p website-pathology/output/images` and try again

Building the website:
1. cd into the website folder: `cd website-pathology`
2. Run pelican: `pelican --autoreload --listen`
3. Visit `http://localhost:8000`

To build the css:
1. Install npm==7.12.0 
2. Run css build in `radboudumc-theme`: `npm run deploy-watch`

To automatically build and host the website in a docker image, follow the instruction in the docker folder. 

## Design resources

If you design an image/poster or similar for the website, please store the
design files (if not too big) in the directoy `content/src/` in the apropriate
subtree. This allows others to update media more easily should they ever become
outdated.


## Pipeline
![pipeline](./pipeline.png)


