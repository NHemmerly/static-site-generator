from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from node_split import node_delimiter_split


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
    first_node = TextNode("This is my first node", TextType.BOLD, "http://localhost:8888")
    node = TextNode("This is text with a code block word", TextType.TEXT)
    new_nodes = node_delimiter_split([node], "`", TextType.CODE)
    print(new_nodes)
    print(first_node)

if __name__ == "__main__":
    main()