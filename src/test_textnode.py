import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_bold_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_link_eq(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        node2 = TextNode("This is a bold node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_link_not_eq(self):
        node = TextNode("This is a link node", TextType.LINK)
        node2 = TextNode(
            "This is a link node", TextType.LINK, "https://www.example.com/"
        )
        self.assertNotEqual(node, node2)

    def test_nodes_not_eq(self):
        node = TextNode(
            "This is an image node", TextType.IMAGE, "https://www.example.com/file.jpg"
        )
        node2 = TextNode(
            "This is a link node", TextType.LINK, "https://www.example.com/"
        )
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
