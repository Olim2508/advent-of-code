# DAY 1  1.12.2022
class CalorieCounting:
    def __init__(self, file_path):
        self.file_path = file_path

    def _turn_into_int(self, item):
        if (c := item.replace("\n", "")) != "":
            return int(c)
        else:
            return c

    def read_input_file(self, file_path):
        with open(file_path) as f:
            data = f.readlines()
            res_data = list(map(self._turn_into_int, data))
        return res_data

    def group_calorie_by_elf(self):
        data_list = self.read_input_file(self.file_path)
        group_by_elf_data_dict, elf_num = {}, 1
        for index, cal in enumerate(data_list):
            if cal == "":
                elf_num += 1
            else:
                if elf_data := group_by_elf_data_dict.get(elf_num):
                    elf_data.append(cal)
                else:
                    group_by_elf_data_dict.update({elf_num: [cal]})
        return group_by_elf_data_dict

    def _get_sorted_grouped_calories_dict(self, grouped_calories_dict):
        return {
            k: v
            for k, v in sorted(
                grouped_calories_dict.items(), key=lambda item: sum(item[1])
            )
        }

    def get_n_numbers_of_max_calories_sum(self, n=1):
        sorted_dict = self._get_sorted_grouped_calories_dict(
            self.group_calorie_by_elf()
        )
        n_keys = [list(sorted_dict)[-i] for i in range(1, n + 1)]
        sum_of_max_n = 0
        for key in n_keys:
            sum_of_max_n += sum(sorted_dict[key])
        return sum_of_max_n


calorie_count = CalorieCounting("/Users/olim/Downloads/input.txt")
print(calorie_count.get_n_numbers_of_max_calories_sum(3))
