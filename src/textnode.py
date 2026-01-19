from enum import Enum
from htmlnode import HTMLNode, LeafNode


class TextType(Enum):
    TEXT = "text"
    H1 = "heading_1"
    H2 = "heading_2"
    H3 = "heading_3"
    H4 = "heading_4"
    H5 = "heading_5"
    H6 = "heading_6"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.H1:
            return LeafNode("h1", text_node.text)
        case TextType.H2:
            return LeafNode("h2", text_node.text)
        case TextType.H3:
            return LeafNode("h3", text_node.text)
        case TextType.H4:
            return LeafNode("h4", text_node.text)
        case TextType.H5:
            return LeafNode("h5", text_node.text)
        case TextType.H6:
            return LeafNode("h6", text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode(
                "a",
                text_node.text,
                {
                    "href": text_node.url,
                },
            )
        case TextType.IMAGE:
            return LeafNode(
                "img",
                "",
                {
                    "src": text_node.url,
                    "alt": text_node.text,
                },
            )
        case _:
            raise ValueError
