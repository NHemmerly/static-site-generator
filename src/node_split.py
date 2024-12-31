from textnode import TextNode, TextType
from extract_markdown import extract_markdown_links, extract_markdown_images

def node_delimiter_split(node_list, delim, type):
    new_nodes = []
    for node in node_list:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        sections = node.text.split(delim)
        if len(sections) % 2 == 0:
            raise Exception("Invalid markdown syntax") 
        for i, section in enumerate(sections):
            if section == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(section, TextType.TEXT))
            else: new_nodes.append(TextNode(section, type))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        images = extract_markdown_images(text)
        for image in images:
            substring = f"![{image[0]}]({image[1]})"
            sections = text.split(substring, 1)
            for i, section in enumerate(sections):
                if i % 2 == 0:
                    if section == "":
                        continue
                    new_nodes.append(TextNode(section, TextType.TEXT))
                else: 
                    new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
                if len(sections) > 1:
                    text = sections[1]
                else: text = ""

    print(new_nodes)