import os

def get_project_info(root_path, exclude=None, include=None):
    project_structure = {}
    
    for root, dirs, files in os.walk(root_path):
        # Exclude directories like .git by modifying dirs in-place
        dirs[:] = [d for d in dirs if d not in exclude]
        
        for file in files:
            if (exclude and any(excl in file for excl in exclude)) or (include and file not in include):
                continue
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except (UnicodeDecodeError, Exception):
                try:
                    with open(file_path, 'r', encoding='latin-1') as f:  # Fallback encoding
                        content = f.read()
                except Exception as e:
                    content = f"Error reading file: {e}"
            project_structure[file_path] = content
            
    return project_structure

# Function to generate the prompt with the root folder name automatically parsed
def generate_prompt(project_structure, readme_content, user_instruction, root_path):
    # Automatically parse the project name from the root path
    project_name = os.path.basename(root_path)

    project_structure_prompt = ""
    for path in project_structure:
        relative_path = os.path.relpath(path, root_path)
        project_structure_prompt += f"- {project_name}/{relative_path}\n"

    project_content_prompt = ""
    for path, content in project_structure.items():
        relative_path = os.path.relpath(path, root_path)
        project_content_prompt += f"\n#### File: `{project_name}/{relative_path}`\n```\n{content}\n```\n"

    main_prompt = f"""
    **Task**:
        Based on the following project structure and file contents, generate code to help the user build a web application.

    ### 1. README File Content:
    {readme_content}

    ###2. Whole project file path structure:
    {project_structure_prompt}
    
    ###3. Each content of files:
    {project_content_prompt}

    ###4. System Instruction:
        The user wants help to build a web application. Based on the project structure and contents provided, 
        generate appropriate code and explanations to guide them in the process. Focus on the following requirements:
            - Analyze the provided file structure and suggest improvements or additions if necessary.
            - If there are any missing components for building a web app (e.g., templates, routes, server setup), suggest appropriate steps or provide the necessary code.
            - Provide clear and modular code snippets, with explanations, where applicable.
            - Ensure the project structure follows best practices for web applications.
            - The project should be ready to run locally on the user's machine.

    ### 5. Expected Output:
        The output should include:
            1. An analysis of the current project structure.
            2. Suggested improvements and additional code where needed.
            3. Detailed explanations of how the user can use the provided code to set up the web application.

    ### 6. User's Instruction:
    {user_instruction}
    """
    
    return main_prompt

# Main function to execute
def main(root_path, exclude=None, include=None, user_instruction=None):
    # Read README content if it exists
    readme_path = os.path.join(root_path, 'README.md')
    readme_content = ""
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_content = f.read()
    else:
        readme_content = "README.md not found"
    
    # Ensure result_prompt.txt is excluded from analysis
    if exclude is None:
        exclude = []
    exclude.append("result_prompt.txt")
    
    # Get project structure and contents
    project_structure = get_project_info(root_path, exclude, include)
    
    # Generate prompt
    prompt = generate_prompt(project_structure, readme_content, user_instruction, root_path)
    
    # Save the prompt to a txt file (overwrite mode)
    output_file = os.path.join(root_path, 'result_prompt.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(prompt)
    
    print(f"Prompt saved to {output_file}")

# Example usage:
root_path = r"..\o1 Prompter"
exclude = ["node_modules", ".git", "example.txt", "README.md", ".gitignore"]
include = None  # Include all files if None
user_instruction = "Please help me build a web app based on this structure."

main(root_path, exclude, include, user_instruction)
