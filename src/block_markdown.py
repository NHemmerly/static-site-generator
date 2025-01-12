import re
from functools import reduce
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType
import node_split

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

def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case(TextType.TEXT):
            return LeafNode(None, text_node.text)
        case(TextType.BOLD):
            return LeafNode("b", text_node.text)
        case(TextType.ITALIC):
            return LeafNode("i", text_node.text)
        case(TextType.CODE):
            return LeafNode("code", text_node.text)
        case(TextType.LINK):
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case(TextType.IMAGE):
            return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
        case _:
            raise Exception("Text type not recognized")


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

def textnode_child(text):
    text_nodes = node_split.text_to_textnodes(text)
    child_nodes = []
    for node in text_nodes:
        child_nodes.append(text_node_to_html_node(node))
    return child_nodes

def create_node_type(node, type):
    match (type):
        case "Heading":
            num = len(re.match(r"^#{1,6}",node).group())
            children = textnode_child(node.split(" ", 1)[1].lstrip())
            return ParentNode(f"h{num}", children)
        case "Quote":
            text = re.sub(r">\s+", "", node)
            children = textnode_child(text)
            return ParentNode("blockquote", children)
        case "Unordered List":
            unordered_list = ParentNode("ul", [])
            for bullet in node.split("\n"):
                bullet_text_children = textnode_child(re.sub(r"^\*\s+|^-\s+","",bullet))
                unordered_list.children.append(ParentNode("li", bullet_text_children))
            return unordered_list
        case "Ordered List":
            ordered_list = ParentNode("ol", [])
            for num in node.split("\n"):
                num_text_children = textnode_child(re.sub(r"^[0-9]+\.\s+","",num))
                ordered_list.children.append(ParentNode("li", num_text_children))
            return ordered_list
        case "Code":
            pre = ParentNode("pre", [])
            pre.children.append(LeafNode("code", node.strip("`")))
            return pre
        case _:
            text = textnode_child(node)
            return ParentNode("p", text)
                

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        nodes.append(create_node_type(block, block_to_block_type(block)))
    div = ParentNode("div", nodes)
    return div

def extract_title(markdown):
    lines = markdown.split('\n')
    pattern = r"^#\s+.+$"
    for line in lines:
        if re.search(pattern, line):
            header = re.search(pattern, line).group()
            return header.lstrip("#").lstrip()
    raise Exception("No header found")
