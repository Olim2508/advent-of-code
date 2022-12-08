from base import BaseService
from test_data import test_day_7_data


class Day7(BaseService):
    def __init__(self, file_path):
        super().__init__(file_path)

    def _prepare_data(self, item: str):
        item = super()._prepare_data(item)
        item = item.split(" ")
        return item

    def part_1(self):
        prepared_data = super().read_input_file(self.file_path)
        test_data = map(self._prepare_data, test_day_7_data)
        dir_tree_list = []
        cd_back_list = []
        temp_len = 0
        for com in prepared_data:
            if com[0] == "$":
                if com[1] == "cd":
                    if com[2] == '/':
                        dir_tree_list.append(['/', 0])
                        temp_len += len(dir_tree_list)
                    elif com[2] == '..':
                        cd_back_list.append(dir_tree_list.pop())
                        # for i in cd_back_list:
                        #     if i[0] == com[2]:
                        #         inx = cd_back_list.index(i)
                        #         dir_tree_list.append(cd_back_list.pop(inx))
                        #         break
                        # else:

                        # if not index_list:
                        # #     index_list.append(len(dir_tree_list) - 1)
                        # # if max(index_list) >= (len(dir_tree_list) - 1):
                        # #     index_list.append(min(index_list) - 1)
                        # # else:
                        # #     index_list.append(len(dir_tree_list) - 1)
                    else:
                        dir_tree_list.append([com[2], 0])
            elif com[0] == 'dir':
                pass
            else:
                for indx, item in enumerate(dir_tree_list):
                    item[1] = item[1] + int(com[0])
        sorted_sizes = sorted(dir_tree_list + cd_back_list, key=lambda x: x[1])
        size = 0
        for item in sorted_sizes:
            size += item[1]
            if size > 100000:
                return size - item[1]


if __name__ == "__main__":
    day_7 = Day7("/Users/olim/Downloads/input7.txt")
    print("Part 1 --->", day_7.part_1())
    # print("Part 2 --->", day_7.solution(letter_group_number=14))
