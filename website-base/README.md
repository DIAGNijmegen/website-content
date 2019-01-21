# Radboudumc Pelican Website Template

[![Build Status](https://travis-ci.org/DIAGNijmegen/website-base.svg?branch=master)](https://travis-ci.org/DIAGNijmegen/website-base)

Base Pelican setup for websites related to the DIAG group.

[Online demo](https://diagnijmegen.github.io/website-base/)

**Components**

This project consists of four subprojects:

1. A Pelican static site.
2. Publications pipeline
3. A sass-powered Radboudumc theme built on top of bootstrap.
4. An above-the-fold css extraction tool.

## Static site by Pelican

### Installation

Install the requirements from `requirements.txt`:

```
pip install -r requirements.txt
```

### Usage

Run in main directory:

```
pelican content --autoreload  --output output --settings pelicanconf.py
```

This runs a local build of the site with auto-reload enabled.

### Server

A server can be ran using the built in Pelican-python server:

```
# Run in output directory
python -m pelican.server
```

Or, if available, using browser-sync:

```
# Run in repository root
browser-sync start --server output --files output
```

## Publications pipeline

The publications pipeline needs manual execution. It parses the content/diag.bib file to create the markdown files in content/pages/publications needed by pelican to create the pages for every publication.

```
# Run in repository root
python plugins/bib_writer.py
```

## Radboudumc theme

The theme requires Nodejs and npm to be built.

### Installation

```
npm --prefix radboudumc-theme install
```

### Usage

For testing purposes:

```
npm --prefix radboudumc-theme run deploy-watch
```

For a new build:

```
npm --prefix radboudumc-theme run deploy
```

## Above the fold

The above-the-fold script requires Nodejs and npm to be built. This script is only required for production sites as it optimizes the css delivery. It is not required for local development or testing.

### Installation

```
npm --prefix above-the-fold install
```

### Usage

```
npm --prefix above-the-fold run critical
```
