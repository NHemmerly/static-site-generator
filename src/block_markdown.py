import re
from functools import reduce

def markdown_to_blocks(markdown):
    out_list = markdown.split("\n\n")
    new_list = []
    for line in out_list:
        if line == "":
            continue
        line = line.strip()
        new_list.append(line)
    return new_list

def block_to_block_type(block):
    lines = block.split("\n")
    ul_pattern = r"^\*\s+.+$|^-\s+.+$"
    heading = r"^#{1,6}\s+.+$"
    code = block[0:2] == "```" and block[-3:] == "```"
    quote = reduce(lambda y, x: x[0] == ">" and y, lines, True)
    unordered_list = all(re.search(ul_pattern, line) for line in lines)
    if re.search(heading, block):
        return "Heading"
    elif code:
        return "Code"
    elif quote:
        return "Quote"
    elif unordered_list:
        return "Unordered List"
    else:
        return "Not Found"
