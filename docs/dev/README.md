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
    - edit-url
    - fileutil
    - pagehierachy
    - imgutil
    - inline extend
    - bibtex loader
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

Locally 

To get website local running, the following steps need to be taken

    - clone repository 
    - install requirements (recommendation is to use a conda/virtual environment)

Docker

A dockerfile is provided to to build a container which can be used for 



