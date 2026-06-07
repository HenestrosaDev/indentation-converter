import os
import unittest

from indentation_converter import (
	convert_leading_spaces_to_tabs,
	convert_leading_tabs_to_spaces,
	process_directory,
	process_file,
	process_lines,
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

	# ---------------------------------------------------------
	# Directory Processing Tests
	# ---------------------------------------------------------

	def test_process_directory_converts_target_files(self):
		process_directory(self.test_directory, convert_leading_spaces_to_tabs, 4)
		converted_file_path = os.path.join(self.test_directory, "test_file.py")

		with open(converted_file_path, "r") as f:
			converted_content = f.read()

		expected_python_content = "\tdef test_function():\n\t\tpass\n"
		self.assertEqual(converted_content, expected_python_content)

	def test_process_directory_respects_gitignore(self):
		process_directory(self.test_directory, convert_leading_spaces_to_tabs, 4)
		ignored_file_path = os.path.join(self.test_directory, "ignored_file.txt")

		with open(ignored_file_path, "r") as f:
			original_content = f.read()

		expected_ignored_content = "    This file should be ignored."
		self.assertEqual(original_content, expected_ignored_content)

	# ---------------------------------------------------------
	# File Processing Tests
	# ---------------------------------------------------------

	def test_process_binary_file_remains_unchanged(self):
		binary_file_path = os.path.join(self.test_directory, "sample_binary.png")

		with open(binary_file_path, "wb") as f:
			f.write(b"  \x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01")

		process_file(binary_file_path, convert_leading_spaces_to_tabs, 2)

		with open(binary_file_path, "rb") as f:
			original_content = f.read()

		expected_content = b"  \x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01"
		self.assertEqual(original_content, expected_content)

	def test_process_file_removes_whitespace_only_lines(self):
		# This acts as an integration test for file I/O + whitespace stripping
		file_path = os.path.join(self.test_directory, "whitespace_lines.txt")

		with open(file_path, "w") as file:
			file.write("first line\n   \n\t\nsecond line\n")

		process_file(file_path, convert_leading_spaces_to_tabs, 4, True)

		with open(file_path, "r") as file:
			converted_content = file.read()

		self.assertEqual(converted_content, "first line\n\n\nsecond line\n")

	# ---------------------------------------------------------
	# Process Lines Tests (In-Memory Processing)
	# ---------------------------------------------------------

	def test_process_lines_applies_conversion(self):
		lines = ["    def test():\n", "        pass\n"]
		expected = ["\tdef test():\n", "\t\tpass\n"]

		result = process_lines(lines, convert_leading_spaces_to_tabs, 4)
		self.assertEqual(result, expected)

	def test_process_lines_removes_whitespace_only_lines(self):
		lines = ["first line\n", "   \n", "\t\n", "second line\n"]
		expected = ["first line\n", "\n", "\n", "second line\n"]

		result = process_lines(lines, convert_leading_spaces_to_tabs, 4, remove_whitespace_only_lines=True)
		self.assertEqual(result, expected)

	def test_process_lines_preserves_crlf_when_removing_whitespace(self):
		lines = ["first line\r\n", "   \r\n", "second line\r\n"]
		expected = ["first line\r\n", "\r\n", "second line\r\n"]

		result = process_lines(lines, convert_leading_spaces_to_tabs, 4, remove_whitespace_only_lines=True)
		self.assertEqual(result, expected)

	def test_process_lines_keeps_whitespace_if_flag_is_false(self):
		lines = ["first line\n", "   \n", "second line\n"]
		# When flag is false, the whitespace lines are still passed to the conversion function
		expected = ["first line\n", "   \n", "second line\n"] 

		# 4 spaces to 1 tab -> 3 spaces stay 3 spaces
		result = process_lines(lines, convert_leading_spaces_to_tabs, 4, remove_whitespace_only_lines=False)
		self.assertEqual(result, expected)

	# ---------------------------------------------------------
	# String Conversion: Spaces to Tabs Tests
	# ---------------------------------------------------------

	def test_convert_4_spaces_to_1_tab(self):
		line = "    def test_function():\n"
		expected_result = "\tdef test_function():\n"
		self.assertEqual(convert_leading_spaces_to_tabs(line, 4), expected_result)

	def test_convert_2_spaces_to_1_tab(self):
		line = "  def test_function():\n"
		expected_result = "\tdef test_function():\n"
		self.assertEqual(convert_leading_spaces_to_tabs(line, 2), expected_result)

	def test_convert_spaces_to_tabs_preserves_trailing_space(self):
		line = "   * part of a comment block"
		expected_result = "\t * part of a comment block"
		self.assertEqual(convert_leading_spaces_to_tabs(line, 2), expected_result)

	def test_convert_spaces_to_tabs_ignores_existing_tabs(self):
		line = "\tdef test_function():\n"
		expected_result = "\tdef test_function():\n"
		self.assertEqual(convert_leading_spaces_to_tabs(line, 4), expected_result)

	# ---------------------------------------------------------
	# String Conversion: Tabs to Spaces Tests
	# ---------------------------------------------------------

	def test_convert_1_tab_to_4_spaces(self):
		line = "\tdef test_function():\n"
		expected_result = "    def test_function():\n"
		self.assertEqual(convert_leading_tabs_to_spaces(line, 4), expected_result)

	def test_convert_1_tab_to_2_spaces(self):
		line = "\tdef test_function():\n"
		expected_result = "  def test_function():\n"
		self.assertEqual(convert_leading_tabs_to_spaces(line, 2), expected_result)

	def test_convert_tabs_to_spaces_preserves_trailing_space(self):
		line = "\t * part of a comment block"
		expected_result = "   * part of a comment block"
		self.assertEqual(convert_leading_tabs_to_spaces(line, 2), expected_result)

	def test_convert_tabs_to_spaces_ignores_existing_spaces(self):
		line = "    def test_function():\n"
		expected_result = "    def test_function():\n"
		self.assertEqual(convert_leading_tabs_to_spaces(line, 4), expected_result)


if __name__ == "__main__":
	unittest.main()