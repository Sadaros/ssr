import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    text_types
)
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links
)

class TestSplitNodes(unittest.TestCase):
    
    def test_code_node(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(new_nodes, [
            TextNode(text="This is text with a ", text_type=text_type_text),
            TextNode(text="code block", text_type=text_type_code),
            TextNode(text=" word", text_type=text_type_text)])
        
    def test_bold_node(self):
        node = TextNode("This is text with a **bold** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" word", text_type_text)
        ])

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another** word after", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
                TextNode(" word after", text_type_text)
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )


class TestExtractImage(unittest.TestCase):

    def test_multiple_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        extracted_text = extract_markdown_images(text)
        self.assertEqual(extracted_text, [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")])

    def test_image_and_link(self):
        text = "This is text with ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://imgur.com/zjjcJKZ)"
        extracted_text = extract_markdown_images(text)
        self.assertEqual(extracted_text, [("image", "https://i.imgur.com/zjjcJKZ.png")])
    
    def test_extract_link_with_image(self):
        text = "This is text with a [link](google.com) and [another link](firefox.com)"
        extracted_text = extract_markdown_images(text)
        self.assertEqual(extracted_text, [])


class TestExtractLinks(unittest.TestCase):

    def test_single_link(self):
        text = "This is text with a [link](google.com)"
        extracted_text = extract_markdown_links(text)
        self.assertEqual(extracted_text, [("link", "google.com")])

    def test_multiple_links(self):
        text = "This is text with a [link](google.com) and [another link](python.org)"
        extracted_text = extract_markdown_links(text)
        self.assertEqual(extracted_text, [("link", "google.com"), ("another link", "python.org")])


if __name__ == "__main__":
    unittest.main()