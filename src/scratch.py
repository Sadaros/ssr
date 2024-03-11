from textnode import TextNode, text_node_to_html_node, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from block_markdown import markdown_to_blocks, block_to_block_type
from inline_markdown import (
    split_nodes_delimiter,
    split_nodes_image,
    extract_markdown_images,
    extract_markdown_links,
    text_to_textnodes
)


class ExampleNodes:
    text_node = TextNode("Hi mom", TextType.text, )
    text_node2 = TextNode("Hello World", TextType.text)
    bold_node = TextNode("This is a **bold** word", TextType.text)
    bold_node2 = TextNode("Another **bold** word, and **another**", TextType.text)
    formatted_bold_node = TextNode("bold text", TextType.bold)
    image_node = TextNode("This is text with an ![image](https://upload.wikimedia.org/wikipedia/commons/3/3f/JPEG_example_flower.jpg)", TextType.text)
    image_node2 = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.text)

def main():
    text = """# A header

Paragraph of text, spanning not just one line.
But two.

Another paragraph, but on one line

* List elements
* Unordererd

1. List elements
2. Ordered"""
    
    blocks = markdown_to_blocks(text)
    for block in blocks:
        print(block)
        print(f"scratch: {block_to_block_type(block)}")
        print("---")


main()