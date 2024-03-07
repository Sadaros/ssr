from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    node = ParentNode(tag="p", children=[
        LeafNode(tag="b", value="Bold text"), 
        LeafNode(tag=None, value="Normal text"),
        ParentNode(tag="ul", children=[
            LeafNode(value="Hi mom", tag="a", props={"href": "google.com", "color": "red"}),
            LeafNode(value="Hello World", tag="h1")
        ]),
        LeafNode(tag="i", value="italic text"), 
        LeafNode(tag=None, value="Normal text"),
        LeafNode(value=""),
        
        ])
    #print(node.to_html())

    parent_with_value = ParentNode(children=[LeafNode("hello", "a")], tag="p")
    print(parent_with_value.to_html())

main()