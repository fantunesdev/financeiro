from balanco.repositorios import movimentacao_repositorio
from balanco.services import movimentacao_service, parcelamento_service


def adicionar_parcelas(movimentacoes, movimentacao_nova):
    # Cadastrar parcelas novas:
    indice_inicial = movimentacoes[0].numero_parcelas + 1
    indice_final = movimentacao_nova.numero_parcelas
    movimentacao_nova.pagas = 0
    for i in range(indice_inicial, indice_final):
        movimentacao_nova.data_efetivacao = movimentacao_repositorio.somar_mes(movimentacao_nova, i)
        movimentacao_nova.pagas = i + 1
        movimentacao_nova.parcelamento = movimentacoes[0].parcelamento
        movimentacao_service.cadastrar_movimentacao(movimentacao_nova)
    # Editar parcelas antigas
    for index, movimentacao in enumerate(movimentacoes):
        movimentacao_nova.data_efetivacao = movimentacao_repositorio.somar_mes(movimentacao, index)
        movimentacao_nova.pagas = index + 1
        movimentacao_service.editar_movimentacao(movimentacao, movimentacao_nova)


def remover_parcelas(movimentacoes, movimentacao_nova):
    movimentacao_nova.pagas = 0
    if movimentacao_nova.numero_parcelas <= 1:
        parcelamento = movimentacao_nova.parcelamento
        movimentacao_nova.numero_parcelas = 0
        movimentacao_nova.parcelamento = None
        movimentacao_nova.data_efetivacao = movimentacoes[0].data_efetivacao
        movimentacao_service.editar_movimentacao(movimentacoes[0], movimentacao_nova)
        parcelamento_service.remover_parcelamento(parcelamento)
    else:
        for index, movimentacao in enumerate(movimentacoes):
            if movimentacao.pagas <= movimentacao_nova.numero_parcelas:
                movimentacao_nova.data_efetivacao = movimentacao_repositorio.somar_mes(movimentacao, index)
                movimentacao_nova.pagas = index + 1
                movimentacao_service.editar_movimentacao(movimentacao, movimentacao_nova)
            else:
                movimentacao_service.remover_movimentacao(movimentacao)


def editar_parcelas(movimentacoes, movimentacao_nova):
    for index, movimentacao in enumerate(movimentacoes):
        movimentacao_nova.data_efetivacao = movimentacao_repositorio.somar_mes(movimentacao, index)
        movimentacao_nova.pagas = index + 1
        movimentacao_service.editar_movimentacao(movimentacao, movimentacao_nova)


def editar_parcelamento(movimentacoes, movimentacao_nova):
    aumentar_numero_parcelas = movimentacoes[0].numero_parcelas < movimentacao_nova.numero_parcelas
    diminuir_numero_parcelas = movimentacoes[0].numero_parcelas > movimentacao_nova.numero_parcelas

    if aumentar_numero_parcelas:
        adicionar_parcelas(movimentacoes, movimentacao_nova)
    elif diminuir_numero_parcelas:
        remover_parcelas(movimentacoes, movimentacao_nova)
    else:
        editar_parcelas(movimentacoes, movimentacao_nova)
