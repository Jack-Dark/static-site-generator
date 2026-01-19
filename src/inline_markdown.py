import re

from enum import Enum
from textnode import TextNode, TextType


class DelimiterType(Enum):
    BOLD = "**"
    ITALIC = "_"
    CODE = "`"


def text_to_textnodes(text):
    nodes: list[TextNode] = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, DelimiterType.BOLD, TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, DelimiterType.ITALIC, TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, DelimiterType.CODE, TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: DelimiterType, text_type: TextType
):
    new_nodes: list[TextNode] = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes: list[TextNode] = []
        sections = old_node.text.split(delimiter.value)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_image(old_nodes: list[TextNode]):
    new_nodes: list[TextNode] = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections: tuple[str, str] = original_text.split(
                f"![{image[0]}]({image[1]})", 1
            )
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]):
    new_nodes: list[TextNode] = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections: tuple[AnchorText, AnchorUrl] = original_text.split(
                f"[{link[0]}]({link[1]})", 1
            )
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


type ImageSrc = str
type AltText = str
type AnchorText = str
type AnchorUrl = str


def extract_markdown_images(text: str) -> tuple[AltText, ImageSrc]:
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text: str) -> tuple[AnchorText, AnchorUrl]:
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
