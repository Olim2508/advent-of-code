from base import BaseService
from test_data import test_day_8_data
import math


class Day8(BaseService):
    def __init__(self, file_path):
        super().__init__(file_path)

    def _prepare_data(self, item: str):
        item = super()._prepare_data(item)
        item = list(map(int, list(item)))
        return item

    def part_1(self):
        prepared_data = super().read_input_file(self.file_path)
        test_data = list(map(self._prepare_data, test_day_8_data))

        counter = 0
        for i in range(len(prepared_data)):
            for j in range(len(prepared_data[i])):
                el = prepared_data[i][j]
                if j == 0 or j == len(prepared_data[i]) - 1:
                    counter += 1
                elif i == 0 or i == len(prepared_data) - 1:
                    counter += 1
                else:
                    added = False
                    # checking left
                    for l in range(0, j):
                        if prepared_data[i][l] < el:
                            pass
                        else:
                            break
                    else:
                        counter += 1
                        added = True

                    # checking right
                    if not added:
                        for r in range(j + 1, len(prepared_data[i])):
                            if prepared_data[i][r] < el:
                                pass
                            else:
                                break
                        else:
                            counter += 1
                            added = True

                    # checking top
                    if not added:
                        for t in range(0, i):
                            if prepared_data[t][j] < el:
                                pass
                            else:
                                break
                        else:
                            counter += 1
                            added = True

                    # checking bottom
                    if not added:
                        for b in range(i + 1, len(prepared_data)):
                            if prepared_data[b][j] < el:
                                pass
                            else:
                                break
                        else:
                            counter += 1
                            added = True
        return counter

    def part_2(self):
        prepared_data = super().read_input_file(self.file_path)
        test_data = list(map(self._prepare_data, test_day_8_data))
        data = prepared_data

        view_distances = []
        for i in range(len(data)):
            for j in range(len(data[i])):
                direction_views = []
                el = data[i][j]
                if j == 0 or j == len(data[i]) - 1:
                    pass
                elif i == 0 or i == len(data) - 1:
                    pass
                else:
                    # checking left
                    counter = 0
                    for l in range(j - 1, -1, -1):
                        # print(l)
                        # print(data[i][l], el, '\n\n')
                        if data[i][l] < el:
                            counter += 1
                        else:
                            counter += 1
                            break
                    direction_views.append(counter)

                    # checking right
                    counter = 0
                    for r in range(j + 1, len(data[i])):
                        if data[i][r] < el:
                            counter += 1
                        else:
                            counter += 1
                            break
                    direction_views.append(counter)

                    # checking top
                    counter = 0
                    for t in range(j - 1, -1, -1):
                        if data[t][j] < el:
                            counter += 1
                        else:
                            counter += 1
                            break
                    direction_views.append(counter)

                    # checking bottom
                    counter = 0
                    for b in range(i + 1, len(data)):
                        if data[b][j] < el:
                            counter += 1
                        else:
                            counter += 1
                            break
                    direction_views.append(counter)
                view_distances.append(math.prod(direction_views))

        print(max(view_distances), view_distances)


if __name__ == "__main__":
    day_8 = Day8("/Users/olim/Downloads/input8.txt")
    # print("Part 1 --->", day_8.part_1())
    print("Part 2 --->", day_8.part_2())
