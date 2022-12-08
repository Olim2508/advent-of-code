from base import BaseService
from test_data import test_day_7_data


class Day8(BaseService):
    def __init__(self, file_path):
        super().__init__(file_path)

    def _prepare_data(self, item: str):
        item = super()._prepare_data(item)
        return item

    def part_1(self):
        prepared_data = super().read_input_file(self.file_path)


if __name__ == "__main__":
    day_8 = Day8("/Users/olim/Downloads/input8.txt")
    print("Part 1 --->", day_8.part_1())
    # print("Part 2 --->", day_7.solution(letter_group_number=14))
