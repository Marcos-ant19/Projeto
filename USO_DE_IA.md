# Uso de Inteligência Artificial

 A utlização da IA foi fundamnetal para o apredizando e como uma ferramneta ajudando a auxiliar em diferentes áreas deste projeto.

 ---

## Ferramnetas utilizadas

- ChatGPT (OpenAI)
- Claude AI

## Etapas do uso da IA

- Primeiramente utilizei a IA para apredizando inicial para entender o contéudo proposto no trabalho
- Utilizei para geração do código
- Explicação do código e correção do próprio
- Utilizei para ajudar na criação do benchmarks para geração dos gráficos
- Utilizei para criação do repósitorio no github

## Exemplos de prompts utilizandos

### prompt 1

"Por favor gere um código em CUDA C/C++ para Google Colab sobre busca por força bruta utilizando SHA-256, sendo fiel ao trabalho acadêmico. O código deve receber uma senha de 4 a 6 caracteres, gerar o hash SHA-256, testar combinações utilizando letras minúsculas e números, executar uma versão sequencial em CPU e uma versão paralela em GPU CUDA, comparar os hashes, medir o tempo de execução da CPU e da GPU, e imprimir tentativas, senha encontrada e speedup."

### Resposta obtida

A IA gerou o código normalmente conforme escrito, e explicou como funcionava o programa.

### Análise crítica 

A resposta foi útil e aproveitada, porém algumas partes não conforme havia pedido de primeiro momomento sendo assim eu reaproveitei o código e pedi para corrigir conforme necessário.

--- 

### prompt 2

"o que é SHA-256?"

### Resposta obtida

A resposta obtida foi uma explicação geral do que o SHA-256 e qual a importancia dessa criptografia dentro da lógica do projeto

### Análise crítica 

A respota obtida foi satisfatória sendo precisamente acertiva por parte da IA utilizada.

## Reflexão de cada integrante

### Marcos antônio do nascimento

Sinto que a utilização da IA foi benéfica por auxiliar tanto no aprendizado quanto como um auxiliador durante todo o desenvolvimento do projeto, levando em consideração que toda a utilização sempre foi para aprimorar conhecimentos intelectual e técnico.

### Jurcelino Castilho Dos Santos Neto

A utilização da ia foi benéficiente, ajudando a corrigir os erros cometidos por mim, porém por uma parte foi mais prolongada por não ter gerado um codigo completo, sendo assim tive que corrigir cerca de 55% manualmente, mais ajudou a chegar no exato da execução.

### Cauã

---

# Uso de Inteligência Artificial

o uso da IA foi em questão para auxilio, foi utilizada para auxiliar e corrigir codigos da CUDA.

## Ferramentas utilizadas

- NotebookLM
- ChatGPT (pro)

## Etapas do uso da IA

- Primeiramente utilizei a IA para apredizando inicial para entender o contéudo proposto no trabalho
- Utilizei para geração do código
- Explicação do código e correção do próprio
- Utilizei para ajudar na criação dos gráficos da gpu

## Exemplos de prompts utilizandos

### prompt 1

"Aja como um especialista em programação massivamente paralela e escreva um código em C/CUDA para um motor de busca por força bruta de hashes SHA-256, seguindo rigorosamente as definições do relatório técnico 'Otimização da Busca por Força Bruta de Pré-Imagens'. O código deve ser compatível com o Google Colab"

### Resposta obtida

"Para implementar o SHA-256 em CUDA no Google Colab seguindo as fases de estrutura solicitadas, é necessário transformar as funções sequenciais do algoritmo em funções de dispositivo (__device__) e gerenciar a execução massivamente paralela através do kernel." Logo em seguida me gerou um codigo incompleto.

### Análise crítica 

A resposta foi útil e aproveitada, porém o codigo havia gerado incompleto, então diante daquilo tive que pedir informações e ajuda ao ChatGPT na versão PRO para me auxiliar na construção do codigo, e fiz 55% manualmente.

### prompt 2

"Com base na estrutura de código definida anteriormente, aplique as seguintes especificações detalhadas:
Definição do Charset: Utilize exatamente a chave const char charset[] = "abcdefghijklmnopqrstuvwxyz0123456789"; (36 caracteres) para a busca:
 - Otimização de Memória: Declare este charset utilizando o especificador __constant__ da GPU. Conforme as boas práticas acadêmicas de CUDA, isso garante que o acesso aos caracteres seja feito via cache de constante, otimizando o broadcast para todas as threads de um warp que estão gerando candidatos simultaneamente.
-  Lógica de Geração de Senhas: Implemente a função de dispositivo password_generator de modo que ela converta o índice global da thread em uma string baseada na base 36 (tamanho do seu charset). Garanta que a função trate corretamente o mapeamento para comprimentos de 4 a 6 caracteres.
 - Sincronização de Símbolos: No código do Host (CPU), utilize a função cudaMemcpyToSymbol para copiar o charset definido na CPU para a memória constante da GPU antes do lançamento do kernel.
- Critério de Sucesso: O código deve imprimir a senha encontrada e o hash original no console assim que a found_flag for ativada por qualquer thread."

### Resposta obtida

A IA me deu uma linha de substituição onde eu apenas tive que trocar dentro do meu proprio codigo.

### Análise crítica 

A respota obtida foi acertada e utilizada no google colab sendo precisamente acertiva por parte da IA utilizada.
