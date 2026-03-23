import time
import random

def bubbleSort(nums:list):
    for i in range(len(nums)):
        swapped = False

        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True

        if not swapped:
            break
    
    return nums

if __name__ == "__main__":
    number = [random.randint(1, 10000) for _ in range(2000)]
    start = time.perf_counter()
    bubbleSort(number)
    end = time.perf_counter()
    print(f"{end - start:.10f} sec")