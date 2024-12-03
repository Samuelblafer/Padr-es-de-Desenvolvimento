# Implementação do pagamento com Cartão de Crédito
class PagamentoCartaoCredito:
    def processar(self):
        print('Processando pagamento com Cartão de Crédito')

# Implementação do pagamento com PayPal
class PagamentoPayPal:
    def processar(self):
        print('Processando pagamento com PayPal')

# Implementação do pagamento com Boleto
class PagamentoBoleto:
    def processar(self):
        print('Processando pagamento com Boleto')

# Exemplo de uso
if __name__ == "__main__":
    pagamento_tipo = input("Digite o tipo de pagamento (cartao, paypal, boleto): ")

    if pagamento_tipo == 'cartao':
        pagamento = PagamentoCartaoCredito()
    elif pagamento_tipo == 'paypal':
        pagamento = PagamentoPayPal()
    elif pagamento_tipo == 'boleto':
        pagamento = PagamentoBoleto()
    else:
        raise ValueError('Tipo de pagamento inválido')

    pagamento.processar()