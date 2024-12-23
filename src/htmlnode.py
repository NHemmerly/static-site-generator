

class HTMLNode():
    def __init__(self, tag=None, children=None, value=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        html_string = ""
        if self.props:
            for prop in self.props:
                html_string += f' {prop}="{self.props[prop]}"'
        return html_string

    def __repr__(self):
        return f"{type(self).__name__}({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"

    def __eq__(self, other):
        tag_equal = self.tag == other.tag
        value_equal = self.value == other.value
        children_equal = self.children == other.children
        props_equal = self.props == other.props
        return (tag_equal and value_equal and children_equal and props_equal)

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if self.tag:
            return f'<{self.tag}{self.props_to_html()}> {self.value} </{self.tag}>'
        else:
            return f'{self.value}'

    def __repr__(self):
        return f"{type(self).__name__}({self.tag}, {self.value}, {self.props_to_html()})"

    def __eq__(self, other):
        tag_equal = self.tag == other.tag
        value_equal = self.value == other.value
        props_equal = self.props == other.props
        return (tag_equal and value_equal and props_equal)

class ParentNode(HTMLNode):
    def __init_(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self, child_output=None):
        print(self)
        if len(self.children) == 0:
            return f'<{self.tag}{self.props_to_html()}> {child_output} </{self.tag}>'
        if not self.tag:
            raise ValueError("All parent nodes must have a tag")
        elif not self.children:
            raise ValueError("All parent nodes must have a child")
        else:
            new_child = self.children.pop(0)
            child_output = self.to_html(child_output)
        return f'<{self.tag}{self.props_to_html()}> {child_output} </{self.tag}>'