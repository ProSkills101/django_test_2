const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const TerserJSPlugin = require('terser-webpack-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');

module.exports = (env = {}, argv) => {
  return {
    entry: {
      'vendor': ['./vendor.js'],
    },
    output: {
      path: path.resolve(__dirname, 'static', 'bundle'),
      filename: 'vendor.bundle.js',
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
        filename: 'vendor.bundle.css',
      }),
    ],

    optimization: {
      minimizer: [new TerserJSPlugin({}), new OptimizeCSSAssetsPlugin({})],
    },
  };
};