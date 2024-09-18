import requests
from bs4 import BeautifulSoup
import re

def web_scrap(month, date):
    
    url = f'https://en.wikipedia.org/wiki/{month}_{date}'

    # Fetch the HTML content of the webpage
    response = requests.get(url)
    html_content = response.text

    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all h2 tags
    for h2_tag in soup.find_all('h2'):
        # Check if the h2 tag contains 'Events'
        if 'Events' in h2_tag.text:
            # Find all the ul tags following this h2 tag
            ul_tags = h2_tag.find_all_next('ul')

            # Extract and print the text from the first three li tags within each ul tag
            all_content=''
            for ul_tag in ul_tags[:3]:
                for li_tag in ul_tag.find_all('li'):
                    content=li_tag.text.strip()
                    filtered_content=re.sub(r'\[[0-9]*\]','',content)
                    all_content+=filtered_content+'\n'
                    #print(filtered_content)
            return (all_content)        

