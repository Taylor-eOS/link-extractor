import os
from bs4 import BeautifulSoup

def find_first_html_file(directory):
    for file in os.listdir(directory):
        if file.endswith('.html'):
            return os.path.join(directory, file)
    return None  # Return None if no HTML file is found

def save_chatgpt_links_from_html(input_html, output_file):
    try:
        with open(input_html, 'r', encoding='utf-8') as file:
            content = file.read()

        soup = BeautifulSoup(content, 'html.parser')

        links = soup.find_all('a', href=lambda href: href and "https://chatgpt.com/c" in href)

        with open(output_file, 'w') as file:
            for link in links:
                href = link.get('href')
                title = link.text.strip() if link.text else 'No title available'
                file.write(f"{href} #{title}\n")

        print("ChatGPT links have been successfully saved to", output_file)
    except Exception as e:
        print("An error occurred:", e)

directory = '.'  # Current directory, change as needed
input_html = find_first_html_file(directory)  # Find the first HTML file in the directory
if input_html:
    output_file = 'links.txt'
    save_chatgpt_links_from_html(input_html, output_file)
else:
    print("No HTML file found in the directory.")

