from base import BaseService


class Day2(BaseService):
    def __init__(self, file_path):
        self.max_numbers = {"red": 12, "green": 13, "blue": 14}
        super().__init__(file_path)

    def parse_game(self, game: str) -> tuple:
        game_info, game_set = game.split(": ")
        _, game_id = game_info.split(" ")
        return game_id, game_set.split("; ")

    def solution(self, is_power_sum=False) -> int:
        data = self.read_input_file()
        res = 0
        for game in data:
            game_id, set_list = self.parse_game(game)
            if is_power_sum:
                power_of_set = self.get_power_of_set(set_list)
                res += power_of_set
            else:
                is_set_possible = self.is_set_possible(set_list)
                if is_set_possible:
                    res += int(game_id)
        return res

    def is_set_possible(self, set_list: list) -> bool:
        for s in set_list:
            cube_map_list = s.split(",")
            for cube_map in cube_map_list:
                num, color = cube_map.split()
                if self.max_numbers[color] < int(num):
                    return False
        return True

    def get_power_of_set(self, set_list: list) -> int:
        max_nums = {"red": 1, "green": 1, "blue": 1}
        for s in set_list:
            cube_map_list = s.split(",")
            for cube_map in cube_map_list:
                num, color = cube_map.split()
                max_nums[color] = max(max_nums[color], int(num))
        power = max_nums["red"] * max_nums["green"] * max_nums["blue"]
        return power


if __name__ == "__main__":
    day2 = Day2("input_day_2.txt")
    print("Part 1 --->", day2.solution())
    print("Part 2 --->", day2.solution(is_power_sum=True))
