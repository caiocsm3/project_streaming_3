import random 
import string
from datetime import datetime 

cod_cliente = list(range(1, 51))
agencia = [2323, 4400, 7676]
conta = ['12345-63', '12345-99', '00005-63', '12345-44', '12565-69']
valor = list(range(10, 1000))
tipo_operacao = ['Deposito','Saque']
data = datetime.now()
data_str = data.strftime("%d/%m/%Y %H:%M:%S")
saldo_conta = list(range(100, 5000))


def generate_message() -> dict:
    random_cod_cliente = random.choice(cod_cliente)
    random_agencia = random.choice(agencia)
    random_conta = random.choice(conta)
    random_valor = random.choice(valor)
    random_tipo_operacao = random.choice(tipo_operacao)
    random_data = data_str
    random_saldo_conta = random.choice(saldo_conta)
    # Generate a random message
    message = ''.join(random.choice(string.ascii_letters) for i in range(32))
    return {
        'cod_cliente': random_cod_cliente,
        'agencia': random_agencia,
        'CONTA_CORRENTE': random_conta,
        'valor': float(random_valor),
        'tipo_operacao': random_tipo_operacao,
        'data': random_data,
        'saldo_conta': float(random_saldo_conta)
    }
