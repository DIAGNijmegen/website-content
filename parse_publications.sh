# #!/usr/bin/env bash

curl -o content/diag.bib -u ${BIB_TOKEN} ${DIAG_BIB_REPO}diag2020.bib >/dev/null 2>&1
curl -o content/fullstrings.bib -u ${BIB_TOKEN} ${DIAG_BIB_REPO}fullstrings.bib >/dev/null 2>&1

python ./bibliography/bibparser.py
