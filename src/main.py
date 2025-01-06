from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from node_split import node_delimiter_split, split_nodes_image, split_nodes_link, text_to_textnodes
from extract_markdown import extract_markdown_images, extract_markdown_links
from block_markdown import markdown_to_blocks, block_to_block_type


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

def main():
    print("Hello SSG")
    text = """# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item* This is another list item"""
    test = "1. s is a test\n2. testing\n4. still testing"
    blocks = markdown_to_blocks(text)
    print(blocks[0])
    print(block_to_block_type(test))
if __name__ == "__main__":
    main()