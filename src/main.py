from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_blocks import markdown_to_blocks


def main():
    # text_node = TextNode(
    #     "This is some anchor text", TextType.LINK, "https://www.boot.dev"
    # )
    # print(text_node)

    # html_node = HTMLNode(
    #     "b",
    #     "This is some bold text",
    # )
    # print(html_node)

    # leaf_node = LeafNode(
    #     "b",
    #     "This is some bold text",
    # )
    # print(leaf_node)

    # parent_node = ParentNode(
    #     "p",
    #     [
    #         LeafNode("b", "Bold text"),
    #         LeafNode(None, "Normal text"),
    #         LeafNode("i", "italic text"),
    #         LeafNode(None, "Normal text"),
    #     ],
    # )

    # print(parent_node)

    print("=======================")
    result = markdown_to_blocks(
        "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and _italic_ words inside of it.\n\n- This is the first list item in a list block\n- This is a list item\n- This is another list item"
    )
    print("=======================")

    print("markdown_to_blocks output:", result)


if __name__ == "__main__":
    main()
