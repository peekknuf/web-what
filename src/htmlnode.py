# htmlnode.py

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def props_to_html(self):
        # Return only the HTML attributes without leading spaces
        return ' '.join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return (f"HTMLNode(tag={self.tag}, value={self.value}, children={len(self.children)}, "
                f"props={self.props})")

    def to_html(self):
        raise NotImplementedError("to_html must be implemented by subclasses")

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag=tag, value=value, children=[], props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value to render.")
        if not self.tag:
            return self.value  # Render as raw text if there's no tag
        else:
            props_html = self.props_to_html()
            # Add a leading space if props_html is non-empty
            return f"<{self.tag}{(' ' + props_html) if props_html else ''}>{self.value}</{self.tag}>"
