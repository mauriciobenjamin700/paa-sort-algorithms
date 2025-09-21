from random import shuffle


def generate_unsorted_data(size: int) -> list[int]:
    """Generate an unsorted list of integers from 0 to size-1."""

    data = list(range(size))
    shuffle(data)
    return data


random_items_10 = generate_unsorted_data(10)
random_items_100 = generate_unsorted_data(100)
random_items_1_000 = generate_unsorted_data(1000)
random_items_10_000 = generate_unsorted_data(10_000)
random_items_100_000 = generate_unsorted_data(100_000)
random_items_1_000_000 = generate_unsorted_data(1_000_000)
