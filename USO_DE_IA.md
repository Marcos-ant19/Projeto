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

### Cauã Azevedo Santos

A utilização de inteligência artificial durante o meu desenvolvimento no trabalho ocorreu nas seguintes etapas:

1. **Planejamento e Direcionamento Inicial:** A IA foi utilizada para dar um rumo inicial sobre o que o trabalho exigia e também para auxiliar na separação das tarefas e do que cada integrante da equipe deveria fazer.
2. **Estudo da Base Teórica:** Usei a IA para estudar e compreender melhor a base teórica e os conceitos do projeto.
3. **Pesquisa de Referências:** Embora o professor já tivesse deixado sugestões de referências, foi necessário buscar mais materiais para fortalecer a argumentação. Utilizei o **Claude** para pesquisar e encontrar mais 5 referências concretas (as quais foram posteriormente verificadas por mim).
4. **Análise de Citações e Documentos:** Com as novas referências em mãos, utilizei o **NotebookLM** para estudar os documentos e planejar o que poderia ser efetivamente citado no relatório.
5. **Escrita do Relatório:** Quando meus tokens do Claude acabaram e faltava apenas a etapa de escrita, utilizei a IDE agêntica do Google (**Antigravity**), configurada com o modelo da Anthropic. Nela, utilizei skills de escrita e inseri as referências em um arquivo `.md`. Criei regras e um fluxo rigoroso para que a IA utilizasse **somente** as referências que eu havia fornecido. Passei todo o contexto do trabalho e do diretório em que eu estava operando, delimitando ao máximo o escopo. Assim, a escrita foi dividida seção por seção, sendo que em cada etapa eu fui revisando e ajustando manualmente certos pontos gerados.

#### Exemplos de prompts utilizados por Cauã

**Prompt 1 (Roteiro Inicial de Estudos):**

> **Contexto:**
> Tenho um trabalho acadêmico/técnico extenso envolvendo CUDA e não sei por onde começar.
> 
> **O que preciso:**
> - Uma explicação introdutória sobre o que é CUDA, o que é, para que serve e por que é relevante
> - Um roteiro estruturado de estudos, do básico ao necessário para executar o trabalho
> - Um plano de ação claro, com etapas sequenciais e priorizadas para eu não me perder
> 
> **Meu nível atual:**
> Sou iniciante no assunto, nunca estudei CUDA antes e ainda preciso entender o escopo completo do trabalho. E sei um pouco de C.
> 
> **O que espero como resposta:**
> - Uma trilha de aprendizado lógica e progressiva
> - Indicação do que estudar primeiro, segundo e assim por diante
> - Dicas de onde encontrar recursos confiáveis (documentação, tutoriais, etc.)
> - Alertas sobre os pontos mais difíceis ou que exigem mais atenção
> 
> ⚠️ Assim que eu compartilhar o enunciado do trabalho, me ajude também a identificar exatamente o que ele está pedindo e como mapear isso ao que estudei.

**Prompt 2 (Instrução para Agente de IA - Escrita do Artigo):**

