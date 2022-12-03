import string

from base import BaseService


class Day4(BaseService):
    def __init__(self, file_path):
        super().__init__(file_path)

    def _prepare_data(self, item: str):
        item = super()._prepare_data(item)
        return item

    def part_1(self):
        prepared_data = super().read_input_file(self.file_path)

    def part_2(self):
        prepared_data = super().read_input_file(self.file_path)


day_4 = Day4('/Users/olim/Downloads/input4.txt')
