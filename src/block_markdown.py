from typing import Literal, Union
from enum import Enum
#
#
class BlockType:
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"

#
#
def markdown_to_blocks(markdown: str) -> list[str]:
    new_blocks: list[str] = []
    markdown_blocks = markdown.split("\n\n")
    for block in markdown_blocks:
        if not block:
            continue
        new_blocks.append(block.strip())

    return new_blocks

def block_to_block_type(block: str) -> str:
    lines = block.split("\n")
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.heading
    if block.startswith("```") and block.endswith("```"):
        return BlockType.code
    if block.startswith(">"):
        quote_block = True
        for line in lines:
            if line.startswith(">"):
                continue
            else:
                quote_block = False
                break
        if quote_block:
            return BlockType.quote
    if block.startswith("*") or block.startswith("-"):
        unordered_list = True
        for line in lines:
            if line.startswith("*") or line.startswith("-"):
                continue
            else:
                unordered_list = False
                break
        if unordered_list:
            return BlockType.unordered_list
    if lines[0][0] == "1":
        ordrered_list = True
        list_order = 1
        for line in lines:
            list_num, _ = line.split('.', 1)
            list_num = list_num.strip()
            if list_num.isdigit() and int(list_num) == list_order:
                list_order += 1
                continue
            else:
                ordrered_list = False
        if ordrered_list:
            return BlockType.ordered_list
    
    return BlockType.paragraph