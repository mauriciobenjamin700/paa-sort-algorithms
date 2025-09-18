# BUCKET SORT E GNOME SORT

## Introdução ao Bucket Sort

O Bucket Sort é um algoritmo de ordenação criado para lidar de forma eficiente com listas de dados que possuem valores distribuídos de maneira relativamente uniforme. Ele foi proposto por Harold H. Seward em 1957, inicialmente para uso em computadores da IBM, e é considerado uma variação dos algoritmos de ordenação por distribuição.

O propósito do Bucket Sort é dividir os elementos em grupos (baldes) de acordo com seus valores, facilitando a ordenação interna de cada grupo e acelerando o processo de ordenação total. Ao invés de comparar cada elemento com todos os outros, como em algoritmos tradicionais, o Bucket Sort aproveita a distribuição dos dados para reduzir o número de comparações necessárias.

Esse método é especialmente útil para grandes volumes de dados que já estão quase ordenados ou distribuídos uniformemente, como dados de sensores, notas de alunos, ou qualquer situação em que os valores estejam espalhados de forma previsível.

O Bucket Sort é um exemplo clássico de como a estrutura dos dados pode ser explorada para melhorar a eficiência dos algoritmos de ordenação.

### Bucket Sort - Código completo

```python
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
```

### Passo a passo do código

1. **Verificação da lista**

   ```python
   if not arr:
       return []
   ```

   Se a lista estiver vazia, retorna uma lista vazia imediatamente.

2. **Cálculo dos valores mínimo e máximo**

   ```python
   min_value = min(arr)
   max_value = max(arr)
   ```

   Encontra o menor e o maior valor da lista para definir o intervalo dos dados.

3. **Definição do número de baldes**

   ```python
   bucket_count = max(1, len(arr) // items_per_bucket)
   ```

   O número de baldes é calculado dividindo o tamanho da lista pelo número de itens por balde (padrão 5). Garante pelo menos 1 balde.

4. **Cálculo do tamanho de cada balde**

   ```python
   bucket_size = max(1, (max_value - min_value + 1) // bucket_count)
   ```

   O tamanho do balde define quantos valores diferentes cada balde pode armazenar, ajudando a distribuir os elementos de forma uniforme.

5. **Criação dos baldes**

   ```python
   buckets = [[] for _ in range(bucket_count)]
   ```

   Cria uma lista de listas vazias, cada uma representando um balde.

6. **Distribuição dos elementos nos baldes**

   ```python
   for num in arr:
       idx = min((num - min_value) // bucket_size, bucket_count - 1)
       buckets[idx].append(num)
   ```

   Para cada número da lista, calcula em qual balde ele deve ser colocado e adiciona o número ao balde correspondente.

7. **Ordenação dos baldes**

   ```python
   for bucket in buckets:
       sorted_bucket = sorted(bucket, reverse=reverse)
       sorted_arr.extend(sorted_bucket)
   ```

   Cada balde é ordenado individualmente usando a função `sorted` do Python (que utiliza o TimSort).

8. **Concatenação dos baldes ordenados**
   Os elementos ordenados de cada balde são adicionados à lista final.

9. **Retorno da lista ordenada**

   ```python
   return sorted_arr
   ```

   A lista final, já ordenada, é retornada.

### Lógica por trás do algoritmo

- O Bucket Sort é eficiente para listas com valores distribuídos uniformemente, pois a distribuição nos baldes tende a ser equilibrada.
- O parâmetro `items_per_bucket` permite ajustar a quantidade de baldes, influenciando a granularidade da distribuição.
- O uso de outro algoritmo de ordenação dentro dos baldes (como o TimSort) garante que cada grupo de elementos seja ordenado corretamente antes da junção final.
- O parâmetro `reverse` permite escolher entre ordem crescente ou decrescente.

Esse método é especialmente útil para dados que já estão quase ordenados ou distribuídos de forma uniforme, tornando a ordenação mais rápida do que métodos tradicionais em alguns casos.

## Exemplo de teste de mesa

Considere a lista abaixo com 20 números inteiros:

```python
lista = [15, 3, 22, 7, 9, 1, 18, 5, 12, 6, 10, 2, 20, 8, 13, 4, 19, 11, 16, 14]
ordenada = bucket_sort(lista)
print("Lista ordenada:", ordenada)
```

### Passo a passo do algoritmo

1. **Lista original:**
   `[15, 3, 22, 7, 9, 1, 18, 5, 12, 6, 10, 2, 20, 8, 13, 4, 19, 11, 16, 14]`

2. **Valores mínimo e máximo:**
   - Mínimo: 1
   - Máximo: 22

3. **Número de baldes:**
   - `bucket_count = max(1, 20 // 5) = 4`

4. **Tamanho de cada balde:**
   - `bucket_size = max(1, (22 - 1 + 1) // 4) = 5`

5. **Distribuição nos baldes:**
   - Balde 0 (1 a 5): `[3, 1, 5, 2, 4]`
   - Balde 1 (6 a 10): `[7, 9, 6, 10, 8]`
   - Balde 2 (11 a 15): `[12, 13, 11, 14, 15]`
   - Balde 3 (16 a 22): `[18, 20, 19, 16, 22]`

6. **Ordenação dos baldes:**
   - Balde 0 ordenado: `[1, 2, 3, 4, 5]`
   - Balde 1 ordenado: `[6, 7, 8, 9, 10]`
   - Balde 2 ordenado: `[11, 12, 13, 14, 15]`
   - Balde 3 ordenado: `[16, 18, 19, 20, 22]`

7. **Concatenação dos baldes:**
   `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22]`

### Saída final

```bash
Lista ordenada: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22]
```

Esse teste de mesa mostra como os elementos são distribuídos, ordenados e concatenados pelo Bucket Sort.
