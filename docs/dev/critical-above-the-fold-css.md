# Critical css

Following web dev recommendations on [critical css](https://web.dev/extract-critical-css/), we generate critical css for all templates. This css is embeded on each page and makes sure that the above-the-fold content of the website renders properly, even without the main css file.

## Generating the critical css

The critical css is not generated at each built as it only changes due to (large) changes in the theme. Instead, the critical css can be generated using a NodeJS script:

`
cd above-the-fold
npm run critical
`

The script generates a critical css file for each template, which is stored in the template folder under `radboudumc-template > templates > critical_css`.
