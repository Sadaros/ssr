class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self) -> str:
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self) -> str:
        """Props always start with an empty space."""
        if self.props is None:
            return ""
        html_str = ''
        for prop,value in self.props.items():
            html_str += f' {prop}="{value}"'
        return html_str
    

class LeafNode(HTMLNode):
    def __init__(self, value: str, tag: str = None, children: list = None, props: dict = None) -> None:
        super().__init__(tag=tag, value=value, children=children, props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("all leaf nodes require a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, props: {self.props}"
