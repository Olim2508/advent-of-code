from base import BaseService


class Day6(BaseService):
    def __init__(self, file_path):
        super().__init__(file_path)

    def _prepare_data(self, item: str):
        item = super()._prepare_data(item)
        return item

    def part_1(self):
        prepared_data = super().read_input_file(self.file_path)

    def part_2(self):
        prepared_data = super().read_input_file(self.file_path)


if __name__ == "__main__":
    day_6 = Day6("/Users/olim/Downloads/input5.txt")
    print("Part 1 --->", day_6.part_1())
    print("Part 2 --->", day_6.part_2())
