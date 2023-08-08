# Algoritmo_Parentizacao

1. Faça a pilha de parêntesis P vazia
2. Para cada símbolo sym na expressão (percorrendo da esq. para direita)
repita:
2.1 Se sym é um parêntesis esquerdo
2.1.1 Adicione sym ao topo da pilha P
2.2 Se sym é um parêntesis direito
2.2.1 Se a pilha P está vazia, termine com false
2.2.2 Remova o parêntesis do topo de P para uma variável left
2.2.3 Se left e sym não são parêntesis complementares, termine
com false
3. Termine com true se a pilha P está vazia, ou false caso contrário 
