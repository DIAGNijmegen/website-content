var gulp = require('gulp');
var log = require('fancy-log');
var critical = require('critical').stream;

// Generate & Inline Critical-path CSS
gulp.task('critical', function () {
    return gulp.src(['../website-pathology/output/**/*.html', '!../website-pathology/output/publications/*/*.html'])
        .pipe(critical({
            base: '../output/',
            inline: false,
            css: ['../output/theme/css/theme.min.css'],
            dimensions: [{
                height: 200,
                width: 500
            }, {
                height: 900,
                width: 1200
            }],
            // penthouse: {
            //   screenshots: {
            //     basePath: '../screenshots',
            //     type: 'jpeg'
            //   }
            // },
            include: [
              '.breadcrumb',
              '.breadcrumb-item',
              '.jumbotron',
              '.block-primary',
              '.block-home'
            ],
        }))
        .on('error', function(err) { log.error(err.message); })
        .pipe(gulp.dest('../radboudumc-template/templates/critical_css'));
});
