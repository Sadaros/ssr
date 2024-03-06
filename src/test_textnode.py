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


class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("""Line one
                        Multipline Text
                        with more lines""", text_type_text, )
        node2 = TextNode("""Line one
                        Multipline Text
                        with more lines""", text_type_text, )
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("Something", text_type_bold, "example.com")
        node2 = TextNode("Else", text_type_bold, "example.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("Same text", text_type_bold, None)
        node2 = TextNode("Same text", text_type_italic, None)
        self.assertNotEqual(node, node2)

    def test_str(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(str(node), str(node2))

if __name__ == "__main__":
    unittest.main()