# 📚 Curso Básico de Python para Iniciantes

Projeto desenvolvido como trabalho acadêmico para a conclusão do **1º semestre do curso de Análise e Desenvolvimento de Sistemas** da **UNIP – Universidade Paulista**. 
O sistema foi construído em grupo com o objetivo de ensinar lógica de programação e fundamentos da linguagem Python de forma didática, interativa e acessível.

---

## 🙏🏼 Participantes - Grupo

| Nome Completo                         | R.A.    |
|-------------------------------------|---------|
| Gustavo Melo de Lima Pereira         | F363JC0 |
| Gabriel Calebe Teixeira Brandão      | H688671 |
| Leticia Mocci Dezanete               | H765GB8 |
| Rafael Henrique Jubilato Batista     | H70CJG2 |
| Rickson Tadeu Candido Pedreira      | H520BA0 |
| Pedro H. dos Reis Cassiano da Silva | H765CC7 |
| Pedro Santana França | R854BD3 | 

---

## 🎯 Objetivo Geral

Criar uma aplicação web educativa com interface intuitiva e recursos interativos, que permita ao usuário aprender os conceitos básicos de programação em Python, praticar por meio de exercícios, e ao final realizar uma avaliação com feedback e relatório de desempenho.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia      | Função                                              |
|----------------|-----------------------------------------------------|
| **Python**      | Linguagem principal do projeto                      |
| **Streamlit**   | Framework para construção da interface web         |
| **SQLite + SQLAlchemy** | Banco de dados e ORM para persistência de usuários |
| **bcrypt**      | Criptografia de senhas (conforme LGPD)             |
| **Matplotlib**  | Geração de gráfico de desempenho (pizza)           |
| **JSON**        | Armazenamento dos resultados individuais da prova  |

---

## ⚙️ Como executar o Projeto

1. Instale as dependências
 no terminal:
 pip install streamlit sqlalchemy bcrypt matplotlib
2. Execute a aplicação
 no terminal:
 streamlit run pim.py
3. Acesse a aplicação no navegador padrão pelo link exibido no terminal.

---

## 🔐 Sistema de Login e Cadastro

A aplicação oferece um sistema seguro de autenticação, com:

- Cadastro com **nome, email e senha**
- Login com validação segura da senha
- Criptografia de senhas usando **bcrypt**
- Armazenamento seguro em banco de dados SQLite

**Exemplo de criptografia:**
```python
hashed_password = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
