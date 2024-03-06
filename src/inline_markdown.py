from textnode import TextNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

text_types: list[str] = ["text", "bold", "italic", "code", "link", "image",]

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: str,) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
#        print(node)
        if not isinstance(node, TextNode):
            new_nodes.append(node)
            continue
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise ValueError(f"Mismatched delimiters in node: {node}")

        for i,w in enumerate(split_text):
            if i % 2 == 0:
                new_nodes.append(TextNode(text=w, text_type="text"))
            else:
                new_nodes.append(TextNode(text=w, text_type=text_type))
    return new_nodes