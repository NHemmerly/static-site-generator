from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from node_split import node_delimiter_split, split_nodes_image, split_nodes_link, text_to_textnodes
from extract_markdown import extract_markdown_images, extract_markdown_links
from block_markdown import markdown_to_blocks, block_to_block_type, markdown_to_html_node


def main():
    print("Hello SSG")
    text = "###### This *is* a heading\n\n> test\n> test2\n\n* ul1\n* ul2\n\n1. test1\n2. test2\n\n```test this out bruv```\n\nthis is a paragraph"
    test = "1. s is a test\n2. testing\n4. still testing"
    blocks = markdown_to_blocks(text)
    print(blocks[0])
    print(markdown_to_html_node(text))
if __name__ == "__main__":
    main()