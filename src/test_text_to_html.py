import unittest

from main import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

class testTextToHTML(unittest.TestCase):
    def test_text(self):
        text_node = TextNode("testing", TextType.TEXT)
        self.assertEqual(text_node_to_html_node(text_node), LeafNode(None, "testing"))

    def test_bold(self):
        bold_node = TextNode("testing", TextType.BOLD)
        self.assertEqual(text_node_to_html_node(bold_node), LeafNode("b", "testing"))

    def test_italic(self):
        italic_node = TextNode("testing", TextType.ITALIC)
        self.assertEqual(text_node_to_html_node(italic_node), LeafNode("i", "testing"))

    def test_code(self):
        code_node = TextNode("testing", TextType.CODE)
        self.assertEqual(text_node_to_html_node(code_node), LeafNode("code", "testing"))

    def test_link(self):
        link_node = TextNode("testing", TextType.LINK, "https://testing.com")
        self.assertEqual(text_node_to_html_node(link_node).to_html(), '<a href="https://testing.com">testing</a>')

    def test_image(self):
        image_node = TextNode("testing", TextType.IMAGE, "https://testing.com/image")
        self.assertEqual(text_node_to_html_node(image_node).to_html(), '<img src="https://testing.com/image" alt="testing"></img>')

        

if __name__ == "__main__":
    unittest.main()