import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_image_output(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), 
             ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")],
               extract_markdown_images(text))
        
    def test_link_output(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text), [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])
        # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

    def test_image_link_dif(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_image_link_dif(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertNotEqual(extract_markdown_links(text), [("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

if __name__ == "__main__":
    unittest.main()