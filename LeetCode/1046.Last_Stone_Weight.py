from typing import List
import heapq


# O(N^2)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # sort the input
        stones.sort(reverse=True)

        # do the below steps until there is 1 or 0 stone left in the list
        while len(stones) > 1:
            # traverse the list from backward and solve for last two items, and get the result
            last_stone = stones.pop()
            last_but_one = stones.pop()
            if last_stone != last_but_one:
                abs_diff = abs(last_stone - last_but_one)
                # put the result at right place
                pos = self.get_position(stones, abs_diff, 0, len(stones) - 1)
                stones.insert(pos, abs_diff)

        return stones[0] if stones[0] else None

    def get_position(self, array, x, start, end):
        mid = start + end // 2
        center_item = array[mid]
        if center_item == x:
            return mid

        length = end - start + 1
        if length == 1:
            return None

        if center_item < x:
            return self.get_position(array, x, mid + 1, end)
        else:
            return self.get_position(array, x, start, mid - 1)


# O(N^2)
class Solution2:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # do the following as long as there is at most 1 stone left
        while len(stones) > 1:
            # traverse the array and find max and max but one indices and delete those items
            heaviest_stone_position, heaviest_stone_weight = self.get_heaviest_stone(stones)
            del stones[heaviest_stone_position]

            second_heaviest_stone_position, second_heaviest_stone_weight = self.get_heaviest_stone(stones)
            del stones[second_heaviest_stone_position]

            # if necessary put the new item
            diff = heaviest_stone_weight - second_heaviest_stone_weight
            if diff != 0:
                stones.append(diff)

        # return accordingly
        return stones[0] if stones else 0

    def get_heaviest_stone(self, stones):
        heaviest_stone_weight = 0
        heaviest_stone_position = None
        for position, stone_weight in enumerate(stones):
            if stone_weight > heaviest_stone_weight:
                heaviest_stone_weight = stone_weight
                heaviest_stone_position = position

        return heaviest_stone_position, heaviest_stone_weight


# O(NlogN)
def heappush(heap, item):
    return heapq.heappush(heap, -item)


def heappop(heap):
    return -heapq.heappop(heap)


class Solution3:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = []
        for stone in stones:
            heappush(stones_heap, stone)

        while len(stones_heap) > 1:
            heaviest_stone = heappop(stones_heap)
            heaviest_but_one_stone = heappop(stones_heap)

            if heaviest_stone != heaviest_but_one_stone:
                new_stone = heaviest_stone - heaviest_but_one_stone
                heappush(stones_heap, new_stone)

        return heappop(stones_heap) if stones_heap else 0


solution = Solution3()
print(solution.lastStoneWeight([2, 7, 4, 1, 8, 1]))
