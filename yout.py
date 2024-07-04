import os
from bs4 import BeautifulSoup

def find_first_html_file(directory):
    for file in os.listdir(directory):
        if file.endswith('.html'):
            return os.path.join(directory, file)
    return None

def save_youtube_links_from_html(input_html, output_file):
    try:
        with open(input_html, 'r', encoding='utf-8') as file:
            content = file.read()

        soup = BeautifulSoup(content, 'html.parser')
        links = soup.find_all('a', href=lambda href: href and "youtube.com/watch" in href)
        
        found_links = set()
        
        with open(output_file, 'w') as file:
            for link in links:
                href = link.get('href')
                if href not in found_links:
                    found_links.add(href)
                    file.write(f"{href}\n")
        
        print("YouTube links have been successfully saved to", output_file)
    except Exception as e:
        print("An error occurred:", e)

# Example usage
directory = '.'  # Current directory, change as needed
input_html = find_first_html_file(directory)
if input_html:
    output_file = 'youtube_links.txt'
    save_youtube_links_from_html(input_html, output_file)
else:
    print("No HTML file found in the directory.")
