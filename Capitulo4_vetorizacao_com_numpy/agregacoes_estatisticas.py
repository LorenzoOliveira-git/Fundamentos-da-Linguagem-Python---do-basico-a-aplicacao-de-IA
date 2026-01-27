# 6. Agregações Estatísticas

#Calcular estatísticas descritivas de um conjunto de dados é uma tarefa comum e muito otimizada no NumPy.

import numpy as np

# Simulando as notas de 3 alunos em 4 provas
notas = np.array([
    [8.5, 7.0, 9.2, 6.5],  # Aluno 1
    [5.5, 6.8, 7.5, 8.0],  # Aluno 2
    [9.5, 9.0, 8.8, 10.0]  # Aluno 3
])

print("\nMatriz de Notas:\n")
print(notas)
type(notas)

# Agregações na matriz inteira
print(f"\nMédia geral da turma:    {notas.mean():.2f}")
print(f"Nota máxima da turma:    {notas.max()}")
print(f"Nota mínima da turma:    {notas.min()}")
print(f"Soma de todas as notas:  {notas.sum()}\n")

# Agregações por eixo (axis)
# Média de cada aluno (agregando nas colunas, axis = 1) arredondando para duas casas decimais
media_por_aluno = notas.mean(axis = 1).round(2)
print(f"\nMédia de cada aluno: {media_por_aluno}\n")

# Média de cada prova (agregando nas linhas, axis = 0) arredondando para duas casas decimais
media_por_prova = notas.mean(axis = 0).round(2)
print(f"\nMédia de cada prova: {media_por_prova}")