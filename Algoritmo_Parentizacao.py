def verifica_parenteses(expressao):
    pilha = []  # Inicializa a pilha vazia

    for sym in expressao:
        if sym == '(':
            pilha.append(sym)  # Adiciona parêntesis esquerdo à pilha
        elif sym == ')':
            if not pilha:  # Se a pilha estiver vazia, os parênteses não estão balanceados
                return False
            left = pilha.pop()  # Remove o último parêntesis esquerdo da pilha
            if left != '(':
                return False  # Parêntesis não correspondentes
    return len(pilha) == 0  # Retorna True se a pilha estiver vazia, caso contrário, False

expressao = input("Digite uma expressão com parênteses: ")
resultado = verifica_parenteses(expressao)

if resultado:
    print("Os parênteses estão balanceados e corretamente aninhados.")
else:
    print("Os parênteses não estão balanceados ou corretamente aninhados.")


# A função verifica_parenteses(expressao) é definida, que recebe uma expressão como entrada.

# Uma pilha vazia chamada pilha é criada para armazenar os parênteses esquerdos encontrados na expressão.

# O código percorre cada caractere sym na expressão.

# Se sym for um parêntesis esquerdo '(', ele é adicionado ao topo da pilha pilha.

# Se sym for um parêntesis direito ')', o código verifica se a pilha está vazia. Se estiver vazia, isso significa que não há parênteses esquerdos correspondentes, então a função retorna False.

# Caso contrário, o último parêntesis esquerdo na pilha é removido e armazenado na variável left. Isso garante que os parênteses sejam aninhados corretamente.

# Em seguida, é verificado se left e sym são parênteses complementares (ou seja, '(' e ')'). Se não forem complementares, a função retorna False.

# Depois de percorrer toda a expressão, a função verifica se a pilha está vazia. Se estiver vazia, isso significa que todos os parênteses foram corretamente fechados e aninhados, e a função retorna True. Caso contrário, retorna False.

# O programa solicita que o usuário insira uma expressão com parênteses.

# A função verifica_parenteses(expressao) é chamada com a expressão fornecida pelo usuário.

# O resultado da verificação é armazenado na variável resultado.

# O programa exibe uma mensagem informando se os parênteses na expressão estão balanceados e corretamente aninhados, com base no valor de resultado.

# Em resumo, o código verifica a validade dos parênteses em uma expressão matemática, garantindo que eles estejam balanceados e corretamente aninhados. Se todos os parênteses forem corretamente fechados e aninhados, a função retorna True; caso contrário, retorna False.