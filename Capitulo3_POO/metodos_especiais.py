## 6. Métodos Especiais (ou "Mágicos")

#São métodos com nomes que começam e terminam com duplo sublinhado. Eles permitem que seus objetos se comportem como tipos nativos em Python. Os mais comuns são __init__ (construtor) e __str__ (representação em string do objeto).

# Cria a classe
class Livro:

    # Construtor
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # Chamado quando usamos print() ou str() no objeto
    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"

    # Chamado quando usamos len() no objeto
    def __len__(self):
        return self.paginas
    
# Cria o objeto
livro_dsa = Livro("Deep Learning Book", "Data Science Academy", 100)

type(livro_dsa)

# O método __str__ é chamado aqui
print(livro_dsa)

# O método __len__ é chamado aqui
print(f"O livro tem {len(livro_dsa)} páginas.")