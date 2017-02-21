'use strict';

var gulp = require('gulp'),
    concat = require('gulp-concat'),
    minify = require('gulp-minify'),
    sass = require('gulp-sass'),
    clean = require('gulp-clean'),
    cleancss = require('gulp-clean-css'),
    sourcemaps = require('gulp-sourcemaps'),
    merge = require('merge-stream');

gulp.task('js', function() {
    gulp.src('assets/js/*.js')
        .pipe(sourcemaps.init())
        .pipe(concat('bundle.js'))
        .pipe(minify({ext:{ src: '.js', min: '.min.js'}}))
        .pipe(sourcemaps.write())
        .pipe(gulp.dest('assets/bundles'))
});


gulp.task('css', function() {

    var cssStream =  gulp.src('assets/css/*.css')
                         .pipe(concat('css-files.css'));

    var sassStream = gulp.src('assets/css/*.scss')
                         .pipe(sass())
                         .pipe(concat('scss-files.scss'));

    merge(cssStream, sassStream)
        .pipe(sourcemaps.init())
        .pipe(concat('bundle.css'))
        .pipe(cleancss())
        .pipe(sourcemaps.write())
        .pipe(gulp.dest('assets/bundles'))
});

gulp.task('watch', function() {
    gulp.watch('assets/js/*.js', ['js'])
    gulp.watch(['assets/css/*.css', 'assets/css/*.scss'], ['css'])
});

gulp.task('clean', function() {
    gulp.src('assets/bundles', {read: false})
        .pipe(clean());
});
