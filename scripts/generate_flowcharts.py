import os
import pyflowchart
import graphviz

PROBLEMS_DIR = "problems"
OUTPUT_DIR = "flowcharts"

def generate_graphviz_flowchart(script_path, output_file):
    """Generates a Graphviz flowchart from a Python script and saves it as PNG."""
    with open(script_path, "r") as f:
        code = f.read()

    fc = pyflowchart.Flowchart.from_code(code)
    dot = graphviz.Source(fc.flowchart())

    # Save as PNG
    dot.render(output_file, format="png", cleanup=False)
    print(f"Saved flowchart: {output_file}.png")

def update_readme(folder, script_name, flowchart_image):
    """Updates the README.md file to include the flowchart image."""
    readme_path = os.path.join(folder, "README.md")

    flowchart_section = f"## Flowchart for `{script_name}`\n\n![Flowchart]({flowchart_image})"

    if os.path.exists(readme_path):
        with open(readme_path, "r") as f:
            content = f.read()

        # Remove old flowchart (if exists) and append the new one
        if "## Flowchart" in content:
            content = content.split("## Flowchart")[0]

        new_content = content.strip() + "\n\n" + flowchart_section
    else:
        new_content = f"# {script_name}\n\n" + flowchart_section

    with open(readme_path, "w") as f:
        f.write(new_content)

    print(f"Updated README: {readme_path}")

def process_all_problems():
    """Processes all Python scripts in the 'problems' directory."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for folder in os.listdir(PROBLEMS_DIR):
        folder_path = os.path.join(PROBLEMS_DIR, folder)
        if os.path.isdir(folder_path):
            for file in os.listdir(folder_path):
                if file.endswith(".py"):
                    script_path = os.path.join(folder_path, file)
                    output_file = os.path.join(OUTPUT_DIR, f"{folder}_flowchart")
                    generate_graphviz_flowchart(script_path, output_file)

                    flowchart_image = f"{OUTPUT_DIR}/{folder}_flowchart.png"
                    update_readme(folder_path, file, flowchart_image)

if __name__ == "__main__":
    process_all_problems()
