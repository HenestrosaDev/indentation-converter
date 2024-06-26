<div id="top"></div>

<!-- PROJECT LOGO -->
<div align="center">
	<h1>Indentation Converter</h1>
	<p>
		Convert indentation between spaces and tabs in text files and directories, ignoring hidden files, binary files, and files in <code>.gitiginore</code>.
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
  - [Running the Program](#running-the-program)
    - [Script Flags](#script-flags)
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
│   poetry.lock
│   pyproject.toml
│   README.md
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
│           indentation_converter.py
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

- Python 3.9 or higher (download it [here](https://www.python.org/downloads/))
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

3. Create a Python virtual environment in the project root. If you're using `virtualenv`, you would run `virtualenv venv`.

4. Activate the virtual environment:

	 ```bash
	 # on Windows
	 . venv/Scripts/activate
	 # if you get the error `FullyQualifiedErrorId : UnauthorizedAccess`, run this:
	 Set-ExecutionPolicy Unrestricted -Scope Process
	 # and then . venv/Scripts/activate

	 # on macOS and Linux
	 source venv/Scripts/activate
	 ```

5. Install `poetry`:

	 ```bash
	 pip install poetry
	 ```

6. Use `poetry` to install the project dependencies:

	 ```bash
	 poetry install
	 ```

7. Run the script using `poetry` (see the [Usage](#usage) section for more information):

	 ```bash
	 poetry run indentation_converter <path> -m <mode> -s <spaces-per-tab>
	 ```

### Package Installation

Install the PyPI package by running `pip install indentation-converter`.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE -->

## Usage

### Running the Program

**NOTE**: The commands in each usage example do the same thing. The only thing that changes is the value passed to the conversion mode (`-m`).

---

To convert the indentation of a file from 2 spaces to tabs:

```
python path/to/indentation_converter.py [FILE_PATH] -m st -s 2
python path/to/indentation_converter.py [FILE_PATH] -m spaces_to_tabs -s 2
```

---

To convert the indentation of a file from 4 spaces to tabs:

```
python path/to/indentation_converter.py [FILE_PATH] -m st
python path/to/indentation_converter.py [FILE_PATH] -m spaces_to_tabs 
```

The value of the `-s` flag defaults to 4, so it's not necessary to specify it in this case.

---

To convert the indentation of the files of a directory from 4 spaces to tabs:

```
python path/to/indentation_converter.py [DIRECTORY_PATH] -m st
python path/to/indentation_converter.py [DIRECTORY_PATH] -m spaces_to_tabs
```

---

To convert the indentation of a file from tabs to 2 spaces:

```
python path/to/indentation_converter.py [FILE_PATH] -m ts -s 2
python path/to/indentation_converter.py [FILE_PATH] -m tabs_to_spaces -s 2
```

---

#### Script Flags

| FLAG                       | DESCRIPTION                                                                                                                                                                             |
|:---------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `-h` or `--help`           | Displays help text for the program.                                                                                                                                                     |
| `-m` or `--mode`           | Conversion mode. The possible inputs are `spaces-to-tabs`, `st`, `tabs-to-spaces`, and `ts`. `st` is the short form of `spaces_to_tabs` and `ts` is the short form of `tabs_to_spaces`. |
| `-s` or `--spaces-per-tab` | Number of spaces per tab. The default value is `4`.                                                                                                                                     |

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
