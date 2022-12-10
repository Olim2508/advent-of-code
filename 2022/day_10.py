from typing import List

from base import BaseService
from test_data import test_day_9_data, day_10_test_data


class Day10(BaseService):
    def __init__(self, file_path):
        super().__init__(file_path)

    def _prepare_data(self, item: str):
        item = super()._prepare_data(item)
        item = item.split(" ")
        return item

    def part_1(self):
        prepared_data = super().read_input_file(self.file_path)
        test_data = list(map(self._prepare_data, day_10_test_data))
        data = prepared_data

        cycle_list = [20, 60, 100, 140, 180, 220]
        calculated_cycle_values = []
        cycle_num = 0
        register_value = 1
        for r in data:
            if len(r) == 2:
                for _ in range(2):
                    cycle_num += 1
                    if cycle_num in cycle_list:
                        calculated_cycle_values.append(cycle_num * register_value)
                register_value += int(r[1])
            else:
                cycle_num += 1
                if cycle_num in cycle_list:
                    calculated_cycle_values.append(cycle_num * register_value)
        return sum(calculated_cycle_values)


    def part_2(self):
        prepared_data = super().read_input_file(self.file_path)
        test_data = list(map(self._prepare_data, day_10_test_data))
        data = test_data
        print(data)


if __name__ == "__main__":
    day_10 = Day10("/Users/olim/Downloads/input10.txt")
    # print("Part 1 --->", day_10.part_1())
    print("Part 2 --->", day_10.part_2())
