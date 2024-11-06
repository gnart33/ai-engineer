import os
import glob


def aggregate_markdown_files(directory_path):
    # Find all .md files in the directory
    md_files = glob.glob(os.path.join(directory_path, "*.md"))

    # Sort files to ensure consistent ordering
    md_files.sort()

    aggregated_content = []

    # Process each markdown file
    for file_path in md_files:
        # Get filename without extension to use as heading
        filename = os.path.basename(file_path)
        heading = os.path.splitext(filename)[0].split("_")[1]

        # Read file content
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Add heading and content to the list
        aggregated_content.append(f"# {heading}\n\n{content}\n")

    # Join all content with newlines
    return "\n".join(aggregated_content)


def main():
    # Get current directory if no path specified
    directory = os.path.dirname(os.path.abspath(__file__))

    try:
        content = aggregate_markdown_files(directory)

        # Write to output file
        output_path = os.path.join(directory, "aggregated.md")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Successfully aggregated markdown files to {output_path}")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
