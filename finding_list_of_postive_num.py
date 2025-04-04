#Given a list of integers, find the sum of all positive numbers


def postive_num(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total
result = list(map(int, input("Enter integers with spaces: ").split()))
nums = postive_num(result)
print(f"the sum of positive number in the list is {nums}")