from textnode import TextNode, TextType

def node_delimiter_split(node_list, delim, type):
    new_nodes = []
    for node in node_list:
        text_list = node.text.split(delim)
        for block in text_list:
            print(text_list)
            if delim in block:
                new_nodes.append(TextNode(block, type))
            elif block:
                new_nodes.append(TextNode(block, TextType.TEXT))
    return new_nodes