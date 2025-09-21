def gnome_sort(
    arr: list[int],
    reverse: bool = False
) -> list[int]:
    """
    Ordena uma lista de inteiros usando o algoritmo Gnome Sort.

    Funcionamento:
    1. O algoritmo percorre a lista comparando elementos adjacentes.
    2. Se os elementos estiverem fora de ordem, eles são trocados e o índice
    volta uma posição.
    3. Se estiverem em ordem, avança para o próximo elemento.
    4. O processo continua até o final da lista, garantindo que todos os
    elementos estejam ordenados.

    O parâmetro 'reverse' permite escolher entre ordem crescente (padrão) ou
    decrescente.
    O Gnome Sort é simples e intuitivo, mas não é eficiente para
    listas grandes.
    """

    if not arr:
        return []

    arr = arr.copy()
    i = 0
    n = len(arr)
    while i < n:
        if i == 0:
            i += 1
        if (
            (not reverse and arr[i] >= arr[i - 1])
            or
            (reverse and arr[i] <= arr[i - 1])
        ):
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr
