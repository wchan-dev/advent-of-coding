# pylint: disable=missing-module-docstring
from calibration_handler import CalibrationHandler
calibration_handler = CalibrationHandler()

result = 0
with open("1_day_one/input.txt", "r") as file:
    for line in file:
        first_digit = calibration_handler.word_to_digit(line)
        last_digit = calibration_handler.word_to_digit(reversed(line), True)
        calibrated = int(f"{first_digit}{last_digit}")
        result += calibrated

print(result)
