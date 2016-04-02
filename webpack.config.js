var webpack = require("webpack");

module.exports = {
  entry: [
    'webpack-dev-server/client?http://localhost:3000',
    'webpack/hot/dev-server',
    './scripts/demo',
  ],
  output: {
    path: __dirname,
    filename: 'bundle.js',
    publicPath: '/build/',
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin()
  ],
  module: {
    loaders: [
      // Babel with ES2015/React presets for .jsx files
      { test: /\.css$/, loader: "style-loader!css-loader" },
      {
        test: /\.jsx$/,
        exclude: /(node_modules)/,
        loaders: [
          'react-hot',
          'babel?cacheDirectory=data/babel,presets[]=react,presets[]=es2015,presets[]=stage-0',
        ],
      },
    ]
  },

  debug: true,
  devtool: 'cheap-module-source-map',
  resolve: {
    extensions: ['', '.js', '.jsx'],
    alias: {
    },
  },
};
