# Assembler Hack – Nand2Tetris Project 6

## Informações do Projeto

https://github.com/lwticias-lelet/assembler

**Disciplina:** Compiladores / Arquitetura de Computadores

**Projeto:** Project 6 – Hack Assembler

**Curso:** Engenharia da Computação

**Aluno:** Letícia Delfino de Araújo

**Link Youtube**

**Professor:** Sergio Souza
**Linguagem:** Python 3

---

# Descrição

Este projeto consiste na implementação de um **Assembler Hack**, responsável por traduzir programas escritos em **Assembly Hack (.asm)** para **código de máquina Hack (.hack)**.

O assembler realiza a tradução completa da linguagem Assembly utilizada na plataforma Hack do projeto Nand2Tetris, produzindo arquivos binários executáveis no CPU Emulator.

A implementação foi desenvolvida utilizando uma arquitetura modular, separando as responsabilidades entre análise do código-fonte, resolução de símbolos e geração das instruções binárias.

---

# Funcionalidades

* Tradução de instruções A (`@valor`)
* Tradução de instruções C (`dest=comp;jump`)
* Reconhecimento de Labels
* Resolução de símbolos em duas passagens
* Tratamento de variáveis
* Geração automática do arquivo `.hack`
* Compatível com os testes do Project 6

---

# Estrutura do Projeto

```text
assembler/
│
├── main.py
│
├── parser/
│   ├── __init__.py
│   └── parser.py
│
├── code/
│   ├── __init__.py
│   └── code.py
│
├── symbol_table/
│   ├── __init__.py
│   └── symbol_table.py
│
├── test_files/
│   └── project06/
│       ├── add/
│       ├── max/
│       ├── rect/
│       └── pong/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Arquitetura

O projeto é dividido em quatro módulos principais.

## Parser

Responsável por realizar a leitura do arquivo Assembly.

Funções:

* Remoção de comentários
* Remoção de linhas vazias
* Identificação do tipo de instrução
* Extração de dest, comp, jump e símbolos

---

## SymbolTable

Responsável pelo gerenciamento dos símbolos.

Funções:

* Inicialização dos símbolos predefinidos
* Registro das Labels
* Alocação automática de variáveis
* Consulta de endereços

---

## Code

Responsável por converter instruções Assembly para código binário.

Utiliza tabelas para:

* comp
* dest
* jump

---

## Main

Coordena toda a tradução.

Fluxo:

1. Primeira passagem

   * encontra Labels
   * salva seus endereços

2. Segunda passagem

   * resolve símbolos
   * traduz todas as instruções
   * gera o arquivo `.hack`

---

# Como executar

Abra o terminal na pasta do projeto.

Execute:

```bash
python main.py caminho/do/arquivo.asm
```

Exemplo:

```bash
python main.py test_files/project06/add/Add.asm
```

Será gerado:

```text
Add.hack
```

na mesma pasta do arquivo de entrada.

---

# Testes

Os testes utilizados são os disponibilizados pelo Project 6 do Nand2Tetris.

Estrutura:

```text
test_files/
└── project06/
    ├── add/
    ├── max/
    ├── rect/
    └── pong/
```

Testes recomendados:

* Add.asm
* Max.asm
* MaxL.asm
* Rect.asm
* RectL.asm
* Pong.asm
* PongL.asm

Após gerar o arquivo `.hack`, basta carregá-lo no CPU Emulator para verificar sua execução.

---

# Exemplo

Entrada:

```asm
@2
D=A
@3
D=D+A
@0
M=D
```

Saída:

```text
0000000000000010
1110110000010000
0000000000000011
1110000010010000
0000000000000000
1110001100001000
```

---

# Tecnologias Utilizadas

* Python 3
* Biblioteca padrão do Python

---

# Compilação

Não é necessária instalação de bibliotecas externas.

---

---

# Autor

Letícia Delfino de Araújo

Engenharia da Computação

---

# Licença

Projeto desenvolvido exclusivamente para fins acadêmicos na disciplina de Compiladores / Arquitetura de Computadores.
