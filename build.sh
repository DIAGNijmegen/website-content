# #!/usr/bin/env bash

# List of websites to build
declare -a websites=( "website-pathology") #"website-base" "website-retina")

# Distribute the content pages
python parse_content.py

for website in "${websites[@]}"
do
  echo "Building $website"

  # Copy default base pages
  cp -r content/pages/defaults/. $website/content/pages/
  # Copy images
  cp -r --no-clobber content/images $website/content
  # Copy bib generator script
  cp -r plugins/bibtex $website/plugins
  cp plugins/bib_writer.py $website/plugins/bib_writer.py

  # Copy literature
  cp content/diag.bib $website/content/diag.bib
  cp content/dict_pubs.json $website/content/dict_pubs.json

  cd $website
  pwd

  # Generate publications
  python plugins/bib_writer.py

  # Build pelican website
  pelican content -s publishconf.py

  # Copy files for github
  cp CNAME output/CNAME
  cp README.md output/README.md
  # Go back to root directory
  cd ..
done
