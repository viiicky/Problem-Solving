from typing import List


def is_valid(new_item, existing_set):
    if new_item in existing_set:
        return False

    hour_sum = 0
    minute_sum = 0
    for item in existing_set:
        if item.type == 'h':
            hour_sum += item.value
        elif item.type == 'm':
            minute_sum += item.value

    if new_item.type == 'h' and new_item.value + hour_sum > 11:
        return False

    if new_item.type == 'm' and new_item.value + minute_sum > 59:
        return False

    return True


class BinaryTime:
    def __init__(self, time_type, value):
        self.type = time_type
        self.value = value

    def __hash__(self) -> int:
        return hash((self.type, self.value))

    def __eq__(self, other):
        return self.type == other.type and self.value == other.value

    def __repr__(self):
        return f'{self.value}{self.type}'

    def __add__(self, other):
        if self.type != other.type:
            raise NotImplementedError

        return self.value + other.value


def format_response(original_response):
    formatted_response = set()
    for items in original_response:
        hours = 0
        minutes = 0
        for item in items:
            if item.type == 'h':
                hours += item.value
            elif item.type == 'm':
                minutes += item.value
        formatted_response.add(f'{hours}:{str(minutes).zfill(2)}')

    return formatted_response


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn == 0:
            return ['0:00']

        if turnedOn in [9, 10]:
            return []

        base_set = [BinaryTime('m', 1),
                    BinaryTime('m', 2),
                    BinaryTime('m', 4),
                    BinaryTime('m', 8),
                    BinaryTime('m', 16),
                    BinaryTime('m', 32),
                    BinaryTime('h', 1),
                    BinaryTime('h', 2),
                    BinaryTime('h', 4),
                    BinaryTime('h', 8)]

        if turnedOn == 1:
            return format_response([{x} for x in base_set])

        response_set = [{x} for x in base_set]
        for i in range(turnedOn - 1):
            new_set = []
            for base_item in base_set:
                for response_item in response_set:
                    if is_valid(base_item, response_item):
                        new_set.append({base_item} | response_item)
            response_set = new_set.copy()

        return format_response(response_set)


class Solution2:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times = []
        for hour in range(0, 12):
            for minute in range(0, 60):
                number_of_ones = bin(hour).count('1') + bin(minute).count('1')
                if number_of_ones == turnedOn:
                    times.append(f'{hour}:{minute:02d}')
        return times


sol = Solution2()
print(sol.readBinaryWatch(2))
