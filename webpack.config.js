const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const TerserJSPlugin = require('terser-webpack-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');

module.exports = (env = {}, argv) => {
  return {
    entry: {
      'site': ['./site.js'],
    },
    output: {
      path: path.resolve(__dirname, 'static', 'bundle'),
      filename: 'site.bundle.js',
    },

    module: {
      rules: [
        {
          test: /\.css$/,
          use: [
            MiniCssExtractPlugin.loader,
            'css-loader',
          ]
        }
      ],
    },

    plugins: [
      new MiniCssExtractPlugin({
        filename: 'site.bundle.css',
      }),
    ],

    optimization: {
      minimizer: [new TerserJSPlugin({}), new OptimizeCSSAssetsPlugin({})],
    },
  };
};