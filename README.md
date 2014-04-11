Lunr.HTML.Scrape.Search
=======================

Test repo: Scrape HTML files, build a Lunr index, and search. Requires python and node.

Edit scrape_data.py to point to the HTML directories you want to scrape. Then run:
```
python scrape_data.py
node build_index.js
```
The index.html page runs search.js to load the new index.
