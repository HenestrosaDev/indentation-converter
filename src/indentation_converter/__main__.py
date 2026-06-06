import argparse
import os
import sys
from typing import Callable, List

from .core import (
	convert_leading_spaces_to_tabs,
	convert_leading_tabs_to_spaces,
	is_hidden,
	process_directory,
	process_file,
)


def main() -> int:
	"""
	Main function to handle argument parsing and conversion processing.
	"""
	parser = argparse.ArgumentParser(
		description="Convert leading whitespace and tabs in files."
	)
	parser.add_argument("path", help="File or directory path to process")
	parser.add_argument(
		"-m",
		"--mode",
		choices=["spaces-to-tabs", "st", "tabs-to-spaces", "ts"],
		help="Conversion mode. `st` is the short form of `spaces-to-tabs` and `ts` is "
		"the short form of `tabs-to-spaces`",
	)
	parser.add_argument(
		"-s",
		"--spaces-per-tab",
		type=int,
		default=4,
		help="Number of spaces per tab. The default value is 4.",
	)
	parser.add_argument(
		"-r",
		"--remove-whitespace-only-lines",
		action="store_true",
		help="Remove lines that contain only spaces, tabs, or line breaks.",
	)

	args = parser.parse_args()

	# Validate that at least one action is specified
	if not args.mode and not args.remove_whitespace_only_lines:
		parser.error("You must specify either a conversion mode (-m) or the remove whitespace flag (-r).")

	conversion_mode = None

	# Explicitly define the type expected for the conversion function
	conversion_function: Callable[[str, int], str]

	# Determine the conversion function if the -m flag was specified
	if args.mode:
		conversion_mode_map = {
			"spaces-to-tabs": "st",
			"tabs-to-spaces": "ts",
		}
		conversion_mode = conversion_mode_map.get(args.mode, args.mode)

		if conversion_mode == "st":
			conversion_function = convert_leading_spaces_to_tabs
		elif conversion_mode == "ts":
			conversion_function = convert_leading_tabs_to_spaces
		else:
			print("Invalid mode specified.", file=sys.stderr)
			return 1
	else:
		conversion_function = lambda line, spaces: line

	if os.path.isdir(args.path):
		process_directory(
			args.path,
			conversion_function,
			args.spaces_per_tab,
			args.remove_whitespace_only_lines,
		)
	elif os.path.isfile(args.path) and not is_hidden(args.path):
		process_file(
			args.path,
			conversion_function,
			args.spaces_per_tab,
			args.remove_whitespace_only_lines,
		)
	else:
		print(f"The path '{args.path}' is not valid or is hidden.", file=sys.stderr)
		return 1

	# Success message with details of the actions performed
	actions: List[str] = []
	if conversion_mode == "st":
		actions.append("leading spaces converted to tabs")
	elif conversion_mode == "ts":
		actions.append("leading tabs converted to spaces")

	if args.remove_whitespace_only_lines:
		actions.append("whitespace-only lines removed")

	print(f"Success! Actions performed on '{args.path}': {', '.join(actions)}.")
	return 0


if __name__ == "__main__":
	sys.exit(main())