def create_html_from_links():
    input_file = 'links.txt'
    output_file = 'links.html'

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        outfile.write("<html>\n<body>\n<ul>\n")
        for line in infile:
            url, title = line.strip().split(" #")
            outfile.write(f'<li><a href="{url}">{title}</a></li>\n')
        outfile.write("</ul>\n</body>\n</html>")

create_html_from_links()
