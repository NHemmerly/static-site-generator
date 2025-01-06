import unittest
from block_markdown import markdown_to_blocks, block_to_block_type

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

if __name__ == "__main__":
    unittest.main()