# Copyright (c) 2024 indentation-converter contributors
# @license: http://www.opensource.org/licenses/mit-license.php

from .core import (
	convert_leading_spaces_to_tabs,
	convert_leading_tabs_to_spaces,
	process_lines,
	process_directory,
	process_file,
)

__all__ = [
	"convert_leading_spaces_to_tabs",
	"convert_leading_tabs_to_spaces",
	"process_lines",
	"process_file",
	"process_directory",
]

__version__ = "0.2.0"
__author__ = "José Carlos López Henestrosa"
__license = "MIT"
__author_email__ = "git@henestrosa.dev"
__maintainer_email__ = "git@henestrosa.dev"
