class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self) -> str:
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"

    def to_html(self):
        """Not implemented on HTMLNode"""
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self) -> str:
        """
        Props always start with an empty space. \n
        Transforms props on Node to HTML compatible string.
        """
        if self.props is None:
            return ""
        html_str = ''
        for prop,value in self.props.items():
            html_str += f' {prop}="{value}"'
        return html_str
    

class LeafNode(HTMLNode):
    def __init__(self, value: str, tag: str = None, props: dict = None) -> None:
        super().__init__(tag=tag, value=value, props=props)
        self.children = []

    def to_html(self) -> str:
        """Transforming a LeafNode to HTML strings."""
        if self.value is None:
            raise ValueError("all leaf nodes require a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode(tag: {self.tag}, value: {self.value}, props: {self.props}"


class ParentNode(HTMLNode):
    
    def __init__(self, children: list, tag: str = None, props: dict = None) -> None:
        super().__init__(tag=tag, children=children, props=props)
    
    def __repr__(self) -> str:
        return f"ParentNode(children: {self.children}, tag: {self.tag}, props: {self.props})"
    
    def to_html(self):
        """Transforming a ParentNode to HTML strings."""
        if self.tag is None:
            raise ValueError("tag must not be None")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        
        html_str = f"<{self.tag}{self.props_to_html()}>"
        for node in self.children:
#            print(f"Parent node loop: {node}")
            html_str += node.to_html()
        html_str += f"</{self.tag}>"
        return html_str