import time
import random

def insertionSort(nums:list):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key
    
    return nums

if __name__ == "__main__":
    number = [random.randint(1, 10000) for _ in range(2000)]
    start = time.perf_counter()
    insertionSort(number)
    end = time.perf_counter()
    print(f"{end - start:.10f} sec")