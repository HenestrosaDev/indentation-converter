import os
from collections.abc import Callable
from typing import List

import pathspec

# Public API of this module
__all__ = [
	"convert_leading_spaces_to_tabs",
	"convert_leading_tabs_to_spaces",
	"process_file",
	"process_directory",
]


def convert_leading_spaces_to_tabs(line: str, spaces_per_tab: int) -> str:
	"""Convert leading spaces in a line to tabs."""
	leading_spaces = len(line) - len(line.lstrip(" "))
	tabs = leading_spaces // spaces_per_tab
	remaining_spaces = leading_spaces % spaces_per_tab
	return "\t" * tabs + " " * remaining_spaces + line.lstrip(" ")


def convert_leading_tabs_to_spaces(line: str, spaces_per_tab: int) -> str:
	"""Convert leading tabs in a line to spaces."""
	leading_tabs = len(line) - len(line.lstrip("\t"))
	spaces = " " * spaces_per_tab * leading_tabs
	return spaces + line.lstrip("\t")


def process_file(
	file_path: str,
	conversion_function: Callable[[str, int], str],
	spaces_per_tab: int,
	remove_whitespace_only_lines: bool = False,
) -> None:
	"""Process a single file to convert its leading spaces or tabs."""
	if _is_binary(file_path):
		return

	with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
		lines = file.readlines()

	with open(file_path, "w", encoding="utf-8", errors="ignore") as file:
		for line in lines:
			if remove_whitespace_only_lines and line.strip(" \t\r\n") == "":
				if line.endswith("\r\n"):
					file.write("\r\n")
				elif line.endswith("\n"):
					file.write("\n")
				continue

			file.write(conversion_function(line, spaces_per_tab))


def process_directory(
	directory_path: str,
	conversion_function: Callable[[str, int], str],
	spaces_per_tab: int,
	remove_whitespace_only_lines: bool = False,
) -> None:
	"""Process all files in a directory to convert leading spaces or tabs."""
	ignored_files = _get_ignored_files(directory_path)
	for root, dirs, files in os.walk(directory_path):
		files[:] = [f for f in files if not is_hidden(os.path.join(root, f))]
		dirs[:] = [d for d in dirs if not is_hidden(os.path.join(root, d))]

		for file_name in files:
			file_path = os.path.join(root, file_name)
			if file_path not in ignored_files:
				process_file(
					file_path,
					conversion_function,
					spaces_per_tab,
					remove_whitespace_only_lines,
				)


def is_hidden(filepath: str) -> bool:
	"""Check if a file or directory is hidden."""
	name = os.path.basename(filepath)
	if name.startswith("."):
		return True
	elif os.name == "nt":  # Windows
		return _has_hidden_attribute_on_windows(filepath)
	return False


# ---------------------------------------------------------
# Private helper functions
# ---------------------------------------------------------

def _get_ignored_files(directory_path: str) -> List[str]:
	"""Get a list of files to ignore based on .gitignore patterns."""
	gitignore_path = os.path.join(directory_path, ".gitignore")
	if not os.path.exists(gitignore_path):
		return []

	with open(gitignore_path, "r", encoding="utf-8", errors="ignore") as file:
		gitignore_patterns = file.read().splitlines()

	spec = pathspec.PathSpec.from_lines("gitwildmatch", gitignore_patterns)

	all_files = []
	for root, dirs, files in os.walk(directory_path):
		for name in files:
			all_files.append(os.path.relpath(os.path.join(root, name), directory_path))
		for name in dirs:
			all_files.append(os.path.relpath(os.path.join(root, name), directory_path))

	ignored_files = spec.match_files(all_files)
	return [os.path.join(directory_path, path) for path in ignored_files]


def _has_hidden_attribute_on_windows(filepath: str) -> bool:
	"""Check if a file has the hidden attribute (Windows only)."""
	import ctypes

	INVALID_FILE_ATTRIBUTES = -1
	FILE_ATTRIBUTE_HIDDEN = 2

	attrs: int = ctypes.windll.kernel32.GetFileAttributesW(str(filepath))

	if attrs == INVALID_FILE_ATTRIBUTES:
		return False

	return (attrs & FILE_ATTRIBUTE_HIDDEN) != 0


def _is_binary(file_path: str) -> bool:
	"""Check if a file is binary."""
	with open(file_path, "rb") as file:
		chunk = file.read(8192)

	if not chunk:
		return False

	if b"\x00" in chunk:
		return True

	try:
		chunk.decode("utf-8")
	except UnicodeDecodeError:
		return True

	return False