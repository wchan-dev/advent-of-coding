# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


class CalibrationHandler:
    NUM_TO_WORD = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    def __init__(self):
        pass

    def word_to_digit(self, line: str, reversed=False):
        tracked = ""
        for char in line:
            if reversed:
                tracked = char + tracked
            else:
                tracked += char
            if char.isdigit():
                return int(char)
            for key in self.NUM_TO_WORD.keys():
                if key in tracked:
                    return self.NUM_TO_WORD[key]
