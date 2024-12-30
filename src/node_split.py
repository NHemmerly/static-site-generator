from textnode import TextNode, TextType

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