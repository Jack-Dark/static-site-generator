import os

from pathlib import Path
from markdown_blocks import markdown_to_html_node


def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = ""
    with open(from_path) as f:
        markdown = f.read()

    template = ""
    with open(template_path) as f:
        template = f.read()

    title = extract_title(markdown)
    html_string = markdown_to_html_node(markdown).to_html()

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)

    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template)


def extract_title(markdown: str):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()

    raise ValueError("No H1 heading found. H1 heading is required.")


def generate_pages_recursive(
    dir_path_content: str,
    template_path: str,
    dest_dir_path: str,
):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")

            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)
