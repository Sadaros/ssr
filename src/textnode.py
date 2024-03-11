from htmlnode import HTMLNode, LeafNode, ParentNode

class TextType:
    """All the valid TextNode types"""
    text = "text"
    bold = "bold"
    italic = "italic"
    code = "code"
    link = "link"
    image = "image"

text_types: list[str] = ["text", "bold", "italic", "code", "link", "image",]


class TextNode:

    def __init__(self, text: str, text_type: str, url: str | None = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object) -> bool:
        return (
            self.text == other.text and
            self.text_type == other.text_type and 
            self.url == other.url
        )
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    

def text_node_to_html_node(text_node: TextNode) -> LeafNode | None:
    """Converts TextNode objects to LeafNode objects of the correct type."""
    if text_node.text_type not in text_types:
        raise TypeError(f"{text_node.text_type} is not an allowed text_type")
    
    if text_node.text_type == TextType.text:
        return LeafNode(value=text_node.text)
    if text_node.text_type == TextType.bold:
        return LeafNode(value=text_node.text, tag="b")
    if text_node.text_type == TextType.italic:
        return LeafNode(value=text_node.text, tag="i")
    if text_node.text_type == TextType.code:
        return LeafNode(value=text_node.text, tag="code")
    if text_node.url:
        if text_node.text_type == TextType.link:
            return LeafNode(value=text_node.text, tag="a", props={"href": text_node.url})
        if text_node.text_type == TextType.image:
            return LeafNode(value="", tag="img", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Must provide url to use {text_node.text_type} type element")        