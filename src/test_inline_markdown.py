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
    split_nodes_delimiter
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





if __name__ == "__main__":
    unittest.main()