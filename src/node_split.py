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
    text = ""
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            text = node.text
        else: 
            new_nodes.append(node)
            continue
        images = extract_markdown_images(text)
        if len(images) == 0:
            new_nodes.append(node)
        for image in images:
            substring = f"![{image[0]}]({image[1]})"
            sections = text.split(substring, 1)
            if len(sections) != 2:
                raise ValueError("Image tag not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        links = extract_markdown_links(text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link in links:
            substring = f"[{link[0]}]({link[1]})"
            sections = text.split(substring, 1)
            if len(sections) != 2:
                raise ValueError("Link tag not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    old_nodes = [TextNode(text, TextType.TEXT)]
    out_nodes = []
    out_nodes = (split_nodes_link(old_nodes))
    out_nodes = (split_nodes_image(out_nodes))
    out_nodes = (node_delimiter_split(out_nodes, '`', TextType.CODE))
    out_nodes = (node_delimiter_split(out_nodes, '**', TextType.BOLD))
    out_nodes = (node_delimiter_split(out_nodes, '*', TextType.ITALIC))
    
    return out_nodes