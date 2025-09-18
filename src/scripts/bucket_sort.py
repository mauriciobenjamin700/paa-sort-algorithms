def bucket_sort(
        arr: list[int],
        reverse: bool = False,
        items_per_bucket: int = 5
) -> list[int]:
    """
    Ordena uma lista de inteiros usando o algoritmo Bucket Sort.

    Funcionamento:
    1. O algoritmo cria vários "baldes" (listas auxiliares) para distribuir
        os elementos da lista original conforme seus valores.
    2. Cada elemento é colocado em um balde de acordo com seu valor, usando
        uma função de mapeamento baseada no valor mínimo, máximo e tamanho dos
        baldes.
    3. Após a distribuição, cada balde é ordenado individualmente usando um
        algoritmo de ordenação interno (neste caso, a função sorted do Python).
        obs: Geralmente o Tim Sort, que é o algoritmo usado pela função sorted.
    4. Por fim, os baldes ordenados são concatenados para formar a lista
        final ordenada.

    O parâmetro 'reverse' permite escolher entre ordem crescente (padrão) ou
    decrescente.
    O Bucket Sort é eficiente para listas com valores distribuídos
    uniformemente.
    """

    if not arr:
        return []

    min_value = min(arr)
    max_value = max(arr)
    bucket_count = max(1, len(arr) // items_per_bucket)
    bucket_size = max(1, (max_value - min_value + 1) // bucket_count)

    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        idx = min((num - min_value) // bucket_size, bucket_count - 1)
        buckets[idx].append(num)

    sorted_arr = []

    for bucket in buckets:
        sorted_bucket = sorted(bucket, reverse=reverse)
        sorted_arr.extend(sorted_bucket)

    return sorted_arr
