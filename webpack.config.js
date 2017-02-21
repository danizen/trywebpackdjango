var path = require('path');
var webpack = require('webpack');
//var BundleTracker = require('webpack-bundle-tracker')
//var ExtractTextPlugin = require('extract-text-webpack-plugin')

// new ExtractTextPlugin('bundle.css')


module.exports = {
  context: path.resolve('assets'),

  entry: './app',

  output: {
    path: path.resolve('./build'),
    filename: 'bundle.js'
  },

  //plugins: [
  //  new BundleTracker({ path: __dirname, filename: 'webpack-stats.json' }),
  //],

  module: {
    loaders: [
      {
        test: /\.css$/, exclude: /node_modules/, loader: 'style-loader!css-loader'
      }
    ]
  },

  resolve: {
    extensions: ['.js']
  }
};

