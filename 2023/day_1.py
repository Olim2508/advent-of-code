from base import BaseService


class Day1(BaseService):
    def __init__(self, file_path):
        self.number_map = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }
        super().__init__(file_path)

    def solution(self, accept_text_nums=False):
        data = self.read_input_file()
        res = 0
        for line in data:
            line_nums = self.get_line_nums(line, accept_text_nums)
            res += int(line_nums[0] + line_nums[-1])
        return res

    def get_line_nums(self, line, accept_text_nums):
        nums = []
        for i in range(len(line)):
            if line[i].isnumeric():
                nums.append(line[i])
            else:
                if accept_text_nums:
                    for num_str in self.number_map:
                        if line[i: i + len(num_str)] == num_str:
                            nums.append(self.number_map[num_str])
        return nums


if __name__ == "__main__":
    day1 = Day1("input_day_1.txt")
    print("Part 1 --->", day1.solution())
    print("Part 2 --->", day1.solution(accept_text_nums=True))
