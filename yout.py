import os
from bs4 import BeautifulSoup

def find_first_html_file(directory):
    # Scan the directory for any file that ends with .html
    for file in os.listdir(directory):
        if file.endswith('.html'):
            return os.path.join(directory, file)
    return None  # Return None if no HTML file is found

def save_youtube_links_from_html(input_html, output_file):
    try:
        # Open and read the HTML file
        with open(input_html, 'r', encoding='utf-8') as file:
            content = file.read()

        soup = BeautifulSoup(content, 'html.parser')

        # Find all anchor tags with a href that contains "youtube.com/watch"
        links = soup.find_all('a', href=lambda href: href and "youtube.com/watch" in href)
        found_links = {}

        # We will keep track of each link and only take action every third occurrence
        link_count = {}

        with open(output_file, 'w') as file:
            for link in links:
                href = link.get('href')
                # Increment the count for this specific link
                if href in link_count:
                    link_count[href] += 1
                else:
                    link_count[href] = 1

                # Check if this is the third occurrence of the link
                if link_count[href] == 3:
                    title = link.get('title', 'No title available')

                    # Ensure each link is saved only once with its title
                    if href not in found_links:
                        found_links[href] = title
                        file.write(f"{href} #{title}\n")

        print("YouTube links have been successfully saved to", output_file)
    except Exception as e:
        print("An error occurred:", e)

# Example usage
directory = '.'  # Current directory, change as needed
input_html = find_first_html_file(directory)  # Find the first HTML file in the directory
if input_html:
    output_file = 'youtube_links.txt'
    save_youtube_links_from_html(input_html, output_file)
else:
    print("No HTML file found in the directory.")

