// By default penthouse opens urls called in parallel in different tabs
// in the same browser, for performance reasons.
// If you need to run many pages however your machine will at some point
// (~ 10 pages) start running out of resources (causing crashes, errors and/or slowdown).
//
// Hence, better to setup a queue -
// this is just a simple example!

var penthouse = require('penthouse')
var fs = require('fs')

// populate with as many urls as you want,
// only X will be executed in parallel;
// configured at the bottom
var urls = [
  {id: 'home', url: 'https://www.computationalpathologygroup.eu/'},
  {id: 'index', url: 'https://www.computationalpathologygroup.eu/highlights/'},
  {id: 'page', url: 'https://www.computationalpathologygroup.eu/contact/'},
  {id: 'article', url: 'https://www.computationalpathologygroup.eu/highlights/mitosis-detection-in-he/'},
  {id: 'people', url: 'https://www.computationalpathologygroup.eu/members/'},
  {id: 'people-single', url: 'https://www.computationalpathologygroup.eu/members/jeroen-van-der-laak/'},
  {id: 'projects', url: 'https://www.computationalpathologygroup.eu/projects/'},
  {id: 'project-single', url: 'https://www.computationalpathologygroup.eu/projects/deeppca/'},
  {id: 'software', url: 'https://www.computationalpathologygroup.eu/software/'},
  {id: 'publications', url: 'https://www.computationalpathologygroup.eu/publications/'},
  {id: 'publications-author', url: 'https://www.computationalpathologygroup.eu/publications/jeroen-van-der-laak/'},
  {id: 'publication-thesis', url: 'https://www.computationalpathologygroup.eu/publications/bejn17a/'},
  {id: 'publication', url: 'https://www.computationalpathologygroup.eu/publications/bejn18a/'},
  {id: 'presentations', url: 'https://www.computationalpathologygroup.eu/presentations/'},
  {id: 'presentation-single', url: 'https://www.computationalpathologygroup.eu/presentations/midl-streaming/'},
  {id: 'thesis-gallery', url: 'https://www.computationalpathologygroup.eu/thesis-gallery//'},
];

// recursively generates critical css for one url at the time,
// until all urls have been handled
function startNewJob () {
  var current = urls.pop() // NOTE: mutates urls array
  if (!current) {
    // no more new jobs to process (might still be jobs currently in process)
    return Promise.resolve()
  }

  console.log(`Processing ${current.id}`);

  return penthouse({
    url: current.url,
    css: '../radboudumc-template/static/css/theme.min.css'
  })
  .then(criticalCss => {
    console.log(`-> Completed processing ${current.id}`);
    fs.writeFileSync('../radboudumc-template/templates/critical_css/' + current.id + '.css', criticalCss);
    return startNewJob();
  })
  .catch(e => {
    console.error(e);
  })
}

// how many jobs do we want to handle in paralell?
// Below, 5:
Promise.all([
  startNewJob(),
  startNewJob(),
  startNewJob(),
  startNewJob(),
  startNewJob()
])
.then(() => {
  console.log('all done!')
})
