from collections import deque
from parser_boi import ParserBoi


def read_third_line_one_liner(file_path):
    return next(line for i, line in enumerate(open(file_path)) if i == 2).strip()


parser_boi = ParserBoi()

# init parser_boi once
# utilize previous_parts and current_parts
empty_deque = deque([],maxlen=3)
with open("3_day_three/input.txt", "r") as file:
    for line in file:
        empty_deque.append(line)


print(empty_deque)
