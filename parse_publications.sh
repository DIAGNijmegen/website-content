# #!/usr/bin/env bash

set -e

curl -H "Authorization: token ${GH_BIB_TOKEN}" \
    -o content/diag.bib \
    -s \
    -L https://raw.githubusercontent.com/AIforAnesthesiology/website-content/master/content/diag.bib

curl -H "Authorization: token ${GH_BIB_TOKEN}" \
    -o content/fullstrings.bib \
    -s \
    -L https://raw.githubusercontent.com/AIforAnesthesiology/website-content/master/content/fullstrings.bib

python ./bibliography/bibparser.py
