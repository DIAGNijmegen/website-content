# DIAG Website content

This repository stores all the content and source code for the diag websites. From this repository multiple Pelican-powered websites are built, based on a central content database.

[![Build Status](https://travis-ci.org/DIAGNijmegen/website-content.svg?branch=master)](https://travis-ci.org/DIAGNijmegen/website-content)

## Websites

Live websites:

- Pathology: https://www.computationalpathologygroup.eu
- Retina: https://www.a-eyeresearch.nl
- RSE: https://rse.diagnijmegen.nl
- AI for Health: https://www.ai-for-health.nl
- AIIM: https://www.aiimnijmegen.nl
- RTC: https://rtc.diagnijmegen.nl

Websites in development

- Bodyct: https://bodyct.diagnijmegen.nl
- Neuro: https://diagnijmegen.github.io/website-neuro/ (temporary)
- DIAG: https://beta.diagnijmegen.nl (temporary)

## Updating the content

Please see the [documentation](https://github.com/DIAGNijmegen/website-content/tree/master/docs) for guides on updating the websites.

## Building the website locally

To build a website:

1. Run `build.sh`
2. Run pelican in `website-pathology` (or any other website): `pelican --autoreload`
3. Start the development server: `pelican --listen`

(On Non-windows you can combine step 2 and 3 with `pelican --autoreload --listen`)

To build the css:

4. Run css build in `radboudumc-theme`: `npm run deploy-watch`

## Design resources

If you design an image/poster or similar for the website, please store the
design files (if not too big) in the directoy `content/src/` in the apropriate
subtree. This allows others to update media more easily should they ever become
outdated.
