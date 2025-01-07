import re
from functools import reduce
from htmlnode import HTMLNode, LeafNode, ParentNode

def is_ordered_list(lines):
    i = 1
    num_pattern = r"[0-9]+"
    out = True
    for line in lines:
        if int(re.findall(num_pattern, line)[0]) == i: 
            out = out and True
            i += 1
        else: out = out and False
    return out


def markdown_to_blocks(markdown):
    out_list = markdown.split("\n\n")
    new_list = []
    for line in out_list:
        if line == "":
            continue
        line = line.strip()
        new_list.append(line)
    return new_list

def block_to_block_type(block):
    lines = block.split("\n")
    ul_pattern = r"^\*\s+.+$|^-\s+.+$"
    ol_pattern = r"^[0-9]+\.\s+.+$"
    i = 0
    heading = r"^#{1,6}\s+.+$"
    code = lines[0][0:3] == "```" and lines[-1][-3:] == "```"
    quote = reduce(lambda y, x: x[0] == ">" and y, lines, True)
    unordered_list = all(re.search(ul_pattern, line) for line in lines)
    ordered_list = all(re.search(ol_pattern, line) for line in lines) and is_ordered_list(lines)
    if re.search(heading, block):
        return "Heading"
    elif code:
        return "Code"
    elif quote:
        return "Quote"
    elif unordered_list:
        return "Unordered List"
    elif ordered_list:
        return "Ordered List"
    else:
        return "Paragraph"

def create_node_type(node, type):
    match (type):
        case "Heading":
            num = len(re.match(r"^#{1,6}",node).group())
            return LeafNode(f"h{num}", node.split(" ", 1)[1].lstrip())
        case "Quote":
            return LeafNode("blockquote", re.sub(r">\s+", "", node))
        case "Unordered List":
            

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        print(block_to_block_type(block))
        nodes.append(create_node_type(block, block_to_block_type(block)))
    return nodes
