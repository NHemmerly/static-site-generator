import re

def extract_markdown_images(text):
    images = []
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    for md in re.findall(pattern, text):
        print(md)
        images.append(md)
    return images

def extract_markdown_links(text):
    links = []
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    for md in re.findall(pattern, text):
        print(md)
        links.append(md)
    return links
    