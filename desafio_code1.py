''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

def filtrar_transacoes(transacoes, limite):
    transacoes_filtradas = []
    for vr in transacoes:
        if vr > limite:
            transacoes_filtradas.append(vr)
        if vr < 0:
               vrp = abs(vr)
               if vrp > limite:
                  transacoes_filtradas.append(vr)
    return transacoes_filtradas


entrada = input()

entrada_transacoes, limite = entrada.split("],")
entrada_transacoes = entrada_transacoes.strip("[]").replace(" ", "") 
limite = float(limite.strip())


transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

# Transações:[100, -50, 300, -150], 100	
resultado = filtrar_transacoes(transacoes, limite)

print(f"Transações: {resultado}")