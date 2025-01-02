import re

def extract_markdown_images(text):
    new_text = text
    images = []
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    for md in re.findall(pattern, new_text):
        images.append(md)
    return images

def extract_markdown_links(text):
    new_text = text
    links = []
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    for md in re.findall(pattern, new_text):
        links.append(md)
    return links
    