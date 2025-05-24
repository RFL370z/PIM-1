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
🔐 Política de Dados e Privacidade
Este projeto segue práticas básicas de segurança e privacidade de dados, com foco na conformidade com a LGPD (Lei Geral de Proteção de Dados Pessoais):

Coleta mínima de dados: Apenas nome, e-mail e senha são solicitados no cadastro.

Uso exclusivo para fins acadêmicos e educacionais.

Criptografia de senhas com bcrypt, impedindo o armazenamento de senhas em texto puro.

Armazenamento local em banco de dados SQLite, sem uso de servidores externos.

Sem compartilhamento de dados com terceiros.

✅ O sistema pode ser adaptado para uso real mediante aplicação de políticas mais robustas, como consentimento explícito e termos de uso.

🌱 Estratégias para Menor Consumo de Energia
Durante o desenvolvimento e execução do projeto, foram adotadas medidas para reduzir o consumo energético:

Uso de ferramentas leves como Streamlit e SQLite, que não exigem servidores ou serviços em nuvem pesados.

Execução local do sistema, dispensando servidores ligados 24h por dia.

Hardware compatível com eficiência energética: Notebooks com gerenciamento de energia ativo.

Codificação otimizada para reduzir processamento desnecessário (uso eficiente de loops, cache e operações simples).

💡 O foco foi desenvolver uma aplicação eficiente, de fácil execução em computadores comuns, sem necessidade de infraestrutura complexa.

💻 Justificativa: Escolha do Windows 11 Pro
O sistema foi desenvolvido em ambiente Windows 11 Pro, considerando os seguintes critérios:

Critério	Justificativa
Compatibilidade	Suporte nativo a ferramentas como Python, VS Code e bibliotecas usadas no projeto.
Estabilidade	Ambiente estável e atualizado, com bom suporte para desenvolvedores.
Acesso a recursos de segurança	A versão Pro oferece funcionalidades como BitLocker, Hyper-V e Windows Sandbox, úteis para testes e segurança de dados.
Apoio acadêmico	Muitos estudantes utilizam Windows 11 através de licenças fornecidas pela universidade.
Facilidade de uso	Interface familiar para a maioria dos integrantes do grupo.
Desempenho em notebooks	Sistema otimizado para dispositivos móveis, com boas práticas de consumo energético.

🎓 A escolha levou em conta a disponibilidade da ferramenta, o nível de conhecimento dos participantes e a necessidade de um ambiente confiável para o desenvolvimento de um projeto educacional.

## 🔐 Sistema de Login e Cadastro

A aplicação oferece um sistema seguro de autenticação, com:

- Cadastro com **nome, email e senha**
- Login com validação segura da senha
- Criptografia de senhas usando **bcrypt**
- Armazenamento seguro em banco de dados SQLite

**Exemplo de criptografia:**
```python
hashed_password = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


