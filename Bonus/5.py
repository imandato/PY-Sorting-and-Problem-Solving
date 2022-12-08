# Write your solution for algorithm 5 below

numbers = [5, 10, 4, 7, 6, 2]

def find_pair(numbers, target):
    sort_numbers = sorted(numbers)
    left = 0 
    right = len(sort_numbers) - 1

    while left < right:
        if sort_numbers[left] + sort_numbers[right] == target:
            return sort_numbers[left], sort_numbers[right]

        if sort_numbers[left]+ sort_numbers[right] < target:
            left += 1
        else:
            right -= 1
        
    return "no pairs add up to target number"


print(find_pair(numbers, 9))