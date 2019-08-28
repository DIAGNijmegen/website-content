# #!/usr/bin/env bash

# Break build on error, prevents websites going offline in case of pelican errors
set -e

for website in $WEBSITES_WITH_BIB
do

  # Copy bib generator script
  cp -r plugins/bibtex $website/plugins
  cp plugins/bib_writer.py $website/plugins/bib_writer.py

  # Copy literature
  cp content/diag.bib $website/content/diag.bib

  cd $website

  # Run the bib plugin
  python plugins/bib_writer.py

  cd ..
done
