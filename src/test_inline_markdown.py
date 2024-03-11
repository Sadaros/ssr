import unittest
from scratch import ExampleNodes
from textnode import (
    TextNode,
    TextType,
)
from inline_markdown import (
    split_nodes_delimiter,
    split_nodes_image,
    extract_markdown_images,
    extract_markdown_links
)

class TestSplitNodes(unittest.TestCase):
    
    def test_code_node(self):
        node = TextNode("This is text with a `code block` word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "`", TextType.code)
        self.assertEqual(new_nodes, [
            TextNode(text="This is text with a ", text_type=TextType.text),
            TextNode(text="code block", text_type=TextType.code),
            TextNode(text=" word", text_type=TextType.text)])
        
    def test_bold_node(self):
        node = TextNode("This is text with a **bold** word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.text),
            TextNode("bold", TextType.bold),
            TextNode(" word", TextType.text)
        ])

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("bolded", TextType.bold),
                TextNode(" word", TextType.text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.text
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("bolded", TextType.bold),
                TextNode(" word and ", TextType.text),
                TextNode("another", TextType.bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another** word after", TextType.text
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("bolded word", TextType.bold),
                TextNode(" and ", TextType.text),
                TextNode("another", TextType.bold),
                TextNode(" word after", TextType.text)
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "*", TextType.italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.text),
                TextNode("italic", TextType.italic),
                TextNode(" word", TextType.text),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "`", TextType.code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.text),
                TextNode("code block", TextType.code),
                TextNode(" word", TextType.text),
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


class TestSplitImageNode(unittest.TestCase):

    def test_split_one_image(self):
        node = TextNode("This is text with an ![image](https://upload.wikimedia.org/wikipedia/commons/3/3f/JPEG_example_flower.jpg)", TextType.text)
        split_nodes = split_nodes_image([node])
        self.assertEqual(
            split_nodes, 
            [
                TextNode("This is text with an ", TextType.text), 
                TextNode("image", TextType.image, "https://upload.wikimedia.org/wikipedia/commons/3/3f/JPEG_example_flower.jpg")
            ]
        )

    def test_split_two_images(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.text)
        split_nodes = split_nodes_image([node])
        self.assertEqual(
            split_nodes,
            [
                TextNode("This is text with an ", TextType.text),
                TextNode("image", TextType.image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.text),
                TextNode("second image", TextType.image, "https://i.imgur.com/3elNhQu.png")
            ]
        )
    
    def test_split_list_images(self):
        node = [ExampleNodes.image_node, ExampleNodes.image_node2]
        split_nodes = split_nodes_image(node)
        self.assertEqual(
            split_nodes,
            [
                TextNode("This is text with an ", TextType.text), 
                TextNode("image", TextType.image, "https://upload.wikimedia.org/wikipedia/commons/3/3f/JPEG_example_flower.jpg"),
                TextNode("This is text with an ", TextType.text),
                TextNode("image", TextType.image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.text),
                TextNode("second image", TextType.image, "https://i.imgur.com/3elNhQu.png")
            ]
        )


if __name__ == "__main__":
    unittest.main()