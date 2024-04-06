#!/usr/bin/env python3
"""Pagination helper function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Simple helper function
    Write a function named index_range that takes
    two integer arguments page and page_size.

    :param page: The number of the page
    :type page: int
    :param page_size: The number of items per page
    :type page_size: int
    :return: A tuple of size two containing a start index and an end index
    :rtype: Tuple[int, int]
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
