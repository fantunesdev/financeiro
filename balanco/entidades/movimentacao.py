class Movimentacao():
    def __init__(self, data, conta, cartao, categoria, descricao, valor, parcelas, pagas, fixa, moeda, observacao,
                 lembrar, tipo, efetivado, tela_inicial, usuario):
        self.data = data
        self.conta = conta
        self.cartao = cartao
        self.categoria = categoria
        self.descricao = descricao
        self.valor = valor
        self.parcelas = parcelas
        self.pagas = pagas
        self.fixa = fixa
        self.moeda = moeda
        self.observacao = observacao
        self.lembrar = lembrar
        self.tipo = tipo
        self.efetivado = efetivado
        self.tela_inicial = tela_inicial
        self.usuario = usuario
