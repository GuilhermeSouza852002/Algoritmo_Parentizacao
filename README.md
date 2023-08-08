# Algoritmo_Parentizacao

Faça a pilha de parêntesis P vazia
Para cada símbolo sym na expressão (percorrendo da esq. para direita)
repita:
Se sym é um parêntesis esquerdo
Adicione sym ao topo da pilha P
Se sym é um parêntesis direito
Se a pilha P está vazia, termine com false
Remova o parêntesis do topo de P para uma variável left
Se left e sym não são parêntesis complementares, termine
com false
Termine com true se a pilha P está vazia, ou false caso contrário
