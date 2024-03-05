import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("""Line one
                        Multipline Text
                        with more lines""", "normal", )
        node2 = TextNode("""Line one
                        Multipline Text
                        with more lines""", "normal", )
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("Something", "bold", "example.com")
        node2 = TextNode("Else", "bold", "example.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("Same text", "bold", None)
        node2 = TextNode("Same text", "itallics", None)
        self.assertNotEqual(node, node2)

    def test_str(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(str(node), str(node2))

if __name__ == "__main__":
    unittest.main()
