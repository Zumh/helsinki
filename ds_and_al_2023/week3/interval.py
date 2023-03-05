def count(numbers):
    """
    count number difference in 1 interval
    """

    numbers.sort()

    count_interval = 1
    max_count = 1
    for index, number in enumerate(numbers):
        prev_number = numbers[index - 1]
        if prev_number == number + 1:
            count_interval += 1
        else:
            max_count = max(max_count, count_interval)
            count_interval = 1
                
    max_count = max(max_count, count_interval)
    return max_count

if __name__ == "__main__":
    print(count([1, 1, 1, 1])) # 1
    print(count([10, 4, 8])) # 1
    print(count([7, 6, 1, 8])) # 3
    print(count([1, 2, 1, 2, 1, 2])) # 2
    print(count([987654, 12345678, 987653, 999999, 987655])) # 3