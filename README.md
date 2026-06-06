<div id="top"></div>

<!-- PROJECT LOGO -->
<div align="center">
	<h1>Indentation Converter</h1>
	<p>
		Convert indentation between spaces and tabs in text files and directories, ignoring hidden files, binary files, and files in <code>.gitignore</code>.
	</p>
	<p>
		<a href="https://pypi.org/project/indentation-converter/">
			<img 
				alt="PyPI version" 
				src="https://img.shields.io/pypi/v/indentation-converter" 
			/>
		</a>
		<a href="https://pypi.org/project/indentation-converter/">
			<img 
				alt="Python versions support" 
				src="https://img.shields.io/pypi/pyversions/indentation-converter" 
			/>
		</a>
		<br />
		<a href="https://github.com/HenestrosaDev/indentation-converter/actions/workflows/build.yaml">
			<img 
				alt="GitHub action: Build" 
				src="https://github.com/HenestrosaDev/indentation-converter/actions/workflows/build.yaml/badge.svg" 
			/>
		</a>
		<a href="https://codecov.io/gh/HenestrosaDev/indentation-converter/">
			<img 
				alt="Codecov" 
				src="https://codecov.io/gh/HenestrosaDev/indentation-converter/branch/main/graph/badge.svg" 
			/>
		</a>
		<a href="https://github.com/HenestrosaDev/indentation-converter/blob/main/LICENSE">
			<img 
				alt="License" 
				src="https://img.shields.io/github/license/HenestrosaDev/indentation-converter" 
			/>
		</a>
		<br />
		<a href="https://github.com/HenestrosaDev/indentation-converter/graphs/contributors">
			<img 
				alt="GitHub Contributors" 
				src="https://img.shields.io/github/contributors/HenestrosaDev/indentation-converter" 
			/>
		</a>
		<a href="https://github.com/HenestrosaDev/indentation-converter/issues">
			<img 
				alt="Issues" 
				src="https://img.shields.io/github/issues/HenestrosaDev/indentation-converter" 
			/>
		</a>
		<a href="https://github.com/HenestrosaDev/indentation-converter/pulls">
			<img 
				alt="GitHub pull requests" 
				src="https://img.shields.io/github/issues-pr/HenestrosaDev/indentation-converter" 
			/>
		</a>
	</p>
	<p>
		<a href="https://github.com/HenestrosaDev/indentation-converter/issues/new/choose">
			Report Bug
		</a> 
		· 
		<a href="https://github.com/HenestrosaDev/indentation-converter/issues/new/choose">
			Request Feature
		</a> 
		· 
		<a href="https://github.com/HenestrosaDev/indentation-converter/discussions">
			Ask Question
		</a>
	</p>
