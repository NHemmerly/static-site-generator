import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq_empty(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node1, node2)

    def test_eq_attr(self):
        node1 = HTMLNode("a")
        node2 = HTMLNode("a")
        self.assertEqual(node1, node2)

    def test_html_props(self):
        node = HTMLNode("a", None, None, {"href": "test", "target": "test"})
        self.assertEqual(node.props_to_html(), ' href="test" target="test"')

if __name__ == "__main__":
    unittest.main()