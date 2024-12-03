from abc import ABC, abstractmethod

# Definição da classe abstrata Pagamento
class Pagamento(ABC):
    @abstractmethod
    def processar(self):
        pass

# Implementação do pagamento com Cartão de Crédito
class PagamentoCartaoCredito(Pagamento):
    def processar(self):
        print('Processando pagamento com Cartão de Crédito')

# Implementação do pagamento com PayPal
class PagamentoPayPal(Pagamento):
    def processar(self):
        print('Processando pagamento com PayPal')

# Implementação do pagamento com Boleto
class PagamentoBoleto(Pagamento):
    def processar(self):
        print('Processando pagamento com Boleto')

# Classe de fábrica para criar pagamentos
class PagamentoFactory:
    @staticmethod
    def criar_pagamento(tipo):
        if tipo == 'cartao':
            return PagamentoCartaoCredito()
        elif tipo == 'paypal':
            return PagamentoPayPal()
        elif tipo == 'boleto':
            return PagamentoBoleto()
        else:
            raise ValueError('Tipo de pagamento inválido')

# Exemplo de uso
if __name__ == "__main__":
    pagamento_tipo = input("Digite o tipo de pagamento (cartao, paypal, boleto): ")
    pagamento = PagamentoFactory.criar_pagamento(pagamento_tipo)
    pagamento.processar()