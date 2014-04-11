var utf8 = require('utf8')

var lunr = require('./lunr.min.js'),
    fs = require('fs');

var idx = lunr(function () {
  this.field('title', { boost: 10 });  
  this.ref('url');  
  this.field('body');
})

fs.readFile('data.json', function (err, data) {
  if (err) {
    throw err;
  }
  var pages_to_index = JSON.parse(data);
  buildIndex(pages_to_index);
});

function buildIndex(pages_to_index) {
    var len = pages_to_index.pages.length;
    
    for (var i = 0; i < len; i++) {
        idx.add(pages_to_index.pages[i]);
    }
    var index_to_write = "var the_index = " + JSON.stringify(idx);
    index_encoded = utf8.encode(index_to_write);
    fs.writeFile('./index.js', index_encoded, 'utf8', function (err) {
        if (err) {
            throw err;
        } else {
        console.log('done');
        }
    });
}