# 🏦 Sistema Bancário em Python 🐍

Bem-vindo ao repositório do Desefio de Engenharia de Dados da DIO:  **Otimização do Sistema Bancário com Funções**!
Acesso o código aqui >> [Codigo Fonte](codigo.py)

## 🎯 Objetivo Geral

Criar um sistema bancário com as operações: **sacar, depositar e visualizar extrato**; utilizando **funções**. Além disso implementar novas funções de **criação de usuário** e **criação de conta**

## 🚀 Desafio

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e, para isso, escolheu a linguagem Python. Para a primeira versão do sistema, devemos melhorar o sistema bancario, implementando funções para as operações: depósito, saque e extrato. Além disso estabelecer um sistema de cadastro de usuários e contas.

# 🚀 Funcionalidades
## 💰 Operação de Depósito

- Deve ser possível depositar valores positivos para a conta bancária.
- A v1 do projeto trabalha apenas com 1 usuário, dessa forma, não precisamos nos preocupar em identificar qual é o número da agência e conta bancária.
- Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

## 🏧 Operação de Saque

- O sistema deve permitir realizar 3 saques diários, com limite máximo de R$ 500,00 por saque.
- Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
- Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

## 📄 Operação de Extrato

- Essa operação deve listar todos os depósitos e saques realizados na conta.
- No fim da listagem, deve ser exibido o saldo atual da conta.
- Se o extrato estiver em branco, exibir a mensagem: "Não foram realizadas movimentações."
- Os valores devem ser exibidos utilizando o formato `R$ xxx.xx`. Exemplo: 1500.45 = R$ 1500.45.

## 👤 Operação de Criar usuario (cliente)
- Armezenar em uma lista
- Inserir campos: nome, data de nascimento, cpf (somente números) e endereço (logradouro, nro - bairro - cidade/sigla estado)
- Não podemos cadastrar dois usuários no mesmo cpf.

## 💳 Operação de Criar conta corrente 
- Armezenar em uma lista
- Inserir campos: agência (constante= '0001' ), número da conta (iniciando em 1) e usuário.
