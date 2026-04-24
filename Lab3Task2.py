
def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # Record each value of total and num at the end of the loop body. First: num = 4, total = 4. Second: num = 9, total = 13. Third: num = 2, total = 15. Fourth: num = 1, total = 16.
    return total

result = tally([4, 9, 2, 1])

'''

def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # Record each value of new_list and idx at the end of the loop body. First: idx = 0, new_list = [4]. Second: idx = 1, new_list = [4,9]. Third: idx = 2, new_list = [4,9,2]. Fourth: idx = 3, new_list = [4,9,2,1].
    return new_list                    # How does this loop differ from that above? We are iterating through nums using 'for idx in range(len(nums))' instead of 'for num in nums.'

result = copy([4, 9, 2, 1])


def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # Record each value of new_list and value at the end of the loop body. First: value = 4, new_list = [5]. Second: value = 9, new_list = [5,10]. Third: value = 2, new_list = [5,10,3]. Fourth: value = 1, new_list = [5,10,3,2].
    return new_list

result = increment_all([4, 9, 2, 1])
'''