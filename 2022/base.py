

class BaseService:
    def __init__(self, file_path):
        self.file_path = file_path

    def _prepare_data(self, item):
        item = item.replace("\n", "")
        return item

    def read_input_file(self, file_path):
        with open(file_path) as f:
            data = f.readlines()
            res_data = list(map(self._prepare_data, data))
        return res_data

