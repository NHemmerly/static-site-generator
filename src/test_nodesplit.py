import unittest

from textnode import TextNode, TextType
from node_split import node_delimiter_split, split_nodes_link, split_nodes_image, text_to_textnodes



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


    def test_image_split(self):
        nodes = [
        TextNode(
        "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
        )
        ]
        new_nodes = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(split_nodes_image(nodes), new_nodes)

    def test_link_split(self):
        nodes = [
        TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
        )
        ]
        new_nodes = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(split_nodes_link(nodes), new_nodes)

    def test_text_to_node(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        test = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(test, text_to_textnodes(text))


if __name__ == "__main__":
    unittest.main()