import os
from block_markdown import markdown_to_html_node, extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = ""
    template = ""
    with open(from_path, "r") as file:
        markdown = file.read()
    with open(template_path, "r") as file:
        template = file.read()
    md_html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", md_html)
    with open(dest_path, "w") as file:
        file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.isdir(dir_path_content):
        if dir_path_content[-3:] == ".md":
            generate_page(dir_path_content, template_path, dest_dir_path)
        return True
    for file in os.listdir(dir_path_content):
        new_file = os.path.join(dir_path_content, file)
        if os.path.isdir(new_file):
            new_dst = os.path.join(dest_dir_path, file)
            os.mkdir(new_dst)
            generate_pages_recursive(new_file, template_path, new_dst)
            continue
        generate_page(new_file, template_path, os.path.join(dest_dir_path, file.replace(".md", ".html")))
    