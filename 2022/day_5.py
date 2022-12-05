import string

from base import BaseService


class Day5(BaseService):
    def __init__(self, file_path):
        super().__init__(file_path)

    def _prepare_data(self, item: str):
        item = super()._prepare_data(item)
        return item

    def get_crates(self):
        return [
            ["J", "H", "G", "M", "Z", "N", "T", "F"],
            ["V", "W", "J"],
            ["G", "V", "L", "J", "B", "T", "H"],
            ["B", "P", "J", "N", "C", "D", "V", "L"],
            ["F", "W", "S", "M", "P", "R", "G"],
            ["G", "H", "C", "F", "B", "N", "V", "M"],
            ["D", "H", "G", "M", "R"],
            ["H", "N", "M", "V", "Z", "D"],
            ["G", "N", "F", "H"],
        ]

    def get_procedures(self, data):
        procedures = []
        start_parcing = False
        for i in data:
            if start_parcing:
                procedures.append(i.split(" "))
            if i == "":
                start_parcing = True
        return procedures

    def _concat_top_crates(self, crates):
        res = str()
        for c in crates:
            res += c.pop()
        return res

    def part_1(self):
        prepared_data = super().read_input_file(self.file_path)
        crates = self.get_crates()
        procedures = self.get_procedures(prepared_data)
        for p in procedures:
            num_of_crates = int(p[1])
            from_stack = int(p[3])
            to_stack = int(p[5])
            for i in range(num_of_crates):
                c = crates[from_stack - 1].pop()
                crates[to_stack - 1].append(c)
        return self._concat_top_crates(crates)

    def part_2(self):
        prepared_data = super().read_input_file(self.file_path)
        crates = self.get_crates()
        procedures = self.get_procedures(prepared_data)
        for p in procedures:
            num_of_crates = int(p[1])
            from_stack = int(p[3])
            to_stack = int(p[5])
            for i in range(num_of_crates, 0, -1):
                c = crates[from_stack - 1].pop(-i)
                crates[to_stack - 1].append(c)
        return self._concat_top_crates(crates)


if __name__ == "__main__":
    day_4 = Day5("/Users/olim/Downloads/input5.txt")
    print("Part 1 --->", day_4.part_1())
    print("Part 2 --->", day_4.part_2())
