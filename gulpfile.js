'use strict';

var gulp = require('gulp'),
    concat = require('gulp-concat'),
    concatCss = require('gulp-concat-css'),
    minify = require('gulp-minify'),
    sass = require('gulp-sass'),
    util = require('gulp-util'),
    clean = require('gulp-clean'),
    cleancss = require('gulp-clean-css'),
    sourcemaps = require('gulp-sourcemaps'),
    merge = require('merge-stream');


var production = !!util.env.production;


gulp.task('js', function() {

    gulp.src('assets/js/*.js')
        .pipe(sourcemaps.init())
        .pipe(concat('bundle.js'))
        .pipe(production ? minify() : util.noop())
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('build'))
});


gulp.task('css', function() {

    var cssStream =  gulp.src('assets/css/*.css')
                         .pipe(concatCss('css-files.css'));

    var sassStream = gulp.src('assets/scss/simple.scss')
                         .pipe(sass({
                           includePaths: [
                             'assets/scss/partials',
                             'node_modules/bootstrap-sass/assets/stylesheets'
                           ]
                         }))
                         .pipe(concatCss('scss-files.scss'));

    merge(cssStream, sassStream)
        .pipe(sourcemaps.init())
        .pipe(concat('bundle.css'))
        .pipe(production ? cleancss() : util.noop())
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('build'))
});


gulp.task('build', ['js', 'css']);

gulp.task('watch', function() {
    gulp.watch('assets/js/*.js', ['js'])
    gulp.watch(['assets/css/*.css', 'assets/scss/**.scss'], ['css'])
});


gulp.task('clean', function() {
    gulp.src('build', {read: false}).pipe(clean());
});


gulp.task('default', ['watch'])
