# #!/usr/bin/env bash

# List of websites to build
declare -a websites=("website-base")

python parse_content.py
python plugins/bib_writer.py

for website in "${websites[@]}"
do
  echo "Building $website"

  # Copy content
  cp -r --no-clobber content "$website"

  cd $website
  pwd

  # Fetch repo
  #rm -rf output
  #git clone --single-branch --depth 1 --branch gh-pages https://diagwebteam:${GH_PAGES}@github.com/diagnijmegen/${website}.git output
  #cd output
  #git pull

  # Build pelican website
  pelican content -s publishconf.py

  #git push --repo diagnijmegen/${website} -f origin gh-pages
  #cd ..

  # Go back to root directory
  cd ..
done
