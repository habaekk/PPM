# 📜 o1 Prompter

  

**o1 Prompter**는 소프트웨어 개발을 위한 효율적인 **코딩 프롬프트 생성 도구**입니다. 
이 도구는 프로젝트 전체 구조와 파일 내용을 바탕으로, 코드 생성을 도와주는 프롬프트를 자동으로 생성합니다. 
특히 대규모 프로젝트에서 빠르게 파일 구조를 분석하고, 필요한 코드를 명확하게 제시할 수 있습니다.

  

## ✨ 주요 기능

  

-  **프로젝트 구조 자동 분석**: 프로젝트 디렉토리의 전체 파일 구조를 자동으로 분석합니다.

-  **프롬프트 생성**: 파일 구조와 파일 내용을 기반으로 맞춤형 코딩 프롬프트를 생성합니다.

-  **사용자 맞춤 지시사항**: 사용자가 원하는 지시사항을 포함하여 정확한 코드 생성을 지원합니다.

-  **확장성 있는 코드 생성**: 프로젝트의 모든 파일과 내용이 반영된 프롬프트로 다양한 코드를 생성할 수 있습니다.

  

## 🚀 설치 및 사용법

  

### 1. 설치


```bash
git  clone  https://github.com/yourusername/o1-prompter.git

cd  o1-prompter
```


### 2. 실행


`main.py` 파일을 실행하여 프롬프트를 생성할 수 있습니다.

```bash
python main.py
```


### 3. 설정


필요한 파일 및 디렉토리를 무시하고 싶다면, `exclude`리스트에 추가하세요.

```python
exclude = ["node_modules", ".git", "README.md", ".gitignore"]
```

`user_instruction`에 원하는 지시사항을 추가해, 생성되는 프롬프트의 내용을 맞춤 설정할 수 있습니다.

```python
user_instruction = "Please help me build a web app based on this structure."
```


## 🛠️ 사용 예시


```bash
python main.py
```

다음과 같은 프롬프트가 생성됩니다:

```plaintext
**Task**: Based on the following project structure and file contents, generate code to help the user build a software application.

### 1. README File Content:
# o1 Prompter

### 2. Whole project file path structure:
- o1 Prompter/main.py

### 3. Each content of files:
#### File: `o1 Prompter/main.py`
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
이제 이 프롬프트를 사용하는 LLM 모델(ChatGPT)에 입력해주세요.

## 📂 프로젝트 구조


```bash
o1-prompter/
├── main.py					# 프롬프트 생성 메인 스크립트
├── result_prompt.txt		# 생성된 프롬프트 결과물
├── README.md				# 프로젝트 설명 파일
└── .gitignore				# Git 무시 파일
```


## 📋 기여 방법


프로젝트에 기여하고 싶다면 언제든지 [이슈](https://github.com/habaekk/ppm/issues)에 피드백을 남기거나 PR(Pull Request)를 제출해 주세요!

1. 포크(fork) 한 뒤 새로운 브랜치를 만듭니다:
	```bash
	git checkout -b feature/new-feature
	```

2. 변경 사항을 커밋 한 후 브랜치를 푸시합니다:
	```bash
	git push origin feature/new-feature
	```

3. PR을 제출해 주세요.


## 🛡️라이선스


이 프로젝트는 MIT 라이선스 하에 배포됩니다. [LICENSE](./LICENSE) 파일에서 자세한 정보를 확인할 수 있습니다.