> # Instruções para o Agente de IA: Escrita do Artigo Científico (SBC)
> 
> Você é um agente de IA atuando como pesquisador e coautor encarregado de escrever um artigo científico rigoroso sobre "Força bruta de hash criptográfico (SHA-256)" acelerado por GPU (CUDA). O artigo é o Trabalho Final da disciplina de Arquitetura de Computadores.
> 
> ## Seu Objetivo
> Seu principal objetivo é redigir o artigo acadêmico diretamente no arquivo LaTeX `main.tex` que se encontra dentro da pasta `Overleaf`, seguindo rigorosamente a formatação do template da Sociedade Brasileira de Computação (SBC).
> 
> ## Contexto do Trabalho
> - **Disciplina:** Arquitetura de Computadores.
> - **Tema (Trio 6):** Força bruta de hash criptográfico (SHA-256). Implementação de busca por força bruta de pré-imagens curtas (4–6 caracteres) para SHA-256 em CPU (sequencial) e CUDA (paralelo).
> - **Objetivos Chave:** Demonstrar como o modelo SIMT (Single Instruction, Multiple Threads) favorece a exploração massiva de espaços de busca; calcular speedup, eficiência; comparar desempenho; discutir restrições éticas e implicações de segurança.
> - **Autores/Integrantes:** Cauã Azevedo Santos, Jurcelino Castilho dos Santos Neto, Marcos Antonio do Nascimento.
> 
> ## Seu Workflow (Como você deve proceder)
> 
> 1. **Análise de Referências e Literatura:**
>    - Leia os arquivos de referências no diretório raiz (ex: `referencias_grupo6.md` e/ou `referencias_grupo6_v2.md`).
>    - **REGRA DE OURO:** Baseie a fundamentação teórica e trabalhos relacionados **exclusivamente** nesses arquivos. Não adicione citações ou referências não fornecidas. Isso é crucial para evitar alucinações.
> 
> 2. **Análise do Código e Resultados (Obrigatório e Fundamental):**
>    - Inspecione detalhadamente a pasta `projeto_new`. É lá que se encontra todo o nosso código (CPU e CUDA), scripts, e principalmente os **resultados dos benchmarks e gráficos**.
>    - Ao escrever o artigo, você **deve referenciar e basear a discussão nestes arquivos reais**. A seção de *Metodologia*, *Implementação* e *Resultados e Discussão* precisa ser fortemente embasada no que foi de fato executado.
> 
> 3. **Escrita no Overleaf:**
>    - Acesse o diretório `Overleaf` e escreva o conteúdo no arquivo `main.tex`.
>    - Utilize a skill humanizer.
> 
> ## Estrutura Exigida do Relatório (Template SBC)
> O seu texto final em `main.tex` deve contemplar obrigatoriamente as seguintes seções:
> 1. **Resumo / Abstract:** (Português e Inglês, máx. 150 palavras cada).
> 2. **Introdução:** Contexto, motivação, problema, objetivos e organização do texto.
> 3. **Fundamentação Teórica:** Paralelismo (taxonomia de Flynn), arquitetura SIMT, hierarquia de memória em GPUs, CUDA (threads/blocos/grids), Lei de Amdahl/Gustafson e criptografia/SHA-256.
> 4. **Trabalhos Relacionados:** Usar estritamente o conteúdo dos arquivos de referências.
> 5. **Metodologia:** Descrição do problema, ambiente experimental (Google Colab), métricas, configurações (blocos/threads), tamanhos de entrada.
> 6. **Implementação:** Trechos comentados das kernels, decisões de projeto, otimizações aplicadas. Descrever a versão CPU e a versão CUDA. (Pegue os dados da pasta `projeto_new`).
> 7. **Resultados e Discussão:** Gráficos e tabelas comparando tempo CPU vs GPU, speedup e eficiência, análise de gargalos. Relacionar teoria e prática. (Use os dados empíricos de `projeto_new`).
> 8. **Conclusões e Trabalhos Futuros:** Resumo dos achados e considerações éticas/de segurança.
> 9. **Referências:** Referenciar os materiais lidos.
> 
> ## Restrições Críticas
> - **NÃO ALUCINE RESULTADOS.** Use apenas os dados da pasta `projeto_new`.
> - **NÃO ALUCINE REFERÊNCIAS.** Use apenas o que foi fornecido nos arquivos `referencias_grupo6`.
> - Foque na escrita do documento LaTeX (`main.tex`). Use formatação correta para tabelas, equações e imagens no LaTeX.
> - **TRADUÇÃO DE CITAÇÕES:** Sempre que citar trechos extraídos das referências em inglês, traduza-os de forma clara e acadêmica para o português no texto do artigo. Não mantenha citações diretas em inglês no meio do texto em português.
> 
> ## ORÇAMENTO DE PÁGINAS (CRÍTICO)
> - **LIMITE TOTAL:** 10 páginas. Sem exceção.
> - **Páginas já consumidas:** ~6 páginas (Resumo/Abstract + Introdução + Fundamentação Teórica + Trabalhos Relacionados).
> - **Páginas restantes:** ~4 páginas para Metodologia + Implementação + Resultados e Discussão + Conclusões + Referências.
> - **REGRA:** Cada seção restante deve ocupar no máximo 1 página. A seção de Referências ocupa cerca de 0,5 página.
> - **COMO ECONOMIZAR ESPAÇO:** Prefira tabelas compactas a parágrafos descritivos. Não repita informações já ditas na Fundamentação. Elimine frases introdutórias genéricas. Vá direto ao ponto. Use `\small` em tabelas e listagens de código se necessário.
> - **PROIBIDO:** Ultrapassar 10 páginas. Se o texto estiver chegando perto do limite, corte explicações secundárias e mantenha apenas dados, métricas e análise.

#### Análise Crítica

No geral, a IA funcionou bem. Dar bastante contexto nos prompts e delimitar o escopo fez com que as respostas viessem mais precisas, quando eu era vago, a resposta vinha genérica. Usar *skills* de escrita na IDE também ajudou a manter o texto dentro do que eu queria, sem a IA inventar referência.

Um ponto que ficou claro: a IA acelera o trabalho, mas só se você já sabe o que quer. Eu tive que revisar e ajustar cada seção que ela gerou. Se alguém só joga o enunciado no chat e aceita tudo sem ler, o resultado sai fraco e a pessoa não aprende nada no processo.

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

A resposta funcionou direto — colei as substituições no código e rodou no Colab sem problemas.