</div>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [About the Project](#about-the-project)
	- [Project Structure](#project-structure)
	- [Built With](#built-with)
- [Getting Started](#getting-started)
	- [Prerequisites](#prerequisites)
	- [Script Installation](#script-installation)
	- [Package Installation](#package-installation)
- [Usage](#usage)
	- [Basic Syntax](#basic-syntax)
	- [Options](#options)
	- [Examples](#examples)
	- [Using the Package in Your Project](#using-the-package-in-your-project)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)
- [Support](#support)


<!-- ABOUT THE PROJECT -->

## About the Project

This Python script provides a flexible tool for converting indentation styles in text files between spaces and tabs. It supports converting leading spaces to tabs and leading tabs to spaces, all while ignoring the files detailed in the `.gitignore`, hidden files, and binary files.

In addition to being able to run this script on its own, you can also install it as a package via **PyPI** (more information on how to install it [here](#use-the-package-in-your-project)).

<!-- PROJECT STRUCTURE -->

### Project Structure

<details>
	<summary>ASCII directory structure</summary>

```
/
│   .gitignore
│   .pre-commit-config.yaml
│   LICENSE
│   pyproject.toml
│   README.md
│   requirements-dev.txt
│   requirements.txt
│
├───.github
│   └───workflows
│           build.yaml
│           publish.yaml
│
├───src
│   └───indentation_converter
│           __init__.py
│           __main__.py
│           core.py
│
└───tests
        test_indentation_converter.py
```

</details>

### Built With

- [pathspec](https://github.com/cpburnz/python-pathspec) for `.gitignore` style pattern matching of file paths.
- [binaryornot](https://github.com/binaryornot/binaryornot) to guess whether a file is binary or text.

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

- Python 3.8 or higher (download it [here](https://www.python.org/downloads/))
- Git (download it [here](https://git-scm.com/downloads))

### Script Installation

1. Clone this repository:

	 ```bash
	 git clone https://github.com/HenestrosaDev/indentation-converter.git
	 ```

2. Navigate to the project directory:

	 ```bash
	 cd indentation-converter
	 ```

3. Create and activate a virtual environment:

	 ```bash
	 python -m venv venv

	 # on macOS / Linux
	 source venv/bin/activate

	 # on Windows
	 Set-ExecutionPolicy Unrestricted -Scope Process
	 . venv/Scripts/activate
	 ```

4. Install dependencies:

	 ```bash
	 pip install -r requirements.txt

	 # (optional) install development tools if you are going to work on the code
	 pip install -r requirements-dev.txt
	 ```

4. Install the package locally so the `indentation_converter` CLI is available:

	 ```bash
	 pip install .
	 ```

5. Run the program:

	 ```bash
	 indentation_converter [PATH] -m [MODE] -s [SPACES_PER_TAB]
	 ```

### Package Installation

Install the PyPI package by running:

```bash
pip install indentation-converter
```

To install from source for development:

```bash
pip install -e .
pip install -r dev-requirements.txt
```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE -->

## Usage

### Basic Syntax

```bash
indentation_converter [PATH] -m [MODE] [OPTIONS]
```
>[!NOTE]
>If you haven't installed the tool globally, you can execute it via Python: `python path/to/__main__.py [PATH] ...`

### Options

* `-m` (or `--mode`): Conversion mode. Use `st` or `spaces_to_tabs` to convert to tabs, and `ts` or `tabs_to_spaces` to convert to spaces.
* `-s` (or `--spaces`): Number of spaces per indentation level. **(Default: 4)**
* `-r` (or `--remove-whitespace-only-lines`): Removes trailing spaces/tabs on blank lines, leaving them completely empty.

### Examples

**Convert 4 spaces to tabs (Default)**
Because `-s` defaults to 4, you don't need to specify the space count. This works for both individual files and entire directories:
```bash
indentation_converter [PATH] -m st
```

**Convert 2 spaces to tabs**
```bash
indentation_converter [PATH] -m st -s 2
```

**Convert tabs to 2 spaces**
```bash
indentation_converter [PATH] -m ts -s 2
```

**Convert and clean up empty lines**
Use the `-r` flag to simultaneously strip rogue spaces or tabs from otherwise blank lines:
```bash
indentation_converter [PATH] -r
```

### Using the Package in Your Project

After following the steps in the [Package Installation](#package-installation) section, import the package and use the functions you want:

```python
# Using the `process_file` and `convert_leading_spaces_to_tabs` functions
import indentation_converter as ic

ic.process_file("file.txt", ic.convert_leading_spaces_to_tabs, spaces_per_tab=4)
```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

You can propose a new feature creating an [issue](https://github.com/HenestrosaDev/indentation-converter/new/choose).

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

<!-- LICENSE -->

## License

Distributed under the MIT License. See [`LICENSE`](https://github.com/HenestrosaDev/indentation-converter/blob/main/LICENSE) for more information.

<!-- AUTHORS -->

## Authors

- HenestrosaDev <henestrosadev@gmail.com> (José Carlos López Henestrosa)

See also the list of [contributors](https://github.com/HenestrosaDev/indentation-converter/contributors) who participated in this project.

<!-- SUPPORT -->

## Support

Would you like to support the project? That's very kind of you! You can go to my Ko-Fi profile by clicking on the button down below.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/henestrosadev)

<p align="right">(<a href="#top">back to top</a>)</p>
