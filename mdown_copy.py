import os
from pathlib import Path


def markdown_copy(source_path,target_path):
    # Define the source and target file paths
    source_file_path = source_path # Replace with the path to your source Markdown file
    target_file_path = target_path  # Replace with the path to your target Markdown file

    # Define the start and end markers for the content you want to copy
    source_start_marker = "<!-- START_MARKER -->"
    source_end_marker = "<!-- END_MARKER -->"
    target_start_marker = "<!-- INSERT_MARKER_START -->"
    target_end_marker = "<!-- INSERT_MARKER_END -->"

    # Read the source Markdown file
    with open(source_file_path, "r", encoding="utf-8") as source_file:
        source_content = source_file.read()

    # Find the indices of the start and end markers in the source content
    start_index = source_content.find(source_start_marker)
    end_index = source_content.find(source_end_marker)

    # Check if both markers were found in the source content
    if start_index != -1 and end_index != -1:
        # Extract the content between the markers
        content_to_copy = source_content[start_index + len(source_start_marker):end_index]

        # Read the target Markdown file
        with open(target_file_path, "r", encoding="utf-8") as target_file:
            target_content = target_file.read()

        # Find the location where you want to insert the copied content in the target content
        target_start_index = target_content.find(target_start_marker)
        target_end_index = target_content.find(target_end_marker)

        # Check if both markers were found in the target content
        if target_start_index != -1 and target_end_index != -1:
            # Insert the copied content into the target content
            updated_content = (
                target_content[:target_start_index + len(target_start_marker)]
                + content_to_copy
                + target_content[target_end_index:]
            )

            # Write the updated content back to the target file
            with open(target_file_path, "w", encoding="utf-8") as target_file:
                target_file.write(updated_content)

            print("Content copied and inserted into the target Markdown.")
        else:
            print("Insert markers not found in the target Markdown.")
    else:
        print("Start or end markers not found in the source Markdown.")

def get_markdown_files(dir_path):
    markdown_files = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

dir_path = os.getcwd()
markdown_files = get_markdown_files(dir_path)
print(markdown_files)
# Print the full paths to all Markdown files.
for markdown_file in markdown_files:
    if 'docs' in markdown_file:
        target_file = markdown_file
    else:
        source_file = markdown_file
    print(source_file,target_file)
    markdown_copy(Path(source_file),Path(target_file))
