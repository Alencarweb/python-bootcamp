# Otimizando o Sistema Bancário com Funções Python

import textwrap
from datetime import datetime
from abc import ABC, abstractmethod


class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class Conta:
    def __init__(self, numero, cliente, limite=1000, limite_saques=4):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.limite = limite
        self.limite_saques = limite_saques
        self.historico = []

    def sacar(self, valor):
        if valor > self.saldo:
            return "Saldo insuficiente."
        if valor > self.limite:
            return "Valor excede o limite."
        self.saldo -= valor
        self.historico.append({"tipo": "Saque", "valor": valor, "data": datetime.now()})
        return "Saque realizado com sucesso."

    def depositar(self, valor):
        if valor <= 0:
            return "Valor inválido."
        self.saldo += valor
        self.historico.append({"tipo": "Depósito", "valor": valor, "data": datetime.now()})
        return "Depósito realizado com sucesso."

    def extrato(self):
        extrato = "\n".join(
            f"{t['data']} - {t['tipo']}: R$ {t['valor']:.2f}" for t in self.historico  
        )
        return extrato or "Nenhuma transação realizada."
    
    def saldo_atual(self):
        return f"Saldo atual: R$ {self.saldo:.2f}"

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    for conta in contas:
        print(
            f"Conta Nº: {conta.numero}, Cliente: {conta.cliente.nome}, CPF: {conta.cliente.cpf}, Saldo: R$ {conta.saldo:.2f}"
        )

def menu():
    return input(
        textwrap.dedent(
            """
            ================ MENU ================
            [d] Depositar
            [s] Sacar
            [sa] Saldo atual
            [e] Extrato
            [nc] Nova conta
            [lc] Listar contas
            [nu] Novo usuário
            [q] Sair
            => """
        )
    )


def encontrar_cliente(cpf, clientes):
    return next((c for c in clientes if c.cpf == cpf), None)


def criar_cliente(clientes):
    cpf = input("CPF: ")
    if encontrar_cliente(cpf, clientes):
        print("Cliente já cadastrado.")
        return
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    clientes.append(Cliente(nome, cpf, endereco))
    print("Cliente criado com sucesso.")


def criar_conta(clientes, contas):
    cpf = input("CPF do cliente: ")
    cliente = encontrar_cliente(cpf, clientes)
    if not cliente:
        print("Cliente não encontrado.")
        return
    numero = len(contas) + 1
    conta = Conta(numero, cliente)
    cliente.adicionar_conta(conta)
    contas.append(conta)
    print("Conta criada com sucesso.")


def realizar_operacao(clientes, contas, operacao):
    cpf = input("CPF do cliente: ")
    cliente = encontrar_cliente(cpf, clientes)
    if not cliente or not cliente.contas:
        print("Cliente ou conta não encontrada.")
        return
    conta = cliente.contas[0]
    if operacao == "d":
        valor = float(input("Valor do depósito: "))
        print(conta.depositar(valor))
    elif operacao == "s":
        valor = float(input("Valor do saque: "))
        print(conta.sacar(valor))
    elif operacao == "e":
        print(conta.extrato())
    elif operacao == "sa":
        print(conta.saldo_atual())


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "d":
            realizar_operacao(clientes, contas, "d")
        elif opcao == "s":
            realizar_operacao(clientes, contas, "s")
        elif opcao == "e":
            realizar_operacao(clientes, contas, "e")
        elif opcao == "sa":
            realizar_operacao(clientes, contas, "sa")
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            criar_conta(clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()