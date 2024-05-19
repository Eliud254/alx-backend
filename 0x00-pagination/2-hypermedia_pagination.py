#!/usr/bin/env python3
"""
Class container with methods to create simple pagination from csv data.
"""
import csv
from typing import List, Dict, Tuple
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class for paginating a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Reads from CSV file and returns the dataset.

        Returns:
            List[List]: The dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def assert_positive_integer_type(value: int) -> None:
        """
        Asserts the value is a positive integer.

        Args:
            value (int): Value to be asserted.
        """
        assert isinstance(value, int) and value > 0

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset.

        Args:
            page (int): Page number.
            page_size (int): Page size.

        Returns:
            List[List]: Page of the dataset.
        """
        self.assert_positive_integer_type(page)
        self.assert_positive_integer_type(page_size)
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a page of the dataset with additional metadata.

        Args:
            page (int): Page number.
            page_size (int): The page size.

        Returns:
            Dict: Page of the dataset with metadata.
        """
        total_pages = math.ceil(len(self.dataset()) / page_size)
        data = self.get_page(page, page_size)
        return {
            "page": page,
            "page_size": len(data),
            "total_pages": total_pages,
            "data": data,
            "prev_page": page - 1 if page > 1 else None,
            "next_page": page + 1 if page < total_pages else None
        }
