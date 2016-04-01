var webpack = require("webpack");

module.exports = {
  entry: [
    'webpack-dev-server/client?http://localhost:3000',
    'webpack/hot/dev-server',
    './scripts/views/demo',
  ],
  output: {
    path: __dirname,
    filename: 'bundle.js',
    publicPath: '/build/',
  },
  module: {
    loaders: [
      { test: /\.jsx$/, loaders: [
        'react-hot',
        'jsx?harmony'],
      },
    ],
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin()
  ],
  resolve: {
    extensions: ['', '.js', '.jsx'],
    alias: {
    },
  },
};
