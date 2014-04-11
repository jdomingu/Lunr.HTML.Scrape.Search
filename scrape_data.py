import os
import re
from bs4 import BeautifulSoup

def scrapeAll():
    scrapeDirectory("./ExpressServer9/content")
    scrapeDirectory("./ExpressZip9/content")
    scrapeDirectory("./GeoExpress9/content")
    
def scrapeDirectory(dir_name):
    for file_name in os.listdir(dir_name):
        url = dir_name + '/' + file_name
        #Debug only
        #print dir_name + '/' + file_name
        
        #Skip directories
        if os.path.isdir(url): 
            continue
            
        with open(url) as page_raw:
            page_data = BeautifulSoup(page_raw.read())
        
        #Get the page title
        if page_data.h2 is not None: 
            title = page_data.h2.text
        elif page_data.h3 is not None:
            title = page_data.h3.text
        elif page_data.h1 is not None: 
            title = page_data.h1.text
        elif page_data.h4 is not None:
            title = page_data.h4.text
        else:
            #It's OK to skip files without a title. This only includes copyright topics,
            #preface topics, glossaries, etc.
            print "Skipping. Could not find a title in " + url
            continue            
        
        #Save the title and URL fields
        title_without_spaces = ' '.join(title.split())
        out_data.write('{"title": ' + '"' + title_without_spaces.encode('ascii') +  '",')
        out_data.write('"url": ' + '"' + url +  '",')
        
        #Get the body text
        body = ""
        #Scrape all <p> tags. Skip the first paragraph with the navigation link.
        for para in page_data.find_all('p')[1:]:
            try:
                para_without_spaces = ' '.join(para.text.split())
                alpha_only_para = re.sub(r'[^a-zA-Z0-9\.\,\d\s:]', '', para_without_spaces)
                body += ' ' + alpha_only_para
            except:
                print "Error parsing paragraph data in " + file_name
        #Scrape all lists, tables, and subheadings
        for content in page_data.find_all(['li', 'th', 'td', 'h3', 'h4']):
            try:
                content_without_spaces = ' '.join(content.text.split())
                alpha_only_content = re.sub(r'[^a-zA-Z0-9\.\,\d\s:]', '', content_without_spaces)
                body += ' ' + alpha_only_content
            except:
                print "Error parsing data in " + file_name
        
        out_data.write('"body": ' + '"' + body.encode('ascii') +  '"},')
 
 
out_data = open('data.json', 'w+')
out_data.write('{"pages": [')
scrapeAll()
#Remove the comma from the last entry
out_data.seek(-1, os.SEEK_END)
out_data.truncate()
out_data.write(']}')
print("Done")
