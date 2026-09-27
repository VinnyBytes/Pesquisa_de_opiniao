# 📋Pesquisa de Opinião

Programa de linha de comando em Python que coleta avaliações sobre o atendimento da empresa fictícia TudoWeb. Ele entrevista 50 pessoas, conta as respostas de cada categoria e apresenta um resumo ao final.

## 📌Requisitos

- Python 3 instalado.
- Nenhuma biblioteca externa é necessária.

## 📌Como executar

Abra um terminal na pasta do projeto e execute:

```powershell
python app.py
```

No Windows, também é possível usar o inicializador `py`:

```powershell
py app.py
```

O programa é interativo: depois de iniciar, responda às perguntas no terminal. Cada entrevista solicita nome, idade e uma avaliação:

| Opção | Avaliação |
| --- | --- |
| 1 | EXCELENTE |
| 2 | BOM |
| 3 | RUIM |

## 📌Como o código funciona

### 1. Inicializa os contadores

As variáveis `quantidade_excelente`, `quantidade_bom` e `quantidade_ruim` começam em zero. Cada uma guarda quantas vezes aquela avaliação foi escolhida.

### 2. Repete a entrevista 50 vezes

O laço `for` controla a quantidade de entrevistas:

```python
for numero_entrevistado in range(1, 51):
```

Em Python, o limite final de `range` não é incluído. Por isso, `range(1, 51)` gera os números de 1 a 50. A cada repetição, o programa pede o nome e a idade da pessoa.

### 3. Lê e valida a avaliação

O laço `while True` mantém a pergunta ativa até receber uma opção válida. A função `input` lê o que foi digitado como texto, e `int` tenta convertê-lo para um número inteiro.

O bloco `try/except` trata o caso em que a conversão falha, como quando alguém digita letras. Se o valor for numérico, a condição `opiniao in (1, 2, 3)` verifica se ele corresponde a uma das opções aceitas. Uma opção inválida faz o programa exibir um aviso e perguntar novamente.

### 4. Atualiza a categoria escolhida

As estruturas `if` e `elif` escolhem qual contador atualizar:

```python
if opiniao == 1:
	quantidade_excelente += 1
elif opiniao == 2:
	quantidade_bom += 1
elif opiniao == 3:
	quantidade_ruim += 1
```

O operador `+= 1` soma uma unidade ao contador correspondente. Como a avaliação já foi validada, somente uma das três categorias é contada por entrevista.

### 5. Exibe o resumo

Depois da quinquagésima entrevista, o programa mostra os totais de EXCELENTE, BOM e RUIM. Por exemplo, uma pesquisa fictícia poderia terminar assim:

```text
--- Resultado da pesquisa ---
Respostas EXCELENTE: 20
Respostas BOM: 18
Respostas RUIM: 12
```

❗ Os números acima são apenas um exemplo; os totais reais dependem das respostas digitadas e somam 50.

## 📌O que o programa guarda

Nome e idade são solicitados e usados na mensagem de confirmação de cada entrevista, mas não aparecem no resumo final. A idade é lida como texto e não passa por validação numérica. As respostas e os totais ficam apenas na memória durante a execução; ao fechar o programa, eles não são salvos em arquivo ou banco de dados.
