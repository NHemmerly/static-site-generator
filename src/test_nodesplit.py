import unittest

from textnode import TextNode, TextType
from node_split import node_delimiter_split



class TestNodeSplit(unittest.TestCase):
    def test_middle(self):
        nodes = [TextNode("This is text with a `code block` word", TextType.TEXT)]
        new_nodes = node_delimiter_split(nodes, '`', TextType.CODE)
        self.assertEqual(new_nodes, 
                        [
                            TextNode("This is text with a ", TextType.TEXT),
                            TextNode("code block", TextType.CODE),
                            TextNode(" word", TextType.TEXT),
                        ])
    
    def test_end(self):
        nodes = [TextNode("This is text with a code block `word`", TextType.TEXT)]
        new_nodes = node_delimiter_split(nodes, '`', TextType.CODE)
        self.assertEqual(new_nodes, 
                    [
                        TextNode("This is text with a code block ", TextType.TEXT),
                        TextNode("word", TextType.CODE),
                    ])
        
    def test_beginning(self):
        nodes = [TextNode("`This` is text with a code block word", TextType.TEXT)]
        new_nodes = node_delimiter_split(nodes, '`', TextType.CODE)
        self.assertEqual(new_nodes, 
                    [
                        TextNode("This", TextType.CODE),
                        TextNode(" is text with a code block word", TextType.TEXT),
                    ])
        
    def test_unclosed(self):
        nodes = [TextNode("This `is text with a code block word", TextType.TEXT)]
        with self.assertRaises(Exception) as e:
            node_delimiter_split(nodes, '`', TextType.CODE)

    def test_multi_node(self):
        nodes = [
            TextNode("This is the `first` block", TextType.TEXT),
            TextNode("This is the `second` block", TextType.TEXT),
            TextNode("This is a text block", TextType.TEXT),
            TextNode("This is a bold block", TextType.BOLD)
            ]
        node_output = [
            TextNode("This is the ", TextType.TEXT),
            TextNode("first", TextType.CODE),
            TextNode(" block", TextType.TEXT),
            TextNode("This is the ", TextType.TEXT),
            TextNode("second", TextType.CODE),
            TextNode(" block", TextType.TEXT),
            TextNode("This is a text block", TextType.TEXT),
            TextNode("This is a bold block", TextType.BOLD)
        ]    
        self.assertEqual(node_delimiter_split(nodes, "`", TextType.CODE), node_output)





if __name__ == "__main__":
    unittest.main()