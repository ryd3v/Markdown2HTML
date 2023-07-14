import os
import markdown

# Prompt the user for the input directory
input_directory = input("Enter the input directory for Markdown files: ")

# Prompt the user for the output directory
output_directory = input("Enter the output directory for JavaScript files: ")

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Iterate through the Markdown files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".md"):
        # Read the Markdown content
        with open(os.path.join(input_directory, filename), "r") as file:
            markdown_content = file.read()

        # Convert the Markdown to HTML
        html_content = markdown.markdown(markdown_content)

        # Define the JavaScript output file path
        js_output_file = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.js")

        # Write the JavaScript file
        with open(js_output_file, "w") as file:
            file.write(f"export default `{html_content}`;")

print("Conversion complete!")
