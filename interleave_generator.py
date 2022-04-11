def interleave(*iterables):
    """
    This generator creates a 'combined list' from all the iterable objects it receives.
    the generator chains all the objects by their index.
    This function first chains all who are in index 1 and then the second etc.
    :param iterables: iterable objects
    :return: a new list of the iterables we got using yield.
    """
    yield [item for sub_list in zip(*iterables) for item in sub_list]


if __name__ == '__main__':
    for var in interleave('abc', [1, 2, 3], ('!', '@', '#')):
        print(var)
