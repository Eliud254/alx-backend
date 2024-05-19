#!/usr/bin/env python3
"""
Defines the index_range helper function.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate start and end indices for pagination.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indices.
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return start, end
