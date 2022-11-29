from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING


def GetAllTokenEntries() -> None:
	'''Gets a list will all available Token entries.'''
def StringConvertTokens(path: str, rpData: Dict[str, object]) -> bool:
	'''Converts tokenized path String to standard String by replacing all Tokens with correct values if found.'''
def FilenameConvertTokens(path: str, rpData: Dict[str, object]) -> bool:
	'''Converts tokenized path Filename into standard Filename by replacing all Tokens with correct values if found.'''
def StringConvertTokensFilter(path: str, rpData: Dict[str, object], exclude: List[object]) -> bool:
	'''Converts tokenized path String to standard String by replacing all Tokens with correct values if found.'''
def FilenameConvertTokensFilter(path: str, rpData: Dict[str, object], exclude: List[str]) -> bool:
	'''Converts tokenized path Filename into standard Filename by replacing all Tokens with correct values if found.'''
def StringExtractRoot(path: str) -> bool:
	'''Searches for the first Token in path. If it is found and it is in-between folder separators, returns the preceding directory path String.'''
def FilenameExtractRoot(path: str) -> bool:
	'''Searches for the first Token in path. If it is found and it is in-between folder separators, returns the preceding directory path Filename.'''
def FilenameSlicePath(path: str) -> Tuple[str, str]:
	'''Splits path in two parts if a Token is found as sub-folders and extracts root and filename path starting at sub-folder.'''

