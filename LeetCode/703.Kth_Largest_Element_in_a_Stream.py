from typing import List
import unittest
import heapq


def heappush(heap, item):
    return heapq.heappush(heap, -item)


def heappop(heap):
    return -heapq.heappop(heap)


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.max_val = 10 ** 4
        # prepare a "count-array"; size 2*10^4 + 1
        self.counts = [0] * (2 * self.max_val + 1)

        # map the items from nums list to the indices of this array
        for num in self.nums:
            mapped_num = self._map(num)
            self.counts[mapped_num] += 1

    def add(self, val: int) -> int:
        # use the mapper to find the index of this new item, and increase the counter at that new item
        mapped_val = self._map(val)
        self.counts[mapped_val] += 1

        # then traverse the array from back, and find the kth largest position
        total = self.k
        position = None
        for i in range(len(self.counts) - 1, -1, -1):
            total -= self.counts[i]
            if total <= 0:
                position = i
                break

        # use the mapper again to return the unmapped value of this position
        return self._unmap(position)

    def _map(self, value):
        return value + self.max_val

    def _unmap(self, value):
        return value - self.max_val


class KthLargest2:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums_heap = []
        for num in self.nums:
            heappush(self.nums_heap, num)

    def add(self, val: int) -> int:
        heappush(self.nums_heap, val)

        popped_items = []
        for _ in range(self.k):
            popped_items.append(heappop(self.nums_heap))

        for popped_item in popped_items:
            heappush(self.nums_heap, popped_item)

        return popped_items[-1]


class KthLargest3:
    def __init__(self, k: int, nums: List[int]):
        """Time complexity: O(N), where N is the number of elements in nums"""
        self.k = k
        self.nums = nums
        # If we can already find the k-th largest element from this initial array,
        # prune everything smaller than the k-th largest element - those values are not going to be of interest, ever.
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        # Now at this point either the heap is of size k, or k-1, given the input constraints

    def add(self, val: int) -> int:
        """Time complexity: O(logN), where N is the number of elements in nums"""
        # If the size of heap is smaller than k (only case: k-1), just add the element
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)

        # If we are coming to this else block, it means the size of the heap is k.
        # We want to maintain this k size of the heap,
        # so that we can easily return the k-th largest element by asking for the min element from the heap.
        # So, just push this item, and then call pop on the heap to eliminate the extra "bad" item after this push.
        #
        # Moreover, if we think about it,
        # in case the incoming value is already smaller or equal to the current minimum value in the heap,
        # we don't even need to do the push-pop because it is the same item that would get pushed and then popped.
        # Thus we can add the below condition to the else block.
        # This way, we touch heap, only when we really need to, else, we do not disturb it.
        elif val > self.nums[0]:
            heapq.heappushpop(self.nums, val)

        return self.nums[0]


class KthLargest4:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        return heapq.nlargest(self.k, self.nums)[-1]


class KthLargest5:
    def __init__(self, k: int, nums: List[int]):
        """Time complexity: O(N), where N is the number of elements in nums"""
        self.k = k
        self.nums = nums
        # Given the input constraints there is a possibility that there are k-1 items in the input nums.
        # In that case, just add a dummy value to match the size k.
        self.nums.append(float('-inf'))

        # If we can already find the k-th largest element from this initial array,
        # prune everything smaller than the k-th largest element - those values are not going to be of interest, ever.
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        """Time complexity: O(logN), where N is the number of elements in nums"""
        # The size of the heap is k right now, and we want to maintain this size of the heap
        # so that we can easily return the k-th largest element by asking for the min element from the heap.
        # So, just push this item, and then call pop on the heap to eliminate the extra "bad" item after this push.
        #
        # Moreover, if we think about it,
        # in case the incoming value is already smaller or equal to the current minimum value in the heap,
        # we don't even need to do the push-pop because it is the same item that would get pushed and then popped.
        # Thus we can add the below condition to the else block.
        # This way, we touch heap, only when we really need to, else, we do not disturb it.
        if val > self.nums[0]:
            heapq.heappushpop(self.nums, val)

        return self.nums[0]


class KthLargestTest(unittest.TestCase):
    def test_add(self):
        kth_largest = KthLargest5(3, [4, 5, 8, 2])
        self.assertEqual(4, kth_largest.add(3))
        self.assertEqual(5, kth_largest.add(5))
        self.assertEqual(5, kth_largest.add(10))
        self.assertEqual(8, kth_largest.add(9))
        self.assertEqual(8, kth_largest.add(4))

    def test_first_largest(self):
        kth_largest = KthLargest5(1, [])
        self.assertEqual(3, kth_largest.add(3))
        self.assertEqual(5, kth_largest.add(5))
        self.assertEqual(10, kth_largest.add(10))
        self.assertEqual(10, kth_largest.add(9))
        self.assertEqual(10, kth_largest.add(4))


if __name__ == '__main__':
    unittest.main()


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
