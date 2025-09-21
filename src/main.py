from datetime import datetime

from src.scripts import bucket_sort, gnome_sort
from src.utils import (
    process_time_diference_in_ms,
    save_multiple_plots
)
from src.data import (
    random_items_10,
    random_items_100,
    random_items_1_000,
    random_items_10_000,
    random_items_100_000,
    random_items_1_000_000,
    sorted_items_10,
    sorted_items_100,
    sorted_items_1_000,
    sorted_items_10_000,
    sorted_items_100_000,
    sorted_items_1_000_000,
    unsorted_items_10,
    unsorted_items_100,
    unsorted_items_1_000,
    unsorted_items_10_000,
    unsorted_items_100_000,
    unsorted_items_1_000_000,
)


def run_comparative_analysis():
    """
    Executa uma análise comparativa entre os algoritmos Bucket Sort e
    Gnome Sort, medindo o tempo de execução para listas de diferentes
    características (ordenadas, desordenadas e aleatórias) e tamanhos.
    Gera gráficos comparativos dos tempos de execução.
    """

    sizes = [10, 100, 1_000, 10_000, 100_000, 1_000_000]

    sorted_items = [
        sorted_items_10,
        sorted_items_100,
        sorted_items_1_000,
        sorted_items_10_000,
        sorted_items_100_000,
        sorted_items_1_000_000,
    ]

    unsorted_items = [
        unsorted_items_10,
        unsorted_items_100,
        unsorted_items_1_000,
        unsorted_items_10_000,
        unsorted_items_100_000,
        unsorted_items_1_000_000,
    ]

    random_items = [
        random_items_10,
        random_items_100,
        random_items_1_000,
        random_items_10_000,
        random_items_100_000,
        random_items_1_000_000,
    ]

    all_times_sorted = {
        "Bucket Sort": [],
        "Gnome Sort": []
    }

    all_times_unsorted = {
        "Bucket Sort": [],
        "Gnome Sort": []
    }

    all_times_random = {
        "Bucket Sort": [],
        "Gnome Sort": []
    }

    for index in range(len(sizes)):
        # Sorted items
        start = datetime.now()
        bucket_sort(sorted_items[index])
        end = datetime.now()
        all_times_sorted["Bucket Sort"].append(process_time_diference_in_ms(
            start, end
        ))

        start = datetime.now()
        gnome_sort(sorted_items[index])
        end = datetime.now()
        all_times_sorted["Gnome Sort"].append(process_time_diference_in_ms(
            start, end
        ))

        # Unsorted items
        start = datetime.now()
        bucket_sort(unsorted_items[index])
        end = datetime.now()
        all_times_unsorted["Bucket Sort"].append(process_time_diference_in_ms(
            start, end
        ))

        start = datetime.now()
        gnome_sort(unsorted_items[index])
        end = datetime.now()
        all_times_unsorted["Gnome Sort"].append(process_time_diference_in_ms(
            start, end
        ))

        # Random items
        start = datetime.now()
        bucket_sort(random_items[index])
        end = datetime.now()
        all_times_random["Bucket Sort"].append(process_time_diference_in_ms(
            start, end
        ))

        start = datetime.now()
        gnome_sort(random_items[index])
        end = datetime.now()
        all_times_random["Gnome Sort"].append(process_time_diference_in_ms(
            start, end
        ))

    save_multiple_plots(
        sizes,
        all_times_sorted,
        "results/sorted_comparison.png"
    )

    save_multiple_plots(
        sizes,
        all_times_unsorted,
        "results/unsorted_comparison.png"
    )

    save_multiple_plots(
        sizes,
        all_times_random,
        "results/random_comparison.png"
    )
