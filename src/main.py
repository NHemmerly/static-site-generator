from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from node_split import node_delimiter_split, split_nodes_image, split_nodes_link, text_to_textnodes
from extract_markdown import extract_markdown_images, extract_markdown_links


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
    text = "This is **text** with an *italic* word and a `code block`"
    print(text_to_textnodes(text))
if __name__ == "__main__":
    main()