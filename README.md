# Algoritmo_Parentizacao
# Criado por: Cristian Rodolfo, Guilherme Oliveira, Ruan Patrick

1. Faça a pilha de parêntesis P vazia
2. Para cada símbolo sym na expressão (percorrendo da esq. para direita)
repita:
3. Se sym é um parêntesis esquerdo
4. Adicione sym ao topo da pilha P
5. Se sym é um parêntesis direito
6. Se a pilha P está vazia, termine com false
7. Remova o parêntesis do topo de P para uma variável left
8. Se left e sym não são parêntesis complementares, termine
com false
9. Termine com true se a pilha P está vazia, ou false caso contrário
