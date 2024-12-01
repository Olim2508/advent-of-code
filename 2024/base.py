import os


class BaseService:
    def __init__(self, file_name):
        self.file_path = os.path.join("inputs", file_name)

    def _prepare_data(self, item):
        return item.replace("\n", "")

    def read_input_file(self):
        with open(self.file_path) as f:
            data = f.readlines()
            res_data = list(map(self._prepare_data, data))
        return res_data
