def all_perfect_numbers():
    """
    Generator function that runs infinitely.
    The function returns the next perfect number after each reading.
    Perfect number: one whose sum of divisors is equal to the number itself
    :return: Perfect number
    """
    up_to = int(2)
    while True:
        if sum(number for number in range(1, up_to) if not up_to % number) == up_to:
            yield up_to
        up_to += 1


if __name__ == '__main__':
    all_perfect_numbers_generator = all_perfect_numbers()
    for number in range(4):
        print(next(all_perfect_numbers_generator))

    # After the 4th call the computer works really hard.
