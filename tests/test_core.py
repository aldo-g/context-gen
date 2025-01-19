import os
import tempfile

from context_generator.core import (
    build_file_tree,
    collect_file_contents,
    generate_context,
)


def test_build_file_tree():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Setup sample directory structure
        os.makedirs(os.path.join(tmpdir, "dir1", "subdir1"))
        os.makedirs(os.path.join(tmpdir, ".hidden_dir"))
        with open(os.path.join(tmpdir, "file1.txt"), "w") as f:
            f.write("Content of file1")
        with open(os.path.join(tmpdir, ".hidden_file.txt"), "w") as f:
            f.write("Hidden file content")
        with open(os.path.join(tmpdir, "dir1", "file2.txt"), "w") as f:
            f.write("Content of file2")
        with open(
            os.path.join(tmpdir, "dir1", "subdir1", "file3.txt"), "w"
        ) as f:
            f.write("Content of file3")

        # Generate file tree
        file_tree = build_file_tree(
            directory=tmpdir,
            exclude_files=["file1.txt"],
            exclude_paths=["dir1/subdir1"],
            exclude_hidden=True,
        )

        # Since LICENSE may not exist, adjust the assertion
        # Check that excluded files and paths are not present
        assert "file1.txt" not in file_tree
        assert "subdir1" not in file_tree
        assert ".hidden_dir" not in file_tree
        assert ".hidden_file.txt" not in file_tree


def test_collect_file_contents():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Setup sample directory structure
        os.makedirs(os.path.join(tmpdir, "dir1"))
        with open(os.path.join(tmpdir, "file1.txt"), "w") as f:
            f.write("Content of file1")
        with open(os.path.join(tmpdir, "__init__.py"), "w") as f:
            f.write("# Init file")

        # Collect file contents
        contents = collect_file_contents(
            directory=tmpdir,
            exclude_files=["file1.txt"],
            exclude_paths=["dir1"],
            exclude_hidden=True,
        )

        assert "file1.txt" not in "".join(contents)
        assert "dir1" not in "".join(contents)
        assert "__init__.py" in "".join(contents)


def test_generate_context():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Setup sample directory structure
        os.makedirs(os.path.join(tmpdir, "dir1"))
        with open(os.path.join(tmpdir, "file1.txt"), "w") as f:
            f.write("Content of file1")
        with open(os.path.join(tmpdir, "dir1", "file2.txt"), "w") as f:
            f.write("Content of file2")

        output_file = os.path.join(tmpdir, "output.txt")

        # Generate context
        generate_context(
            directory=tmpdir,
            output_file=output_file,
            exclude_files=["file1.txt"],
            exclude_paths=["dir1"],
            exclude_hidden=True,
        )

        # Read output and verify
        with open(output_file, "r") as f:
            content = f.read()

        assert "file1.txt" not in content
        assert "dir1" not in content
        assert "file2.txt" not in content
        assert "output.txt" not in content  # Output file is excluded
        assert "File Tree:" in content
        assert "Files:" in content
