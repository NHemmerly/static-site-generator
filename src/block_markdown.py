

def markdown_to_blocks(markdown):
    out_list = markdown.split("\n")
    new_list = []
    running = ""
    for line in out_list:
        line = line.strip()
        if line:
            running += line + "\n"
        else:
            new_list.append(running)
            running = ""
    new_list.append(running)
    return new_list
