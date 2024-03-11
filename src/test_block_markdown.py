import unittest
from block_markdown import markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):

    def test_empty_string(self):
        text = ""
        blocks = markdown_to_blocks(text)
        self.assertEqual(blocks, [])

    def test_correct_input(self):
        text = """# A header

Paragraph of text, spanning not just one line.
But two.

Another paragraph, but on one line

* List elements
* Unordererd

1 List elements
2 Ordered"""
        blocks = markdown_to_blocks(text)
        self.assertEqual(blocks,[
            "# A header",
            "Paragraph of text, spanning not just one line.\nBut two.",
            "Another paragraph, but on one line",
            "* List elements\n* Unordererd",
            "1 List elements\n2 Ordered"
        ])
    
    def test_one_block(self):
        text = """One singular block of text
This sucks so much to format manually
Really, I hate it
Writing tests suck, but is important
Fuck"""
        blocks = markdown_to_blocks(text)
        self.assertEqual(blocks, [
            "One singular block of text\nThis sucks so much to format manually\nReally, I hate it\nWriting tests suck, but is important\nFuck"
        ])
    
    def test_multiple_blank_lines(self):
        text = """# A header, unlike anything else.

A strong paragraph
Like a piece of text, only;
a little longer

We can even have multiple graphs

And lists
Actually no, i dont like
LISTS
        
        
        """
        blocks = markdown_to_blocks(text)
        self.assertEqual(blocks, [
            "# A header, unlike anything else.",
            "A strong paragraph\nLike a piece of text, only;\na little longer",
            "We can even have multiple graphs",
            "And lists\nActually no, i dont like\nLISTS"

        ])