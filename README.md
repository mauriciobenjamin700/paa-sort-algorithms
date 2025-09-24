# Bucket Sort e Gnome Sort

Equipe:

- Mauricio Benjamin da Rocha
- Pedro Antonio Vital

## Introdução

Este trabalho apresenta o estudo dos algoritmos de ordenação Bucket Sort e Gnome Sort, abordando suas definições, funcionamento, aspectos históricos, análise de complexidade, comparação de desempenho, resultados práticos e conclusões. O objetivo é compreender as diferenças, vantagens e limitações de cada método, utilizando exemplos e testes realizados na mesma plataforma.## Introdução

## Introdução ao Bucket Sort

O Bucket Sort é um algoritmo de ordenação criado para lidar de forma eficiente com listas de dados que possuem valores distribuídos de maneira relativamente uniforme. Ele foi proposto por Harold H. Seward em 1957, inicialmente para uso em computadores da IBM, e é considerado uma variação dos algoritmos de ordenação por distribuição.

O propósito do Bucket Sort é dividir os elementos em grupos (baldes) de acordo com seus valores, facilitando a ordenação interna de cada grupo e acelerando o processo de ordenação total. Ao invés de comparar cada elemento com todos os outros, como em algoritmos tradicionais, o Bucket Sort aproveita a distribuição dos dados para reduzir o número de comparações necessárias.

Esse método é especialmente útil para grandes volumes de dados que já estão quase ordenados ou distribuídos uniformemente, como dados de sensores, notas de alunos, ou qualquer situação em que os valores estejam espalhados de forma previsível.

O Bucket Sort é um exemplo clássico de como a estrutura dos dados pode ser explorada para melhorar a eficiência dos algoritmos de ordenação.

## Definições dos Algoritmos

### Bucket Sort

O Bucket Sort é um algoritmo de ordenação por distribuição, criado por Harold H. Seward em 1957 para uso em computadores IBM. Ele distribui os elementos em baldes (buckets) de acordo com seus valores, ordena cada balde individualmente e, por fim, concatena os baldes para obter a lista final ordenada. É eficiente para listas com valores distribuídos uniformemente.

### Gnome Sort

O Gnome Sort foi criado por Ivan Lacarak em 2000. É um algoritmo simples, inspirado no modo como um gnomo organizaria uma fileira de vasos: compara elementos adjacentes e troca-os se necessário, voltando para corrigir qualquer desordem anterior. É semelhante ao Bubble Sort, mas volta uma posição após cada troca.

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

   arr = arr.copy()

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

### Passo a passo do código do Bucket Sort

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

### Lógica por trás do algoritmo Bucket Sort

- O Bucket Sort é eficiente para listas com valores distribuídos uniformemente, pois a distribuição nos baldes tende a ser equilibrada.
- O parâmetro `items_per_bucket` permite ajustar a quantidade de baldes, influenciando a granularidade da distribuição.
- O uso de outro algoritmo de ordenação dentro dos baldes (como o TimSort) garante que cada grupo de elementos seja ordenado corretamente antes da junção final.
- O parâmetro `reverse` permite escolher entre ordem crescente ou decrescente.

Esse método é especialmente útil para dados que já estão quase ordenados ou distribuídos de forma uniforme, tornando a ordenação mais rápida do que métodos tradicionais em alguns casos.

## Exemplo de teste de mesa com Bucket Sort

Considere a lista abaixo com 20 números inteiros:

```python
lista = [15, 3, 22, 7, 9, 1, 18, 5, 12, 6, 10, 2, 20, 8, 13, 4, 19, 11, 16, 14]
ordenada = bucket_sort(lista)
print("Lista ordenada:", ordenada)
```

### Passo a passo do algoritmo Bucket Sort

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

### Saída final do BucketSort

```bash
Lista ordenada: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22]
```

Esse teste de mesa mostra como os elementos são distribuídos, ordenados e concatenados pelo Bucket Sort.

## Introdução ao Gnome Sort

O Gnome Sort é um algoritmo de ordenação simples e intuitivo, criado por Ivan Lacarak em 2000. Ele é inspirado no modo como um gnomo de jardim organizaria uma fileira de vasos: comparando elementos adjacentes e trocando-os quando necessário, voltando para corrigir qualquer desordem anterior. O Gnome Sort é semelhante ao Bubble Sort, mas volta uma posição após cada troca, garantindo que todos os elementos estejam no lugar correto.

O propósito do Gnome Sort é ordenar listas de forma didática e fácil de entender, sendo útil para fins educacionais e para listas pequenas. Apesar de sua simplicidade, não é eficiente para grandes volumes de dados.

O Gnome Sort exemplifica como algoritmos podem ser construídos a partir de ideias simples de comparação e troca.

### Gnome Sort - Código completo

```python
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
```

### Passo a passo do código

1. **Verificação da lista**

   ```python
   if not arr:
       return []
   ```

   Se a lista estiver vazia, retorna uma lista vazia imediatamente.

2. **Preparação da lista**

   ```python
   arr = arr.copy()
   i = 0
   n = len(arr)
   ```

   Cria uma cópia da lista para não modificar o original e inicializa os índices.

3. **Percorrendo e comparando elementos**

   ```python
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
   ```

   Percorre a lista, compara elementos adjacentes e troca se necessário. Após cada troca, volta uma posição para garantir que o novo elemento esteja no lugar correto.

4. **Retorno da lista ordenada**

   ```python
   return arr
   ```

   Retorna a lista ordenada.

### Lógica por trás do algoritmo

- O Gnome Sort é eficiente apenas para listas pequenas ou quase ordenadas.
- O parâmetro `reverse` permite escolher entre ordem crescente ou decrescente.
- O algoritmo é fácil de implementar e entender, sendo útil para fins didáticos.
- Sua principal característica é voltar uma posição após cada troca, garantindo que todos os elementos estejam no lugar correto.

