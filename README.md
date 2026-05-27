# Busca por Força Bruta de Pré-imagens Curtas para SHA-256 Utilizando CPU e CUDA

## Descrição 

Este projeto tem como ideia apresentar a análise de uma busca por força de pré-imagens curtas utilizando o algoritmo criptográfico SHA-256 em duas abordagens distintas

- Execução sequencial em CPU;
- Execução paralela utilizando CUDA em GPU.

O objetivo principal e mostrar a diferença de execução entre a utilização sequencial e paralela.

O projeto foi desenvolvido utilizando Google Colab com suporte a GPU NVIDIA Tesla T4.

## Objetivos do projeto

- Implementar SHA-256 em CPU e CUDA;
- Realizar busca por força bruta de senhas curtas (4-6 caracteres);
- Demonstrar o impacto do paralelismo massivo em problemas computacionalmente intensivos;
- Produzir benchmarks, gráficos e métricas de desempenho;

## Tecnologias Utilizadas

### Linguagens

- Python
- CUDA C

### Ferramentas

- Google Colab
- NVIDIA CUDA Toolkit
- GitHub
- Visual Studio Code

### Bibliotecas Python

- Pandas
- Matplotlib

---

## Execução no Google Colab

### Abrir Notebook

## Abrir no Google Colab

[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Marcos-ant19/Projeto/blob/main/codigo/cpu&gpu.ipynb)
---

## Configuração do Ambiente

Antes da execução:

1. Abrir o notebook no Google Colab;
2. Ativar aceleração por GPU:

```text
Ambiente de execução
→ Alterar tipo de ambiente de execução
→ GPU
```

## Compilação do Código CUDA

O notebook realiza automaticamente:

```bash
!nvcc -Wno-deprecated-gpu-targets sha256_cpu_cuda.cu -o programa
```

---

## Execução

Após compilar:

```bash
!./programa
```

O usuário deverá informar uma senha de 4 a 6 caracteres utilizando:

```text
abcdefghijklmnopqrstuvwxyz0123456789.
```
## Funcionamento do Programa

O sistema:

1. Recebe uma senha;
2. Gera automaticamente o hash SHA-256;
3. Executa busca por força bruta na CPU;
4. Executa busca por força bruta na CUDA;
5. Compara os tempos de execução;
6. Exibe:
   - senha encontrada;
   - quantidade de tentativas;
   - tempo CPU;
   - tempo CUDA.

---
## Benchmarks Obtidos

Os experimentos demonstraram ganhos expressivos utilizando CUDA.

### Tempo Médio Obtido

| Implementação | Tempo Médio |
|---|---|
| CPU | 2.96 s |
| CUDA | 0.0058 s |

---

## Speedup Médio

```text
≈ 501x mais rápido utilizando CUDA
```

---

## Resultados

Resultado obtidos:

- [Benchmark CPU vs CUDA](./resultados/benchmark_cpu_cuda_sha256.png)
- [Gráfico de Speedup](./resultados/speedup_cpu_cuda_sha256.png)
- [Tabela CSV com os resultados](./resultados/benchmark_resultados.csv)

---

## Modelo SIMT

O modelo SIMT (*Single Instruction Multiple Threads*) utilizado pelas GPUs permite que milhares de threads executem simultaneamente a mesma instrução sobre diferentes dados.

Esse comportamento favorece aplicações altamente paralelizáveis, como força bruta criptográfica, reduzindo drasticamente o tempo necessário para explorar grandes espaços de busca.

---

## Complexidade do Problema

O crescimento do espaço de busca é exponencial:

```text
36^4 = 1.679.616 combinações
36^5 = 60.466.176 combinações
36^6 = 2.176.782.336 combinações
```

Isso mostra que cada vez que aumenta fica ainda mais inviavel utilizar método sequencial.

---
## Considerações Finais

Os resultado obtidos demonstram claramente o impacto do paralelismo massivo proporcionado por GPUs em problemas computacionalmente intensivos.

A implementação em CUDA apresentou ganhos extremamente significativos em relação à abordagem sequencial em CPU, reforçando a eficiência do modelo SIMT para aplicações de exploração massiva de espaços de busca
---

## Integrantes 

- Marcos Antônio do Nascimento
- Cauã Azevedo Santos
- Jurcelino Castilho dos Santos Neto

## Contatos

Email: marco.nascimento1@estudante.ifgoiano.edu.br  
Email: caua.azevedo@estudante.ifgoiano.edu.br  
Email: jurcelino.santos@estudante.ifgoiano.edu.br  

