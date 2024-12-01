from collections import defaultdict

from base import BaseService


class Day1(BaseService):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.left = []
        self.right = []
        self.read_input_file()

    def read_input_file(self):
        data = super().read_input_file()
        for line in data:
            self.left.append(int(line.split("   ")[0]))
            self.right.append(int(line.split("   ")[1]))
        return data

    def part_1(self):
        self.left.sort()
        self.right.sort()
        res = 0
        for l, r in zip(self.left, self.right):
            res += abs(l - r)
        return res

    def part_2(self):
        res = 0
        right_dict = defaultdict(int)
        for r in self.right:
            right_dict[r] += 1

        for l in self.left:
            res += l * right_dict[l]

        return res


if __name__ == "__main__":
    day1 = Day1(file_path="input_day_1.txt")
    print("Part 1 --->", day1.part_1())
    print("Part 2 --->", day1.part_2())
