# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


class Entry:
    def __init__(self):
        self.information = {"red": 0, "green": 0, "blue": 0}

    def populate_information(self, entry):
        config = {}
        for data in entry:
            entry = {}
            entry[data.split()[1]] = int(data.split()[0])
            config.update(entry)
        self.information = config
