from base import BaseService


# Day-2.  2.12.2022
class RockPaperScissors(BaseService):
    points = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    round_points = {"LOSE": 0, "DRAW": 3, "WIN": 6}

    def __init__(self, file_path):
        super().__init__(file_path)

    def _prepare_data(self, item):
        item = item.replace("\n", "").split(" ")
        return item

    def calculate_total_points(self):
        data = self.read_input_file(self.file_path)
        total_points = 0
        for item in data:
            if item[0] == "A" and item[1] == "Y":
                total_points += self.points[item[1]]
                total_points += self.round_points["WIN"]
            elif item[0] == "A" and item[1] == "X":
                total_points += self.points[item[1]]
                total_points += self.round_points["DRAW"]
            elif item[0] == "A" and item[1] == "Z":
                total_points += self.points[item[1]]
                total_points += self.round_points["LOSE"]
            elif item[0] == "B" and item[1] == "X":
                total_points += self.points[item[1]]
                total_points += self.round_points["LOSE"]
            elif item[0] == "B" and item[1] == "Y":
                total_points += self.points[item[1]]
                total_points += self.round_points["DRAW"]
            elif item[0] == "B" and item[1] == "Z":
                total_points += self.points[item[1]]
                total_points += self.round_points["WIN"]
            elif item[0] == "C" and item[1] == "X":
                total_points += self.points[item[1]]
                total_points += self.round_points["WIN"]
            elif item[0] == "C" and item[1] == "Y":
                total_points += self.points[item[1]]
                total_points += self.round_points["LOSE"]
            elif item[0] == "C" and item[1] == "Z":
                total_points += self.points[item[1]]
                total_points += self.round_points["DRAW"]

        return total_points

    def new_strategy_calculation(self):
        data = self.read_input_file(self.file_path)
        total_points = 0
        test_data = [['A', 'Y'], ['B', 'X'], ['C', 'Z']]  # test data. total should be 12
        for item in data:
            if item[0] == "A" and item[1] == "Y":
                total_points += self.points["X"]
                total_points += self.round_points["DRAW"]
            elif item[0] == "A" and item[1] == "X":
                total_points += self.points["Z"]
                total_points += self.round_points["LOSE"]
            elif item[0] == "A" and item[1] == "Z":
                total_points += self.points["Y"]
                total_points += self.round_points["WIN"]
            elif item[0] == "B" and item[1] == "X":
                total_points += self.points["X"]
                total_points += self.round_points["LOSE"]
            elif item[0] == "B" and item[1] == "Y":
                total_points += self.points["Y"]
                total_points += self.round_points["DRAW"]
            elif item[0] == "B" and item[1] == "Z":
                total_points += self.points["Z"]
                total_points += self.round_points["WIN"]
            elif item[0] == "C" and item[1] == "X":
                total_points += self.points["Y"]
                total_points += self.round_points["LOSE"]
            elif item[0] == "C" and item[1] == "Y":
                total_points += self.points["Z"]
                total_points += self.round_points["DRAW"]
            elif item[0] == "C" and item[1] == "Z":
                total_points += self.points["X"]
                total_points += self.round_points["WIN"]
        return total_points


rock_paper_scissors = RockPaperScissors('/Users/olim/Downloads/input2.txt')

print(rock_paper_scissors.new_strategy_calculation())
