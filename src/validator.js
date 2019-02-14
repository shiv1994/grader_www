// imports
const nodeW3CValidator = require('node-w3c-validator');
 
// paths
const validatePath = '../public/*.html';
// or directly to the file - './dist/index.html'
// or a glob pattern - './dist/**/*.html'
const resultOutput = 'result.html';
 
// validate
nodeW3CValidator(validatePath, {
    format: 'html',
    skipNonHtml: true,
    verbose: true
}, function (err, output) {
    if (err === null) {
        return;
    }
    console.log(output);
    nodeW3CValidator.writeFile(resultOutput, output);
});