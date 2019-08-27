# #!/usr/bin/env bash

# Break build on error, prevents websites going offline in case of pelican errors
set -e

# List of websites to build
declare -a websites=("website-diag" "website-pathology" "website-neuro" "website-rse" "website-retina" "website-bodyct" "website-aiimnijmegen" "website-rtc")

for website in "${websites[@]}"
do

  # Copy bib generator script
  cp -r plugins/bibtex $website/plugins
  cp plugins/bib_writer.py $website/plugins/bib_writer.py

  # Copy literature
  cp content/diag.bib $website/content/diag.bib

  cd $website

  # Run the bib plugin
  python plugins/bib_writer.py
done
