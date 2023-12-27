# pylint: disable=missing-module-docstring
# pylint: disable=

from cube_boi import CubeBoi

constraint = {"red": 12, "green": 13, "blue": 14}
cube_boi = CubeBoi(constraint)


with open("2_day_two/input.txt", "r") as file:
    total_sum = 0
    for line in file:
        entry = cube_boi.least_possible(line)
        total_sum += cube_boi.power_cumulative(entry)
    print(total_sum)
