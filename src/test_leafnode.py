import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode(None, "This is a test")
        node2 = LeafNode(None, "This is a test")
        self.assertEqual(node1, node2)

    def test_repr(self):
        node = LeafNode("a", "This is a test", {"test": "test"})
        self.assertEqual(node.__repr__(), 'LeafNode(a, This is a test,  test="test")')

    def test_value_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError) as context:
            node.to_html()

    def test_raw_text(self):
        node = LeafNode(None, "This is raw text.")
        self.assertEqual(node.to_html(), "This is raw text.")

    def test_html_render(self):
        node = LeafNode("a", "Test html", {"href": "test.com"})
        self.assertEqual(node.to_html(), '<a href="test.com"> Test html </a>')


if __name__ == "__main__":
    unittest.main()