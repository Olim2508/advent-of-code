from base import BaseService


class Day6(BaseService):
    def __init__(self, file_path):
        super().__init__(file_path)

    def _prepare_data(self, item: str):
        item = super()._prepare_data(item)
        return item

    def solution(self, letter_group_number=4):
        prepared_data = super().read_input_file(self.file_path)
        temp_list = []
        order = 0
        for i in range(len(prepared_data[0])):
            for j in range(i, len(prepared_data[0])):
                if len(temp_list) > letter_group_number:
                    continue
                elif len(temp_list) == letter_group_number:
                    if len(temp_list) == len(list(set(temp_list))):
                        order = j + 1
                        break
                else:
                    temp_list.append(prepared_data[0][j])
                    if len(temp_list) == letter_group_number:
                        if len(temp_list) == len(list(set(temp_list))):
                            order = j + 1
                            temp_list.clear()
                            break
            else:
                temp_list.clear()
            if order > 0:
                break
        return order


if __name__ == "__main__":
    day_6 = Day6("/Users/olim/Downloads/input6.txt")
    print("Part 1 --->", day_6.solution())
    print("Part 2 --->", day_6.solution(letter_group_number=14))
