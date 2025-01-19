import os
from pathlib import Path


def generate_context(directory, output_file="file_context.txt"):
    # Generate file tree
    def build_file_tree(dir_path, prefix=""):
        lines = []
        for item in sorted(os.listdir(dir_path)):
            item_path = os.path.join(dir_path, item)
            if os.path.isdir(item_path):
                lines.append(f"{prefix}├── {item}")
                lines.extend(build_file_tree(item_path, prefix + "│   "))
            else:
                lines.append(f"{prefix}├── {item}")
        return lines

    # Collect file contents
    def collect_file_contents(dir_path):
        content_lines = []
        for root, _, files in os.walk(dir_path):
            for file in sorted(files):
                file_path = os.path.join(root, file)
                try:
                    file_content = Path(file_path).read_text(errors="ignore")
                    content_lines.append(f"\n--- Start of {file_path} ---\n")
                    content_lines.append(file_content)
                    content_lines.append(f"\n--- End of {file_path} ---\n")
                except Exception as e:
                    content_lines.append(f"\n--- Start of {file_path} ---\n")
                    content_lines.append(f"Error reading file: {e}")
                    content_lines.append(f"\n--- End of {file_path} ---\n")
        return content_lines

    # Build file tree and file contents
    file_tree = build_file_tree(directory)
    file_contents = collect_file_contents(directory)

    # Write everything to the output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("File Tree:\n")
        f.write("\n".join(file_tree))
        f.write("\n\nFiles:\n")
        f.writelines(file_contents)

    print(f"Context successfully generated in {output_file}")


# Replace 'path_to_your_directory' with the root directory path you want to scan
generate_context("path_to_your_directory")