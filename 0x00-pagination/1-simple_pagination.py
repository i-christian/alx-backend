#!/usr/bin/env python3
"""
Adds `get_page` method to `Server` class.
"""
import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self._dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self._dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self._dataset = dataset[1:]

        return self._dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """Calculate start & end index range for a `page`, with `page_size`."""
        next_page_start_index = page * page_size
        return next_page_start_index - page_size, next_page_start_index

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get items for the given page number.

        Args:
            page (int): Page number.
            page_size (int): Number of items per page.

        Returns:
            List: A list of rows if inputs are within range,else empty.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start_index, end_index = self.index_range(page, page_size)
        return self.dataset()[start_index:end_index]
