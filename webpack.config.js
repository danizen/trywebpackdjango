var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker')



module.exports = {
  context: path.resolve('assets'),

  entry: './app',

  output: {
    path: path.resolve('./build'),
    filename: 'bundle.js'
  },

  plugins: [
    new BundleTracker({ path: __dirname, filename: 'webpack-stats.json' })
  ],

  module: {
    loaders: [
      {
        test: /\.css$/,
        exclude: /node_modules/,
        loader: 'css-loader!style-loader'
      }
    ]
  },

  resolve: {
    extensions: ['.js']
  }
};

