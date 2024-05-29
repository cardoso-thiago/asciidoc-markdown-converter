import re
import sys
import os

def convert_asciidoc_to_markdown(asciidoc_content):
    # Titles
    markdown_content = re.sub(r'^== (.*)', r'## \1', asciidoc_content, flags=re.MULTILINE)
    markdown_content = re.sub(r'^= (.*)', r'# \1', markdown_content, flags=re.MULTILINE)
    # Lists
    markdown_content = re.sub(r'^\* (.*)', r'- \1', markdown_content, flags=re.MULTILINE)
    # Links
    markdown_content = re.sub(r'link:(.*?)\[(.*?)\]', r'[\2](\1)', markdown_content)
    # Code snippets
    markdown_content = re.sub(r'\[source,([a-zA-Z0-9]+)\]\n----\n(.*?)\n----', r'```\1\n\2\n```', markdown_content, flags=re.DOTALL)
    # Images
    markdown_content = re.sub(r'image::(.*?)\[(.*?)\]', r'![\2](\1)', markdown_content)
    return markdown_content

def main(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        asciidoc_content = file.read()

    markdown_content = convert_asciidoc_to_markdown(asciidoc_content)
    output_file = os.path.splitext(input_file)[0] + '.md'
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(markdown_content)

    print(f'Converted file: {output_file}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python converter.py <path_adoc_file.adoc>')
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)