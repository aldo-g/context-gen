# Context Generator

![PyPI](https://img.shields.io/pypi/v/context-generator)
![Python Versions](https://img.shields.io/pypi/pyversions/context-generator)
![License](https://img.shields.io/pypi/l/context-generator)
![GitHub Issues](https://img.shields.io/github/issues/yourusername/context-generator)
![GitHub Forks](https://img.shields.io/github/forks/yourusername/context-generator)
![GitHub Stars](https://img.shields.io/github/stars/yourusername/context-generator)
![GitHub License](https://img.shields.io/github/license/yourusername/context-generator)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Generating Context](#generating-context)
  - [Calibrating Configuration](#calibrating-configuration)
- [Configuration](#configuration)
- [Examples](#examples)
- [Integration with VSCode](#integration-with-vscode)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

**Context Generator** is a Python CLI tool designed to generate a comprehensive file tree and collect file contents from your project. This tool is particularly useful for providing context to Large Language Models (LLMs) for coding assistance, documentation generation, or project analysis.

## Features

- **File Tree Generation:** Visual representation of your project's directory structure.
- **Content Collection:** Aggregates contents of selected files for easy reference.
- **Exclusion Options:** Customize which files or directories to exclude from the context.
- **Hidden Files Handling:** Option to include or exclude hidden files and directories.
- **Configuration Management:** Easily configure default settings through a JSON file.
- **VSCode Integration:** Seamlessly integrate with Visual Studio Code via a dedicated extension (planned).
- **Cross-Platform Support:** Works on Windows, macOS, and Linux.

## Installation

### Prerequisites

- **Python 3.7+**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### Install via PyPI

```bash
pip install context-generator