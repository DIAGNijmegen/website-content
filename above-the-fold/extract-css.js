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
  {id: 'home', url: 'http://localhost:8000/'},
  {id: 'index', url: 'http://localhost:8000/highlights/'},
  {id: 'page', url: 'http://localhost:8000/contact/'},
  {id: 'article', url: 'http://localhost:8000/highlights/mitosis-detection-in-he/'},
  {id: 'people', url: 'http://localhost:8000/members/'},
  {id: 'people-single', url: 'http://localhost:8000/members/jeroen-van-der-laak/'},
  {id: 'projects', url: 'http://localhost:8000/projects/'},
  {id: 'project-single', url: 'http://localhost:8000/projects/deeppca/'},
  {id: 'software', url: 'http://localhost:8000/software/'},
  {id: 'publications', url: 'http://localhost:8000/publications/'},
  {id: 'publications-author', url: 'http://localhost:8000/publications/jeroen-van-der-laak/'},
  {id: 'publication-thesis', url: 'http://localhost:8000/publications/bejn17a/'},
  {id: 'publication', url: 'http://localhost:8000/publications/bejn18a/'},
  {id: 'presentations', url: 'http://localhost:8000/presentations/'},
  {id: 'presentation-single', url: 'http://localhost:8000/presentations/midl-streaming/'},
  {id: 'thesis-gallery', url: 'http://localhost:8000/thesis-gallery//'},
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
