// Simple script that reads the css version number and increases it
//
const fs = require('fs');

const filePath = '../radboudumc-template/templates/blocks/css.version';

const newVersion = parseInt(fs.readFileSync(filePath));

fs.writeFile(filePath, (newVersion + 1).toString(), function (err) {
  if (err) throw err;
  console.log('Updated CSS version number.');
});
