from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    text_node = TextNode(
        "This is some anchor text", TextType.LINK, "https://www.boot.dev"
    )
    print(text_node)

    html_node = HTMLNode(
        "b",
        "This is some bold text",
    )
    print(html_node)

    leaf_node = LeafNode(
        "b",
        "This is some bold text",
    )
    print(leaf_node)

    parent_node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(parent_node)


if __name__ == "__main__":
    main()
