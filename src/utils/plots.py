import matplotlib.pyplot as plt


def plot_sorting_times(
    sizes: list[int],
    times: list[float],
    algorithm_name: str
):
    """
    Plota o gráfico de tempos de execução para um algoritmo de ordenação.

    As entradas são:
    - sizes: lista de tamanhos das entradas.
    - times: lista de tempos de execução correspondentes.
    - algorithm_name: nome do algoritmo para o título do gráfico.
    """
    plt.plot(sizes, times, label=algorithm_name)
    plt.xlabel("Tamanho da entrada")
    plt.ylabel("Tempo (ms)")
    plt.title("Comparação de Algoritmos de Ordenação")
    plt.legend()
    plt.show()


def save_plot(
    sizes: list[int],
    times: list[float],
    algorithm_name: str,
    filename: str
):
    """
    Salva o gráfico de tempos de execução para um algoritmo de ordenação.

    As entradas são:
    - sizes: lista de tamanhos das entradas.
    - times: lista de tempos de execução correspondentes.
    - algorithm_name: nome do algoritmo para o título do gráfico.
    - filename: nome do arquivo onde o gráfico será salvo.
    """
    plt.plot(sizes, times, label=algorithm_name)
    plt.xlabel("Tamanho da entrada")
    plt.ylabel("Tempo (ms)")
    plt.title("Comparação de Algoritmos de Ordenação")
    plt.legend()
    plt.savefig(filename)
    plt.close()


def plot_multiple_sorting_times(
    sizes: list[int],
    all_times: dict[str, list[float]]
):
    """
    Plota o gráfico comparativo de tempos de execução para múltiplos
    algoritmos.

    As entradas são:
    - sizes: lista de tamanhos das entradas.
    - all_times: dicionário onde as chaves são nomes dos algoritmos e os
      valores são listas de tempos de execução correspondentes.
    """
    for algorithm_name, times in all_times.items():
        plt.plot(sizes, times, label=algorithm_name)
    plt.xlabel("Tamanho da entrada")
    plt.ylabel("Tempo (ms)")
    plt.title("Comparação de Algoritmos de Ordenação")
    plt.legend()
    plt.show()


def save_multiple_plots(
    sizes: list[int],
    all_times: dict[str, list[float]],
    filename: str,
    title: str
):
    """
    Salva o gráfico comparativo de tempos de execução para múltiplos
    algoritmos.

    As entradas são:
    - sizes: lista de tamanhos das entradas.
    - all_times: dicionário onde as chaves são nomes dos algoritmos e os
      valores são listas de tempos de execução correspondentes.
    - filename: nome do arquivo onde o gráfico será salvo.
    """
    for algorithm_name, times in all_times.items():
        plt.plot(sizes, times, label=algorithm_name)
    plt.xlabel("Tamanho da entrada")
    plt.ylabel("Tempo (ms)")
    plt.title(title)
    plt.legend()
    plt.savefig(filename)
    plt.close()
