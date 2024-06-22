import os
import unittest

from indentation_converter import (
    convert_leading_spaces_to_tabs,
    convert_leading_tabs_to_spaces,
    process_directory,
    process_file,
)


class TestIndentationConverter(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory with test files
        self.test_directory = "tests/test_files"
        os.makedirs(self.test_directory, exist_ok=True)

        # Create a Python file to convert
        with open(os.path.join(self.test_directory, "test_file.py"), "w") as f:
            f.write("    def test_function():\n        pass\n")

        # Create a file to be ignored as per .gitignore
        with open(os.path.join(self.test_directory, "ignored_file.txt"), "w") as f:
            f.write("    This file should be ignored.")

        # Create .gitignore file
        with open(os.path.join(self.test_directory, ".gitignore"), "w") as f:
            f.write("ignored_file.txt\n")

    def tearDown(self):
        # Clean up the temporary directory and files
        for filename in os.listdir(self.test_directory):
            file_path = os.path.join(self.test_directory, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

        os.rmdir(self.test_directory)

    def test_process_directory_with_gitignore(self):
        # Call process_directory function with test directory
        process_directory(self.test_directory, convert_leading_spaces_to_tabs, 4)

        # Check that indentation was converted in the expected file
        converted_file_path = os.path.join(self.test_directory, "test_file.py")
        with open(converted_file_path, "r") as f:
            converted_content = f.read()
        expected_python_content = "\tdef test_function():\n\t\tpass\n"
        self.assertEqual(converted_content, expected_python_content)

        # Check that ignored_file remains unchanged
        ignored_file_path = os.path.join(self.test_directory, "ignored_file.txt")
        with open(ignored_file_path, "r") as f:
            original_content = f.read()
        expected_ignored_content = "    This file should be ignored."
        self.assertEqual(original_content, expected_ignored_content)

    def test_no_indentation_for_binary_files(self):
        # Example binary file path (adjust as per your project structure)
        binary_file_path = "tests/test_files/sample_binary.png"

        # Create a temporary file with binary content
        with open(binary_file_path, "wb") as f:
            f.write(
                b"  \x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01"
            )

        # Call the whitespace converter function on the binary file
        process_file(binary_file_path, "spaces_to_tabs", 2)

        # Assert that the binary file remains unchanged (no indentation)
        with open(binary_file_path, "rb") as f:
            original_content = f.read()

        expected_content = (
            b"  \x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01"
        )
        self.assertEqual(original_content, expected_content)

    def test_convert_leading_spaces_to_tabs(self):
        # Test case 1: Convert 4 spaces to 1 tab
        line = "    def test_function():\n"
        expected_result = "\tdef test_function():\n"
        result = convert_leading_spaces_to_tabs(line, 4)
        self.assertEqual(result, expected_result)

        # Test case 2: Convert 2 spaces to 1 tab
        line = "  def test_function():\n"
        expected_result = "\tdef test_function():\n"
        result = convert_leading_spaces_to_tabs(line, 2)
        self.assertEqual(result, expected_result)

        # Test case 3: Convert 2 spaces to 1 tab and preserve the trailing space.
        # Important for comment blocks.
        line = "   * part of a comment block"
        expected_result = "\t * part of a comment block"
        result = convert_leading_spaces_to_tabs(line, 2)
        self.assertEqual(result, expected_result)

        # Test case 4: No conversion if already using tabs
        line = "\tdef test_function():\n"
        expected_result = "\tdef test_function():\n"
        result = convert_leading_spaces_to_tabs(line, 4)
        self.assertEqual(result, expected_result)

    def test_convert_leading_tabs_to_spaces(self):
        # Test case 1: Convert 1 tab to 4 spaces
        line = "\tdef test_function():\n"
        expected_result = "    def test_function():\n"
        result = convert_leading_tabs_to_spaces(line, 4)
        self.assertEqual(result, expected_result)

        # Test case 2: Convert 1 tab to 2 spaces
        line = "\tdef test_function():\n"
        expected_result = "  def test_function():\n"
        result = convert_leading_tabs_to_spaces(line, 2)
        self.assertEqual(result, expected_result)

        # Test case 3: Convert 1 tab to 2 spaces and preserve the trailing space.
        # Important for comment blocks.
        line = "\t * part of a comment block"
        expected_result = "   * part of a comment block"
        result = convert_leading_tabs_to_spaces(line, 2)
        self.assertEqual(result, expected_result)

        # Test case 4: No conversion if already using spaces
        line = "    def test_function():\n"
        expected_result = "    def test_function():\n"
        result = convert_leading_tabs_to_spaces(line, 4)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
