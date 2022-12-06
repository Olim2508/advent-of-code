from base import BaseService


class Day7(BaseService):
    def __init__(self, file_path):
        super().__init__(file_path)

    def _prepare_data(self, item: str):
        item = super()._prepare_data(item)
        return item

    def solution(self, letter_group_number=4):
        prepared_data = super().read_input_file(self.file_path)


if __name__ == "__main__":
    day_7 = Day7("/Users/olim/Downloads/input6.txt")
    print("Part 1 --->", day_7.solution())
    # print("Part 2 --->", day_7.solution(letter_group_number=14))
