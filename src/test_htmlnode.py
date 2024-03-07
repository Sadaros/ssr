import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    def test_props_href(self):
        node = HTMLNode(props={
            "href": "https://google.com",
            "target": "_blank",
            })
        self.assertEqual(node.props_to_html(), ' href="https://google.com" target="_blank"')

    def test_props_css(self):
        node = HTMLNode(props={
            "color": "black",
            "min_width": "10px",
        })
        self.assertEqual(node.props_to_html(), ' color="black" min_width="10px"')


class TestLeafNode(unittest.TestCase):
    
    def test_props_to_html(self):
        node = LeafNode(value="Hi mom", tag="p", props={"font-size": "24", "color": "red"})
        self.assertEqual(node.props_to_html(), ' font-size="24" color="red"')

    def test_to_html(self):
        node = LeafNode(value="Hi mom", tag="p")
        self.assertEqual(node.to_html(), "<p>Hi mom</p>")

    def test_to_html_props(self):
        node = LeafNode(value="Heisann", tag="h1", props={"font-size": "24", "color": "red"})
        self.assertEqual(node.to_html(), '<h1 font-size="24" color="red">Heisann</h1>')


class TestParentNode(unittest.TestCase):

    def test_single_item_parent(self):
        node = ParentNode(tag="ul", children=[
            LeafNode(value="Leaf Node Single", tag="li")
        ])
        self.assertEqual(node.to_html(), "<ul><li>Leaf Node Single</li></ul>")

    def test_long_single_list(self):
        node = ParentNode(tag="ul", children=[
            LeafNode(value="Leaf Node 1", tag="li"),
            LeafNode(value="Leaf Node 2", tag="li"),
            LeafNode(value="Leaf Node 3", tag="li"),
        ])
        self.assertEqual(node.to_html(), "<ul><li>Leaf Node 1</li><li>Leaf Node 2</li><li>Leaf Node 3</li></ul>")
        

if __name__ == "__main__":
    unittest.main()