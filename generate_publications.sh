# #!/usr/bin/env bash

# Break build on error, prevents websites going offline in case of pelican errors
set -e

echo "Generating publications for $WEBSITE"

# Copy bib generator script
cp -r plugins/bibtex $WEBSITE/plugins
cp plugins/bib_writer.py $WEBSITE/plugins/bib_writer.py

# Copy literature
cp content/diag.bib $WEBSITE/content/diag.bib

cd $WEBSITE

# Run the bib plugin
python plugins/bib_writer.py

cd ..
