def generate_unsorted_data(size: int) -> list[int]:
    """Generate an unsorted list of integers from 0 to size-1."""
    data = list(range(size))
    data.reverse()
    return data


unsorted_items_10 = generate_unsorted_data(10)
unsorted_items_100 = generate_unsorted_data(100)
unsorted_items_1_000 = generate_unsorted_data(1000)
unsorted_items_10_000 = generate_unsorted_data(10_000)
unsorted_items_100_000 = generate_unsorted_data(100_000)
unsorted_items_1_000_000 = generate_unsorted_data(1_000_000)
