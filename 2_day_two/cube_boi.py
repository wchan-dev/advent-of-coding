# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

from entry import Entry


class CubeBoi:
    def __init__(self, constraint: dict):
        self.constraint = constraint

    def get_id(self, line: str) -> int:
        game_idx = line.find("Game") + len("Game")
        semi_colon_idx = line.find(":")
        return int(line[game_idx:semi_colon_idx].strip())

    def is_valid_config(self, element):
        entry = Entry()
        entry.populate_information(element)
        for color, value in entry.information.items():
            if self.constraint[color] < value:
                return False
        return True

    def least_possible(self, line: str) -> Entry:
        parsed = self._parse(line)
        min_entry = Entry()
        for config in parsed:
            entry = Entry()
            entry.populate_information(config)
            for color, value in entry.information.items():
                min_entry.information[color] = max(value, min_entry.information[color])
        return min_entry

    def power_cumulative(self, entry: Entry):
        reduced = 1
        for val in entry.information.values():
            reduced *= val
        return reduced

    def _parse(self, line: str):
        line = line[slice(line.find(":") + 1, len(line))]
        parsed = [
            [val.strip() for val in element.split(",")] for element in line.split(";")
        ]
        return parsed
