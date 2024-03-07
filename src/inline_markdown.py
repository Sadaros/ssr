from textnode import TextNode, TextType
import re

text_types: list[str] = ["text", "bold", "italic", "code", "link", "image",]

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: str,) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.text:
            new_nodes.append(node)
            continue

        split_text = node.text.split(delimiter)
        split_nodes = []
        if len(split_text) % 2 == 0:
            raise ValueError(f"Mismatched delimiters in node: {node}")

        for i,w in enumerate(split_text):
            if w == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(text=w, text_type=TextType.text))
            else:
                split_nodes.append(TextNode(text=w, text_type=text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text == "":
            continue
        image_tup = extract_markdown_images(node.text)
        if len(image_tup) > 1:
            raise Exception(f"image list too long: {image_tup}")
        if not image_tup:
            new_nodes.append(node)
            continue
        
        split_text = node.text.split(f"![{image_tup[0][0]}]({image_tup[0][1]})", 1)
        print(split_text)



def extract_markdown_images(text: str) -> list[tuple]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text: str) -> list[tuple]:
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)