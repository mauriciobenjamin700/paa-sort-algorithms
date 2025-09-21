def generate_sorted_data(size: int) -> list[int]:
    """Generate a sorted list of integers from 0 to size-1."""
    return list(range(size))


sorted_items_10 = generate_sorted_data(10)
sorted_items_100 = generate_sorted_data(100)
sorted_items_1_000 = generate_sorted_data(1000)
sorted_items_10_000 = generate_sorted_data(10_000)
sorted_items_100_000 = generate_sorted_data(100_000)
sorted_items_1_000_000 = generate_sorted_data(1_000_000)
