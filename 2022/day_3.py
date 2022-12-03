import string

from base import BaseService


class Day3(BaseService):
    def __init__(self, file_path):
        super().__init__(file_path)

    def _prepare_data(self, item: str):
        item = super()._prepare_data(item)
        return item

    def _calculate_badges(self, common_badges: list):
        res = 0
        for c in common_badges:
            for index, letter in enumerate(list(string.ascii_letters)):
                if c[0] == letter:
                    res += index + 1
        return res

    def part_1(self):
        prepared_data = super().read_input_file(self.file_path)
        test_data = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg",
                     "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", 'ttgJtRGJQctTZtZT', "CrZsJsPPZsGzwwsLwLmpwMDw"]
        compartment_1, compartment_2, common = [], [], []
        for item in prepared_data:
            half_count = int(len(item) / 2)
            compartment_1.append(item[:half_count])
            compartment_2.append(item[half_count:])
        for (f_half, s_half) in zip(compartment_1, compartment_2):
            common.append(list(set(f_half) & set(s_half)))
        return self._calculate_badges(common)

    def part_2(self):
        prepared_data = super().read_input_file(self.file_path)
        test_data = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg",
                     "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", 'ttgJtRGJQctTZtZT', "CrZsJsPPZsGzwwsLwLmpwMDw"]
        counter = 0
        temporary_list, common_badges = [], []
        for item in prepared_data:
            temporary_list.append(item)
            counter += 1
            if counter == 3:
                common_badges.append(list(set(temporary_list[0]) & set(temporary_list[1]) & set(temporary_list[2])))
                temporary_list.clear()
                counter = 0
        return self._calculate_badges(common_badges)


day_3 = Day3('/Users/olim/Downloads/input3.txt')
