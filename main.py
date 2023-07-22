import xml.etree.ElementTree as ET

def get_unique_g_tags(svg_file_path):
    unique_g_tags = []
    tree = ET.parse(svg_file_path)
    root = tree.getroot()
    for element in root.iter():
        if element.tag.endswith('}g'):
            unique_g_tags.append(ET.tostring(element))
    return unique_g_tags

def get_svg_attributes(svg_content):
    start_idx = svg_content.find("<svg")
    end_idx = svg_content.find(">", start_idx) + 1
    return svg_content[start_idx:end_idx] if start_idx != -1 and end_idx != 0 else ''

def extract_style_from_svg(svg_content):
    start_idx = svg_content.find("<style")
    end_idx = svg_content.find("</style>") + len("</style>")
    return svg_content[start_idx:end_idx] if start_idx != -1 and end_idx != -1 else ''

def save_g_tag_to_svg(svg_content, filename, svg_attributes, style_content):
    svg_content_str = svg_content.decode('utf-8').strip()
    svg_content_str = svg_content_str[svg_content_str.find('>') + 1 : svg_content_str.rfind('</svg>')]
    new_svg_content = f"""<?xml version='1.0' encoding='utf-8'?>
 {svg_attributes}
{style_content}<ns0:g>
{svg_content_str}>
</ns0:svg>"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_svg_content)

if __name__ == "__main__":
    svg_file_path = input("Enter the path to the SVG file: ")
    unique_g_tags = get_unique_g_tags(svg_file_path)
    print(f"Found {len(unique_g_tags)} unique <g> tags in the SVG file.")
    with open(svg_file_path, 'r', encoding='utf-8') as f:
        svg_content = f.read()
    svg_attributes = get_svg_attributes(svg_content)
    style_content = extract_style_from_svg(svg_content)
    while True:
        action = input("Enter 'read <index>' to read a <g> tag or 'save <index>' to export as SVG (or 'q' to quit): ")
        if action.lower() == 'q':
            break
        action_parts = action.split()
        if len(action_parts) != 2:
            print("Invalid input. Please enter a valid action.")
            continue
        index_str = action_parts[1]
        try:
            index = int(index_str)
            if action_parts[0].lower() == 'read':
                if 0 <= index < len(unique_g_tags):
                    print(f"Contents of unique <g> tag at index {index}:")
                    print(unique_g_tags[index].decode('utf-8'))
                else:
                    print("Invalid index. Please enter a valid index.")
            elif action_parts[0].lower() == 'save':
                if 0 <= index < len(unique_g_tags):
                    output_filename = f"g_tag_{index}.svg"
                    save_g_tag_to_svg(unique_g_tags[index], output_filename, svg_attributes, style_content)
                    print(f"Unique <g> tag at index {index} has been saved as '{output_filename}'")
                else:
                    print("Invalid index. Please enter a valid index.")
            else:
                print("Invalid action. Please enter 'read <index>' or 'save <index>'.")
        except ValueError:
            print("Invalid input. Please enter a valid index or 'q' to quit.")
