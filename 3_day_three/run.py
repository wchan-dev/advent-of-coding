from parser_boi import ParserBoi

parser_boi = ParserBoi()

with open("3_day_three/input.txt", "r") as file:
    for line in file:
        res = parser_boi.is_part(line.strip())
        print(res)
