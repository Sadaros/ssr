import unittest

from textnode import (
    TextNode,
    TextType
)


class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("""Line one
                        Multipline Text
                        with more lines""", TextType.text, )
        node2 = TextNode("""Line one
                        Multipline Text
                        with more lines""", TextType.text, )
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("Something", TextType.bold, "example.com")
        node2 = TextNode("Else", TextType.bold, "example.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("Same text", TextType.bold, None)
        node2 = TextNode("Same text", TextType.italic, None)
        self.assertNotEqual(node, node2)

    def test_str(self):
        node = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertEqual(str(node), str(node2))

if __name__ == "__main__":
    unittest.main()