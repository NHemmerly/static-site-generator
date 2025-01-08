import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, markdown_to_html_node
from htmlnode import ParentNode, LeafNode

class TestBlockMarkdown(unittest.TestCase):
    def test_out(self):
        text = """# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"""
        test = ["# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
        self.assertEqual(test, markdown_to_blocks(text))

    def test_heading(self):
        text = "# test heading"
        self.assertEqual("Heading", block_to_block_type(text))

    def test_ordered_list(self):
        text = "1. test\n2. test\n3. test"
        self.assertEqual("Ordered List", block_to_block_type(text))
    
    def test_unordered_list(self):
        text = "* test\n* test\n* test"
        self.assertEqual("Unordered List", block_to_block_type(text))

    def test_quote(self):
        text = "> test\n> test\n> test"
        self.assertEqual("Quote", block_to_block_type(text))

    def test_code(self):
        text = "```test\ntest\ntest```"
        self.assertEqual("Code", block_to_block_type(text))

    def test_paragraph(self):
        text = "This is just a plain old paragraph"
        self.assertEqual("Paragraph", block_to_block_type(text));

    # Testing for markdown_to_html_node function
    def test_html_out(self):
        text = """# Header

Paragraph

- List item
- List item

[link](link.com)

![image](image.com)

*italics*

**bold**
"""
        test = ParentNode("div", [ParentNode("h1", [LeafNode(None, "Header")]),
                                        ParentNode("p", [LeafNode(None, "Paragraph")]),
                                        ParentNode("ul", [ParentNode("li", [LeafNode(None, "List item")]),
                                                                ParentNode("li", [LeafNode(None, "List item")])]),
                                                                ParentNode("p", [LeafNode("a", "link",  {"href":"link.com"})]),
                                                                ParentNode("p", [LeafNode("img", "", {"src":"image.com", "alt":"image"})]),
                                                                ParentNode("p", [LeafNode("i", "italics")]), ParentNode("p", [LeafNode("b", "bold")])])
        self.assertEqual(markdown_to_html_node(text), test)

    def test_children_text(self):
        text = """This is a paragraph with *italics* and **Bold**"""
        test = ParentNode("div", [ParentNode("p", [LeafNode(None, "This is a paragraph with "),
                                LeafNode("i", "italics"),
                                LeafNode(None, " and "),
                                LeafNode("b", "Bold")])])
        self.assertEqual(test, markdown_to_html_node(text))

if __name__ == "__main__":
    unittest.main()