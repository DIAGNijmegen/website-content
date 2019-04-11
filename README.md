# website-content
This repository stores all the content for the diag websites

[![Build Status](https://travis-ci.org/DIAGNijmegen/website-content.svg?branch=master)](https://travis-ci.org/DIAGNijmegen/website-content)


## Building the website locally

1. Run `build.sh`
2. Use browser sync in a one of the website directories: `browser-sync start --server output --files output`
3. Run pelican in `website-pathology`: `pelican content --autoreload  --output output`
4. Run css build in `radboudumc-theme`: `npm run deploy-watch`


## Design resources

If you design an image/poster or similar for the website, please store the
design files (if not too big) in the directoy `content/src/` in the apropriate
subtree. This allows other to update media more easily should they ever become
outdated.