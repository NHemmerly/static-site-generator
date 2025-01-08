from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from node_split import node_delimiter_split, split_nodes_image, split_nodes_link, text_to_textnodes
from extract_markdown import extract_markdown_images, extract_markdown_links
from block_markdown import markdown_to_blocks, block_to_block_type, markdown_to_html_node


def main():
    print("Hello SSG")
    test = ParentNode("div", [ParentNode("h1", [LeafNode(None, "Header")]),
                                        ParentNode("p", [LeafNode(None, "Paragraph")]),
                                        ParentNode("ul", [ParentNode("li", [LeafNode(None, "List item")]),
                                                                ParentNode("li", [LeafNode(None, "List item")])]),
                                                                ParentNode("p", [LeafNode("a", "link",  {"href":"link.com"})]),
                                                                ParentNode("p", [LeafNode("img", {"src":"image.com", "alt":"image"})]),
                                                                ParentNode("p", [LeafNode("i", "italics")]), ParentNode("p", [LeafNode("b", "bold")])])
    text = """# Header

Paragraph

- List item
- List item

[link](link.com)

![image](image.com)

*italics*

**bold**
"""
    print(markdown_to_html_node(text).to_html())
    print(test.to_html())
if __name__ == "__main__":
    main()