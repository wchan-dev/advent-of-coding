class ParserBoi:
    is_number = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    is_period = {"."}
    not_symbol = is_number.union(is_period)

    def __init__(self):
        previous_parts: []
        current_parts: []

    def is_part(self, line: str):
        result = []
        for idx, char in enumerate(line):
            if char not in self.not_symbol:
                entry = self.find_part_horizontal(idx, line)
                result.append(entry)
        return result

    def find_part_horizontal(self, symbol_idx: int, line: str):
        before_symbol = ""
        after_symbol = ""
        for i in range(symbol_idx - 1, -1, -1):
            if line[i] in self.is_number:
                before_symbol = line[i] + before_symbol
            else:
                break

        for i in range(symbol_idx + 1, len(line), 1):
            if line[i] in self.is_number:
                after_symbol += line[i]
            else:
                break
        return [before_symbol, after_symbol]

    def find_part_vertical(self, symbol_idx: int, line: str):
        pass
