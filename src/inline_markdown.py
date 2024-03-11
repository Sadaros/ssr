from textnode import TextNode, TextType
import re

text_types: list[str] = ["text", "bold", "italic", "code", "link", "image",]

def text_to_textnodes(text: str) -> list[TextNode]:
    input_text = [TextNode(text, TextType.text)]
    new_nodes = split_nodes_delimiter(input_text, "**", TextType.bold)
    new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.italic)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.code)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_links(new_nodes)
    

    return new_nodes


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
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text == "":
            continue
        working_nodes = []
        image_tup = extract_markdown_images(node.text)
        if not image_tup:
            new_nodes.append(node)
            continue
        for image in image_tup:
            extracted_text = node.text.split(f"![{image[0]}]({image[1]})", 1)
            node.text = extracted_text[1]
            working_nodes.append(TextNode(extracted_text[0], TextType.text))
            working_nodes.append(TextNode(image[0], TextType.image, image[1]))
        if node.text != "":
            working_nodes.append(TextNode(node.text, TextType.text))
        new_nodes.extend(working_nodes)
    return new_nodes

def split_nodes_links(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text == "":
            continue
        working_nodes = []
        link_tup = extract_markdown_links(node.text)
        if not link_tup:
            new_nodes.append(node)
            continue
        for link in link_tup:
            extracted_text = node.text.split(f"[{link[0]}]({link[1]})", 1)
            node.text = extracted_text[1]
            working_nodes.append(TextNode(extracted_text[0], TextType.text))
            working_nodes.append(TextNode(link[0], TextType.link, link[1]))
        if node.text != "":
            working_nodes.append(TextNode(node.text, TextType.text))
        new_nodes.extend(working_nodes)
    return new_nodes



def extract_markdown_images(text: str) -> list[tuple]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text: str) -> list[tuple]:
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)