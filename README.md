# 📜 PPM

  

**PPM(Project Prompt Master)** is an efficient **coding prompt generation tool** for software development.
This tool automatically generates prompts to assist with code creation based on the entire project structure and file contents.
It is particularly useful for large projects, allowing for rapid analysis of the file structure and providing clear code suggestions.

  

## ✨ Key Features

  

-  **Automatic Project Structure Analysis**: Automatically analyzes the entire file structure of the project directory.

-  **Prompt Generation**: Generates customized coding prompts based on the file structure and file contents.

-  **User-Specific Instructions**: Supports accurate code generation by including the user's desired instructions.

-  **Scalable Code Generation**: Generates various types of code using prompts that reflect all files and contents of the project.

  

## 🚀 Installation and Usage

  

### 1. Installation


```bash
git  clone  https://github.com/habaekk/ppm.git

cd  ppm
```


### 2. Execution


You can run the `main.py` file to generate the prompt.

```bash
python main.py
```


### 3. Configuration


If you want to exclude specific files and directories, add them to the `exclude` list.

```python
exclude = ["node_modules", ".git", "README.md", ".gitignore"]
```

You can customize the content of the generated prompt by adding your desired instructions to `user_instruction`.

```python
user_instruction = "Please help me build a web app based on this structure."
```


## 🛠️ Usage Example


```bash
python main.py
```

The following prompt will be generated:


```plaintext
**Task**: Based on the following project structure and file contents, generate code to help the user build a software application.

### 1. README File Content:
# ppm

### 2. Whole project file path structure:
- ppm/main.py

### 3. Each content of files:
#### File: `ppm/main.py`
...

### 4. System Instruction:
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
	Please help me build a web app based on this structure.
```
Now, please input this prompt into the LLM model (ChatGPT o1).
## 📂 Project Structure


```bash
ppm/
├── main.py			# Prompt Generation Main Script
├── result_prompt.txt		# Generated Prompt Output
├── README.md				
└── .gitignore				
```


## 📋 How to Contribute

If you would like to contribute to the project, feel free to leave feedback in the [Issues](https://github.com/habaekk/ppm/issues) or submit a PR (Pull Request)!

1. fork and create a new branch:
	```bash
	git checkout -b feature/new-feature
	```

2. After committing your changes, push the branch:
	```bash
	git push origin feature/new-feature
	```

3. Please submit a PR (Pull Request).


## 🛡️ Licence

This project is licensed under the MIT License. For more details, see the [LICENSE](./LICENSE) file.