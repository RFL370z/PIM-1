import streamlit as st
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import bcrypt
import io
import contextlib
import matplotlib.pyplot as plt

# Banco de dados
engine = create_engine('sqlite:///users.db', echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Modelo de usuário
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    nome = Column(String, nullable=False)

Base.metadata.create_all(engine)

# Funções de usuário
def registro_user(email, senha, nome):
    hashed_password = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    novo_user = User(nome=nome, email=email, senha=hashed_password)
    try:
        session.add(novo_user)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Erro: {e}")
        return False

def login_user(email, senha):
    user = session.query(User).filter_by(email=email).first()
    if user and bcrypt.checkpw(senha.encode('utf-8'), user.senha.encode('utf-8')):
        return user.nome
    return None

# Interpretação de erros
def interpretar_erro(e):
    if isinstance(e, SyntaxError):
        return "❌ Erro de sintaxe! Isso pode ser causado por parênteses ou aspas não fechadas. Verifique se você fechou corretamente todos os símbolos."
    elif isinstance(e, NameError):
        return "❌ Você usou uma **variável ou função não definida**. Verifique a grafia."
    elif isinstance(e, ZeroDivisionError):
        return "❌ Você tentou dividir por zero. Isso não é permitido!"
    elif isinstance(e, TypeError):
        return "❌ Erro de **tipo**: talvez você esteja tentando somar uma string com um número, o que não é permitido."
    else:
        return f"❌ Erro desconhecido: {str(e)}"

# Página de estudos
def pagina_estudos(nome):
    st.title(f'Bem-vindo(a), {nome} à sua Jornada Python!')
    st.header('📘 Introdução ao Python')

    # Strings
    with st.expander("1. Strings"):
        st.markdown("""
        **Strings** são sequências de **caracteres** (letras, números e outros símbolos) que ficam entre **aspas**.
        
        Exemplos:
        ```python
        nome = "João"  # Uma string simples
        idade = "25"   # Uma string com números, mas ainda é texto
        print(nome)    # Exibe: João
        ```

        - **Como criar strings**: Basta colocar o texto entre aspas duplas `" "` ou simples `' '`.
        - **Métodos úteis com strings**:
            - `.upper()` – Converte todas as letras da string para maiúsculas.
            - `.lower()` – Converte todas as letras da string para minúsculas.
            - `len()` – Retorna o **número de caracteres** de uma string.
            - `.replace()` – Substitui parte de uma string por outra.

        **Exemplo**:
        ```python
        nome = "João"
        print(nome.upper())  # Exibe: JOÃO
        print(nome.lower())  # Exibe: joão
        print(len(nome))     # Exibe: 4
        print(nome.replace("João", "Carlos"))  # Exibe: Carlos
        ```
        """)
        entrada = st.text_input("Digite uma palavra:")
        if entrada:
            st.write(f"Maiúsculas: {entrada.upper()}")
            st.write(f"Minúsculas: {entrada.lower()}")
            st.write(f"Número de caracteres: {len(entrada)}")

    # Operadores Aritméticos
    with st.expander("2. Operadores Aritméticos"):
        st.markdown("""
        **Operadores Aritméticos** são usados para realizar cálculos matemáticos em Python.

        - **Soma (+)**: Adiciona dois números.
        - **Subtração (-)**: Subtrai o segundo número do primeiro.
        - **Multiplicação (*)**: Multiplica dois números.
        - **Divisão (/)**: Divide o primeiro número pelo segundo.
        - **Divisão Inteira (//)**: Retorna o **quociente** da divisão (sem parte decimal).
        - **Módulo (%)**: Retorna o **resto** da divisão entre dois números.
        - **Potência (**)**: Eleva o primeiro número à potência do segundo.

        **Exemplo de soma e multiplicação**:
        ```python
        a = 5
        b = 3
        print(a + b)  # Soma: Exibe 8
        print(a * b)  # Multiplicação: Exibe 15
        ```

        **Exemplo de divisão e módulo**:
        ```python
        c = 10
        d = 3
        print(c / d)  # Divisão normal: Exibe 3.333...
        print(c // d) # Divisão inteira: Exibe 3
        print(c % d)  # Módulo (resto da divisão): Exibe 1
        ```

        **Exemplo de potência**:
        ```python
        base = 2
        expoente = 3
        print(base ** expoente)  # Exibe 8 (2 elevado à 3)
        ```
        """)

        num1 = st.number_input("Número 1", value=0)
        num2 = st.number_input("Número 2", value=0)
        st.write(f"Soma: {num1 + num2}")
        st.write(f"Subtração: {num1 - num2}")
        st.write(f"Multiplicação: {num1 * num2}")
        if num2 != 0:
            st.write(f"Divisão: {num1 / num2}")
        else:
            st.write("Divisão por zero não é permitida.")

    # Treinamento com print()
    with st.expander("3. Pratique com print()"):
        st.markdown("""
        O comando **`print()`** é usado para **exibir resultados** no Python.

        Exemplo simples:
        ```python
        print("Olá, Mundo!")  # Exibe: Olá, Mundo!
        ```

        Você também pode fazer operações dentro do `print()`:
        ```python
        print(5 + 3)  # Exibe: 8
        print(10 * 2) # Exibe: 20
        ```
        Escreva um código usando `print()`. Exemplo:
        ```python
        print("Olá, Mundo!")
        print('5 + 3')            
        ```
        """)
        user_code = st.text_area("Digite seu código aqui:")
        if st.button("Executar código"):
            if "print" in user_code:
                try:
                    # Garantir que o código esteja "completo" e que as strings estejam fechadas
                    user_code = user_code.strip()
                    if user_code.count('"') % 2 != 0 or user_code.count("'") % 2 != 0:
                        st.error("❌ Parece que há uma string não fechada. Verifique as aspas.")
                    elif user_code.count('(') != user_code.count(')'):
                        st.error("❌ Parece que você não fechou corretamente os parênteses. Verifique a quantidade de parênteses.")
                    else:
                        # Executar o código com segurança
                        f = io.StringIO()
                        with contextlib.redirect_stdout(f):
                            exec(user_code, {"__builtins__": {"print": print}})
                        output = f.getvalue()
                        st.code(output, language="python")
                except SyntaxError as e:
                    st.error(f"Erro de sintaxe: `{e}`")
                    st.info("❌ Parece que há um erro de sintaxe no seu código. Verifique se você fechou todos os parênteses e aspas corretamente.")
                except Exception as e:
                    st.error(f"Erro encontrado: `{type(e).__name__}` — {e}")
                    st.info(interpretar_erro(e))
            else:
                st.warning("Use o comando print() para mostrar a saída.")

    # Calculadora
    with st.expander("4. Calculadora com código"):
        st.markdown("""
        Escreva uma conta matemática e mostre com `print()`:
        ```python
        resultado = 10 * 2 + 5
        print(resultado)
        ```
        """)
        conta = st.text_area("Digite sua conta Python aqui:", key="conta")
        if st.button("Calcular"):
            if "print" in conta:
                try:
                    f = io.StringIO()
                    with contextlib.redirect_stdout(f):
                        exec(conta, {"__builtins__": {"print": print}})
                    output = f.getvalue()
                    st.code(output, language="python")
                except SyntaxError as e:
                    st.error(f"Erro de sintaxe: `{e}`")
                    st.info("❌ Parece que há um erro de sintaxe. Verifique se você usou corretamente os operadores e parênteses.")
                except Exception as e:
                    st.error(f"Erro encontrado: `{type(e).__name__}` — {e}")
                    st.info(interpretar_erro(e))
            else:
                st.warning("Use o comando print() para mostrar a saída.")
    
    if st.button("Ir para a Prova"):
        st.session_state.page = 'prova'
        st.rerun() 
    
    # Botão para sair
    elif st.button("Sair"):
        st.session_state.page = 'login'
        st.rerun()

# Função para a página da prova
def pagina_prova():
    st.title('Prova de Python')

    if st.button("⬅ Voltar para os Estudos"):
        st.session_state.page = 'estudos'
        st.rerun()

    questoes = [
        {
            "pergunta": "O que é uma string em Python?",
            "opcoes": ["a) Um número inteiro", "b) Um tipo de dados que representa textos", "c) Um tipo de dados usado para cálculos", "d) Um erro no código"],
            "resposta_correta": "b) Um tipo de dados que representa textos"
        },
        {
            "pergunta": "Como se declara uma string corretamente em Python?",
            "opcoes": ["a) texto = 123", "b) texto = 'Olá Mundo'", "c) texto = Olá Mundo", "d) texto = \[Olá Mundo]"],
            "resposta_correta": "b) texto = 'Olá Mundo'"
        },
        {
            "pergunta": "Qual função usamos para saber o tamanho (número de caracteres) de uma string?",
            "opcoes": ["a) size()", "b) count()", "c) len()", "d) length()"],
            "resposta_correta": "c) len()"
        },
        {
            "pergunta": "O que faz o código `'python'.upper()`?",
            "opcoes": ["a) Transforma em número", "b) Deixa todas as letras em minúsculas", "c) Deixa todas as letras em maiúsculas", "d) Apaga a string"],
            "resposta_correta": "c) Deixa todas as letras em maiúsculas"
        },
        {
            "pergunta": "O que faz o código `'banana'[0]` em Python?",
            "opcoes": ["a) Mostra o último caractere da palavra", "b) Conta quantas letras tem a palavra", "c) Mostra o primeiro caractere da palavra ('b')", "d) Dá um erro"],
            "resposta_correta": "c) Mostra o primeiro caractere da palavra ('b')"
        },
        {
            "pergunta": "Qual operador usamos para somar dois números em Python?",
            "opcoes": ["a) -", "b) *", "c) +", "d) /"],
            "resposta_correta": "c) +"
        },
        {
            "pergunta": "O que faz o operador `**` em Python?",
            "opcoes": ["a) Soma dois números", "b) Multiplica normalmente", "c) Calcula a raiz quadrada", "d) Potência (exemplo: 2 ** 3 = 8)"],
            "resposta_correta": "d) Potência (exemplo: 2 ** 3 = 8)"
        },
        {
            "pergunta": "Qual o resultado de `10 // 3` em Python?",
            "opcoes": ["a) 3,33", "b) 3", "c) 10.0", "d) erro"],
            "resposta_correta": "b) 3"
        },
        {
            "pergunta": "Qual operador usamos para pegar o resto da divisão em Python?",
            "opcoes": ["a) //", "b) %", "c) **", "d) /"],
            "resposta_correta": "b) %"
        },
        {
            "pergunta": "Qual será o resultado da operação `(2 + 3) * 4`?",
            "opcoes": ["a) 20", "b) 14", "c) 24", "d) 9"],
            "resposta_correta": "a) 20"
        }
    ]

    respostas_usuario = []
    for i, questao in enumerate(questoes):
        st.subheader(f"Pergunta {i+1}: {questao['pergunta']}")
        resposta = st.radio(f"Escolha a alternativa:", questao['opcoes'], key=f"q{i+1}")
        respostas_usuario.append(resposta)

    if st.button("Finalizar Prova"):
        # Avaliar as respostas
        acertos = 0
        for i, questao in enumerate(questoes):
            if respostas_usuario[i] == questao["resposta_correta"]:
                acertos += 1

        # Exibir resultado
        st.write(f"Você acertou {acertos} de {len(questoes)} questões!")

        # Exibir gráfico de desempenho
        desempenho = [acertos, len(questoes) - acertos]
        labels = ['Acertos', 'Erros']
        fig, ax = plt.subplots()
        ax.pie(desempenho, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal') 

        st.pyplot(fig)

# Página inicial
if 'page' not in st.session_state:
    st.session_state.page = 'login'

if st.session_state.page == 'login':
    st.title('Bem-Vindo(A) ao Curso Básico de Python!')
    st.subheader('Selecione Login ou Cadastro')

    menu = st.sidebar.selectbox('Escolha uma opção:', ['Login', 'Cadastro'])

    if menu == 'Cadastro':
        st.subheader('* Criar nova conta')
        nome = st.text_input('Nome: ').strip()
        email = st.text_input('Email: ').strip()
        senha = st.text_input('Senha: ', type='password')
        if st.button('Registrar'):
            if registro_user(email, senha, nome):
                st.success('Registrado com sucesso!')
            else:
                st.error('Esse email já está cadastrado.')

    elif menu == 'Login':
        st.subheader('* Acessar conta')
        email = st.text_input('Email:', key="login_email")
        senha = st.text_input('Senha:', type='password', key="login_senha")

        if st.button("Logar"):
            nome = login_user(email, senha)
            if nome:
                st.session_state.page = 'estudos'
                st.session_state.nome = nome
                st.rerun()
            else:
                st.error('Email ou senha incorretos.')

elif st.session_state.page == 'estudos':
    pagina_estudos(st.session_state.nome)

elif st.session_state.page == 'prova':
    pagina_prova()