# Licensed under the GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# For details: https://github.com/pylint-dev/pylint/blob/main/LICENSE
# Copyright (c) https://github.com/pylint-dev/pylint/blob/main/CONTRIBUTORS.txt

__all__ = [
    "KNOWN_NAME_TYPES_WITH_STYLE",
    "AnyStyle",
    "CamelCaseStyle",
    "NameChecker",
    "NamingStyle",
    "PascalCaseStyle",
    "SnakeCaseStyle",
    "UpperCaseStyle",
]

from pylint.checkers.base.name_checker.checker import NameChecker
from pylint.checkers.base.name_checker.naming_style import (
    KNOWN_NAME_TYPES_WITH_STYLE,
    AnyStyle,
    CamelCaseStyle,
    NamingStyle,
    PascalCaseStyle,
    SnakeCaseStyle,
    UpperCaseStyle,
)