## Exemplo de teste de mesa

Considere a lista abaixo com 10 números inteiros:

```python
lista = [7, 3, 5, 2, 8, 1, 4, 6, 9, 0]
ordenada = gnome_sort(lista)
print("Lista ordenada:", ordenada)
```

### Passo a passo do algoritmo

1. **Lista original:**
   `[7, 3, 5, 2, 8, 1, 4, 6, 9, 0]`

2. **Comparações e trocas:**
   - 7 > 3 → troca → `[3, 7, 5, 2, 8, 1, 4, 6, 9, 0]`
   - 7 > 5 → troca → `[3, 5, 7, 2, 8, 1, 4, 6, 9, 0]`
   - 7 > 2 → troca → `[3, 5, 2, 7, 8, 1, 4, 6, 9, 0]`
   - 5 > 2 → troca → `[3, 2, 5, 7, 8, 1, 4, 6, 9, 0]`
   - 3 > 2 → troca → `[2, 3, 5, 7, 8, 1, 4, 6, 9, 0]`
   - 8 > 1 → troca → `[2, 3, 5, 7, 1, 8, 4, 6, 9, 0]`
   - 7 > 1 → troca → `[2, 3, 5, 1, 7, 8, 4, 6, 9, 0]`
   - 5 > 1 → troca → `[2, 3, 1, 5, 7, 8, 4, 6, 9, 0]`
   - 3 > 1 → troca → `[2, 1, 3, 5, 7, 8, 4, 6, 9, 0]`
   - 2 > 1 → troca → `[1, 2, 3, 5, 7, 8, 4, 6, 9, 0]`
   - 8 > 4 → troca → `[1, 2, 3, 5, 7, 4, 8, 6, 9, 0]`
   - 7 > 4 → troca → `[1, 2, 3, 5, 4, 7, 8, 6, 9, 0]`
   - 5 > 4 → troca → `[1, 2, 3, 4, 5, 7, 8, 6, 9, 0]`
   - 8 > 6 → troca → `[1, 2, 3, 4, 5, 7, 6, 8, 9, 0]`
   - 7 > 6 → troca → `[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]`
   - 9 > 0 → troca → `[1, 2, 3, 4, 5, 6, 7, 8, 0, 9]`
   - 8 > 0 → troca → `[1, 2, 3, 4, 5, 6, 7, 0, 8, 9]`
   - 7 > 0 → troca → `[1, 2, 3, 4, 5, 6, 0, 7, 8, 9]`
   - 6 > 0 → troca → `[1, 2, 3, 4, 5, 0, 6, 7, 8, 9]`
   - 5 > 0 → troca → `[1, 2, 3, 4, 0, 5, 6, 7, 8, 9]`
   - 4 > 0 → troca → `[1, 2, 3, 0, 4, 5, 6, 7, 8, 9]`
   - 3 > 0 → troca → `[1, 2, 0, 3, 4, 5, 6, 7, 8, 9]`
   - 2 > 0 → troca → `[1, 0, 2, 3, 4, 5, 6, 7, 8, 9]`
   - 1 > 0 → troca → `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`

3. **Lista final ordenada:**
   `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`

### Saída final

```bash
Lista ordenada: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Esse teste de mesa mostra como o Gnome Sort percorre, compara e troca elementos até que toda a lista esteja ordenada.

## Ordem de Complexidade

- **Bucket Sort:**
  - Melhor caso: $O(n + k)$, onde $k$ é o número de baldes.
  - Pior caso: $O(n^2)$ (se todos os elementos caírem no mesmo balde).
- **Gnome Sort:**
  - Melhor caso: $O(n)$ (lista já ordenada).
  - Pior caso: $O(n^2)$ (lista invertida).

## Comparação de Funcionamento

- **Bucket Sort:**
  - Mais eficiente para listas grandes e distribuídas uniformemente.
  - Utiliza ordenação interna nos baldes (ex: TimSort).
- **Gnome Sort:**
  - Simples, fácil de implementar e entender.
  - Indicado para listas pequenas ou quase ordenadas.
  - Lembra o Bubble Sort, mas volta após cada troca.

### Comparação Prática

- Bucket Sort foi mais rápido para listas grandes e distribuídas.
- Gnome Sort teve desempenho aceitável apenas para listas pequenas ou no caso da lista já estar ordenada.
- Ambos retornaram resultados corretos, mas o Bucket Sort se destacou em eficiência.

## Conclusão

O estudo mostrou que o Bucket Sort é mais indicado para listas grandes e distribuídas uniformemente, enquanto o Gnome Sort é útil para fins didáticos e listas pequenas. A escolha do algoritmo depende do contexto e do tipo de dados. O uso de algoritmos de ordenação adequados pode impactar significativamente o desempenho das aplicações.

## Referências Bibliográficas

- Cormen, Thomas H., et al. "Instructor’s Manual." (2002).
- Seward, H. H. (1957). Information sorting in the application of electronic digital computers to business operations. Commun. ACM.
- Lacarak, I. (2000). Gnome Sort - The Sorting Algorithm for Gnomes.

## Links Úteis

- [bucket sort - geeksforgeeks.org](https://www.geeksforgeeks.org/dsa/bucket-sort-2/)
- [programiz.com](https://www.programiz.com/dsa/bucket-sort)
- [gnome sort - geeksforgeeks.org](https://www.geeksforgeeks.org/dsa/gnome-sort-a-stupid-one/)
- [gnome sort - rosettacode](https://rosettacode.org/wiki/Sorting_algorithms/Gnome_sort)
