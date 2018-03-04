const path = require('path');
const webpack = require('webpack');


module.exports = {
    entry: './list_js/app.js',
    output: {
        path: path.resolve(__dirname, 'listsi/static'),
        filename: 'list.js'
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: "babel-loader",
                query: {
                    presets: ['react']
                }
            }
        ],
    },
    stats: {
        colors: true
    }
};
