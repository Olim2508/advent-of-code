from typing import List

from base import BaseService
from test_data import test_day_9_data
import math


class Day9(BaseService):
    def __init__(self, file_path):
        super().__init__(file_path)

    def _prepare_data(self, item: str):
        item = super()._prepare_data(item)
        item = item.split(" ")
        item[1] = int(item[1])
        return item

    def _check_in_absence(self, overall_tail_cords: List[list], tail_cord_x: int, tail_cord_y: int):
        current_overall_tail_cords = overall_tail_cords.copy()
        for t in overall_tail_cords:
            if t[0] == tail_cord_x and t[1] == tail_cord_y:
                pass
            else:
                current_overall_tail_cords.append([tail_cord_x, tail_cord_y])
                break
        return current_overall_tail_cords

    def _remove_duplicates(self, cords):
        res_list = []
        for item in cords:
            if item not in res_list:
                res_list.append(item)
        return res_list

    def part_1(self):
        prepared_data = super().read_input_file(self.file_path)
        test_data = list(map(self._prepare_data, test_day_9_data))
        data = prepared_data
        tail_cords, head_cords = [0, 0], [0, 0]
        overall_tail_cords = [[0, 0]]
        for step in data:
            """0 - X
               1 - Y 
            """
            if step[0] == 'R':
                for _ in range(1, step[1] + 1):
                    head_cords[0] += 1
                    if abs(head_cords[0] - tail_cords[0]) > 1:
                        tail_cords[0] += 1
                        tail_cords[1] = head_cords[1]
                        overall_tail_cords = self._check_in_absence(overall_tail_cords, tail_cords[0], tail_cords[1])

            elif step[0] == 'L':
                for _ in range(1, step[1] + 1):
                    head_cords[0] -= 1
                    if abs(head_cords[0] - tail_cords[0]) > 1:
                        tail_cords[0] -= 1
                        tail_cords[1] = head_cords[1]
                        overall_tail_cords = self._check_in_absence(overall_tail_cords, tail_cords[0], tail_cords[1])

            elif step[0] == 'U':
                for _ in range(1, step[1] + 1):
                    head_cords[1] += 1
                    if abs(head_cords[1] - tail_cords[1]) > 1:
                        tail_cords[1] += 1
                        tail_cords[0] = head_cords[0]
                        overall_tail_cords = self._check_in_absence(overall_tail_cords, tail_cords[0], tail_cords[1])
            else:
                for _ in range(1, step[1] + 1):
                    head_cords[1] -= 1
                    if abs(head_cords[1] - tail_cords[1]) > 1:
                        tail_cords[1] -= 1
                        tail_cords[0] = head_cords[0]
                        overall_tail_cords = self._check_in_absence(overall_tail_cords, tail_cords[0], tail_cords[1])

        counted_cords = self._remove_duplicates(overall_tail_cords)
        return len(counted_cords)

    def part_2(self):
        prepared_data = super().read_input_file(self.file_path)
        test_data = list(map(self._prepare_data, test_day_9_data))
        print(test_data)
        data = test_data

        knot_cords = [
            [0, 0, 0],
            [1, 0, 0],
            [2, 0, 0],
            [3, 0, 0],
            [4, 0, 0],
            [5, 0, 0],
            [6, 0, 0],
            [7, 0, 0],
            [8, 0, 0],
            [9, 0, 0],
        ]
        for i, j in zip(knot_cords, knot_cords[1:]):
            print(i, j)
        tail_cords, head_cords = [0, 0], [0, 0]
        overall_tail_cords = [[0, 0]]
        for step in data:
            """0 - X
               1 - Y
            """
            if step[0] == 'R':
                for _ in range(1, step[1] + 1):  # increment coordinates n times
                    for i in range(len(knot_cords)):
                        knot_cords[i][1] += 1

                        # head_cords[0] += 1
                    # if abs(head_cords[0] - tail_cords[0]) > 1:
                    #     tail_cords[0] += 1
                    #     tail_cords[1] = head_cords[1]
                    #     overall_tail_cords = self._check_in_absence(overall_tail_cords, tail_cords[0], tail_cords[1])

            elif step[0] == 'L':
                for _ in range(1, step[1] + 1):
                    head_cords[0] -= 1
                    if abs(head_cords[0] - tail_cords[0]) > 1:
                        tail_cords[0] -= 1
                        tail_cords[1] = head_cords[1]
                        overall_tail_cords = self._check_in_absence(overall_tail_cords, tail_cords[0], tail_cords[1])

            elif step[0] == 'U':
                for _ in range(1, step[1] + 1):
                    head_cords[1] += 1
                    if abs(head_cords[1] - tail_cords[1]) > 1:
                        tail_cords[1] += 1
                        tail_cords[0] = head_cords[0]
                        overall_tail_cords = self._check_in_absence(overall_tail_cords, tail_cords[0], tail_cords[1])
            else:
                for _ in range(1, step[1] + 1):
                    head_cords[1] -= 1
                    if abs(head_cords[1] - tail_cords[1]) > 1:
                        tail_cords[1] -= 1
                        tail_cords[0] = head_cords[0]
                        overall_tail_cords = self._check_in_absence(overall_tail_cords, tail_cords[0], tail_cords[1])

        counted_cords = self._remove_duplicates(overall_tail_cords)
        return len(counted_cords)


if __name__ == "__main__":
    day_9 = Day9("/Users/olim/Downloads/input9.txt")
    # print("Part 1 --->", day_9.part_1())
    print("Part 2 --->", day_9.part_2())
