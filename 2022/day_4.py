import string

from base import BaseService


class Day4(BaseService):
    def __init__(self, file_path):
        super().__init__(file_path)

    def _prepare_data(self, item: str):
        item = super()._prepare_data(item)
        item = item.split(",")
        item[0], item[1] = item[0].split("-"), item[1].split("-")
        return item
    
    def solution(self, all=True):
        prepared_data = super().read_input_file(self.file_path)
        count = 0
        for i in prepared_data:
            left_list = [*range(int(i[0][0]), int(i[0][1]) + 1)]
            right_list = [*range(int(i[1][0]), int(i[1][1]) + 1)]
            if all:
                if all(elem in left_list for elem in right_list):
                    count += 1
            else:
                if any(elem in left_list for elem in right_list):
                    count += 1
        return count
    

if __name__ == '__main__':
    day_4 = Day4('/Users/olim/Downloads/input4.txt')
    # print("Part 1 --->", day_4.solution())
    print("Part 2 --->", day_4.solution(all=False))
    