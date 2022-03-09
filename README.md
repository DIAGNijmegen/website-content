# DIAG Website content

This repository stores all the content and source code for the DIAG websites. From this repository multiple Pelican-powered websites are built, based on a central content database.

[![Build and Deploy](https://github.com/DIAGNijmegen/website-content/workflows/Build%20and%20Deploy/badge.svg)](https://github.com/DIAGNijmegen/website-content/actions)


## Websites

Live websites:

- Pathology: https://www.computationalpathologygroup.eu
- Retina: https://www.a-eyeresearch.nl
- RSE: https://rse.diagnijmegen.nl
- AI for Health: https://www.ai-for-health.nl
- RTC: https://rtc.diagnijmegen.nl
- DIAG (main website): https://www.diagnijmegen.nl

## Updating the content

Please see the [documentation](https://github.com/DIAGNijmegen/website-content/tree/master/docs) for guides on updating the sites.

## Building the website locally

Install requirements 
1. `pip install -r requirements.txt`

To build a website: 
1. Run: `./parse_publications.sh` to download diag.bib
2. Run: `WEBSITE=website-pathology ./copy_content.sh` to copy files for any website (pathology in this example).
3. cd into a website folder (e.g., website-pathology): `cd website-pathology`
4. Run pelican: `pelican --autoreload --listen`

To build the css:
1. Install npm==7.12.0 
2. Run css build in `radboudumc-theme`: `npm run deploy-watch`

## Design resources

If you design an image/poster or similar for the website, please store the
design files (if not too big) in the directoy `content/src/` in the apropriate
subtree. This allows others to update media more easily should they ever become
outdated.
