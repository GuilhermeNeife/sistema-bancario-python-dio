# 🏦 Sistema Bancário com Python

## 📌 Sobre o Projeto

Este projeto foi desenvolvido como parte do desafio **"Criando um Sistema Bancário com Python"**, da formação **Coding Future Vivo — Python AI Backend Developer**, oferecida pela [Digital Innovation One (DIO)](https://www.dio.me/).

O objetivo é simular operações bancárias básicas utilizando os fundamentos da linguagem Python, aplicando estruturas condicionais, laços de repetição, operadores e manipulação de variáveis.

Além dos requisitos propostos, implementei melhorias na interface do terminal para proporcionar uma experiência mais organizada e intuitiva ao usuário.

## 🚀 Funcionalidades

### 💰 Depósito

* Permite realizar depósitos de valores positivos.
* Atualiza automaticamente o saldo disponível.
* Registra todas as operações no extrato.
* Impede depósitos com valores inválidos.

### 💸 Saque

* Limite máximo de **R\$ 500,00 por operação**.
* Permite até **3 saques por execução**.
* Verifica a disponibilidade de saldo.
* Impede saques com valores negativos ou zerados.
* Registra os saques realizados no extrato.

### 📄 Extrato

* Exibe o histórico de depósitos e saques.
* Apresenta o saldo atualizado da conta.
* Informa quando não existem movimentações registradas.

### 🖥️ Interface de Terminal

* Menu interativo com opções de navegação.
* Limpeza automática da tela entre operações.
* Exibição do saldo e da quantidade de saques disponíveis.
* Mensagens de confirmação e erro.
* Tratamento de entradas inválidas utilizando `<span>try/except</span>`.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Visual Studio Code**
* **Git**
* **GitHub**

### Conceitos aplicados

* Variáveis e tipos de dados
* Estruturas condicionais (`<span>if</span>`, `<span>elif</span>`, `<span>else</span>`)
* Estruturas de repetição (`<span>while</span>`)
* Operadores aritméticos e lógicos
* Manipulação e formatação de strings
* Tratamento de exceções (`<span>try/except</span>`)
* Entrada e saída de dados
* Importação de módulos da biblioteca padrão

## 📂 Estrutura do Projeto

```
sistema-bancario-python-dio/
│
├── desafio.py       # Código principal do sistema
├── README.md        # Documentação do projeto
└── .gitignore       # Arquivos ignorados pelo Git
```

## ▶️ Como Executar

**1. Clone o repositório:**

```
git clone https://github.com/SEU-USUARIO/sistema-bancario-python-dio.git
```

**2. Acesse a pasta do projeto:**

```
cd sistema-bancario-python-dio
```

**3. Execute o programa:**

```
python desafio.py
```

> É necessário ter o Python 3 instalado. O projeto não exige bibliotecas externas.

## 💻 Exemplo de Utilização

```
==========================================
              BANCO PYTHON
==========================================

  SALDO DISPONIVEL
  R$ 1500.00

  Saques disponiveis: 3 de 3

==========================================
              MENU PRINCIPAL
==========================================

  [D] Depositar
  [S] Sacar
  [E] Consultar extrato
  [Q] Sair

==========================================

=> Selecione uma operacao:
```

O usuário pode realizar operações sucessivas, consultar o histórico de movimentações e encerrar o sistema selecionando a opção `<span>Q</span>`.

## 📋 Regras de Negócio


| Operação           | Regra                                         |
| -------------------- | --------------------------------------------- |
| Depósito            | Apenas valores positivos                      |
| Saque                | Máximo de R\$ 500,00 por operação          |
| Quantidade de saques | Até 3 por execução                         |
| Saldo                | Não permite saques superiores ao disponível |
| Extrato              | Registra depósitos e saques realizados       |
| Conta bancária      | Usuário único nesta versão                 |

**Observação:** esta é uma versão inicial de caráter educacional. Os dados são mantidos em memória durante a execução e não são persistidos após o encerramento do programa.

## 🔮 Possíveis Melhorias Futuras

* [ ]  Cadastro de usuários e contas bancárias
* [ ]  Persistência de dados em banco de dados
* [ ]  Histórico de transações com data e hora
* [ ]  Controle de limite diário com reinicialização por data
* [ ]  Interface gráfica
* [ ]  Implementação de programação orientada a objetos
* [ ]  Testes automatizados

## 🎯 Aprendizados

O desenvolvimento deste projeto permitiu consolidar conhecimentos fundamentais de Python, especialmente na construção de fluxos condicionais, validação de dados e controle de operações financeiras.

A personalização da interface também proporcionou a oportunidade de aprimorar a experiência do usuário, mantendo a simplicidade e a lógica original do desafio.

## 📚 Referência

Projeto desenvolvido com base no desafio disponibilizado pela **Digital Innovation One (DIO)**.

[Repositório de referência — Trilha Python DIO](https://github.com/digitalinnovationone/trilha-python-dio)

---

**Desenvolvido por Guilherme Neife**

Projeto educacional desenvolvido para fins de aprendizado e composição de portfólio profissional.
