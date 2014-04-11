var idx_string = JSON.stringify(the_index);
var idx = lunr.Index.load(JSON.parse(idx_string));

function the_search(query) {
    var result = idx.search(query);
    if (result.length !== 0) {
        var formatted_result = "<strong>Results</strong>";
        for (var i = 0; i < result.length; i++) {
            
            var url_split = result[i]['ref'].split('/');
            var url_with_nav = "./" + url_split[1] + "/index.htm#" + url_split[3]
            
            formatted_result += "<br><a href='" + url_with_nav + "'>" + url_with_nav
                + "</a>";
        }
        document.getElementById('searchResults').innerHTML = formatted_result;
    } else {
        document.getElementById('searchResults').innerHTML = "<p>No results</p>";
    }
}