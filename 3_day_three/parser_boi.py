class ParserBoi:
    is_number = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    is_period = {"."}
    not_symbol = is_number.union(is_period)

    def __init__(self):
        pass

    def is_part(self, line: str):
        for char in line:
            if char not in self.not_symbol:
                symbol_idx = line.find(char)
                if line[symbol_idx - 1] in self.is_number:
                    search_idx = symbol_idx - 1
                    part_number = ""
                    while line[search_idx] in self.is_number:
                        part_number = line[search_idx] + part_number
                        search_idx -= 1
                    return part_number
