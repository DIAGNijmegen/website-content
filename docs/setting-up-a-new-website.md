# Setting up a new website

This file describe the steps to set up a new website.

## 1. Setting up the repository

1. Create a new repository for the website at `DIAGNijmegen/website-{website name}`.
2. Make sure that `DIAGWebTeam` user has write access to this repository; this can be done by adding this user as a collaborator.

## 2. Configure the domain

1. Check with the group which domain name they want to use, e.g. `{group}.diagnijmegen.nl` or `www.{group}.nl`.
2. Setup the DNS records, see https://help.github.com/en/articles/quick-start-setting-up-a-custom-domain

## 3. Create a new website directory

1. In the `website-content` repository, copy the contents of `website-base` to a new directory with the same name as the new repositiory (e.g. `website-{website name}`).
2. Update `pelicanconf.py` if needed, e.g. change the name of the website. 
3. Update `publishconf.py`, set `SITEURL` to the correct value (the URL where the website should be accessible).

## 4. Create a new deploy step

1. Update `parse_content.py` (in the root directory) by adding the new site, see https://github.com/DIAGNijmegen/website-content/blob/master/parse_content.py#L6
2. Update `travis.yaml` and add a new deploy step at the bottom. See the other deploy steps for an example. Set the `fqdn` variable to the website URL.
3. Update build.sh and add new website to websites to build: declare -a websites= 

## 5. Publish

1. Commit your changes, Travis should now build and deploy the website.
