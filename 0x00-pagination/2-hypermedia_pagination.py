#!/usr/bin/env python3
"""Hypermedia pagination sample.
"""
import csv
import math
from typing import Dict, List, Tuple


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


class Server:
    """Server Class
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a Server instance.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset

        :return: the dataset
        :rtype: List[List]
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get the page of the dataset

        :param page: page number, defaults to 1
        :type page: int, optional
        :param page_size: page size, defaults to 10
        :type page_size: int, optional
        :return: the page of the dataset
        :rtype: List[List]
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get the hypermedia pagination

        :param page: page number, defaults to 1
        :type page: int, optional
        :param page_size: page size, defaults to 10
        :type page_size: int, optional
        :return: the page of the dataset
        :rtype: Dict
        """
        page_data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_info = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if end < len(self.__dataset) else None,
            'prev_page': page - 1 if start > 0 else None,
            'total_pages': total_pages,
        }
        return page_info
