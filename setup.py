from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="context-generator",
    version="0.1.0",
    description="Generate file tree and file contents for coding assistance with LLMs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Alastair Grant",
    author_email="aldo.e.george@gmail.com",
    url="https://github.com/aldo-g/context-gen",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "generate-context=context_generator.cli:main",
        ],
    },
    install_requires=[
        # List your package dependencies here, e.g.,
        # "requests>=2.25.1",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",  # Adjust according to your LICENSE
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
    ],
    keywords="context generation file tree LLMs coding assistance",
    project_urls={
        "Bug Reports": "https://github.com/aldo-g/context-gen/issues",
        "Source": "https://github.com/aldo-g/context-gen",
    },
)