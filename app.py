import locale
import sys

import requests
import config
from datetime import datetime
from models.Cotacao import Cotacao
from dao.sqlite_dao_factory import SqliteDAOFactory

url_base = 'https://api.hgbrasil.com/finance'.format('?key={0}', config.api_key)


locale.setlocale(locale.LC_ALL, '')
data_hora_hoje = str(datetime.today().date().strftime('%A, %x'))
cotacaoDAO = None
cotacao_hoje = None


def consultar_dados_financeiros() -> Cotacao:
    res = requests.get(url_base)
    dados = res.json()['results']['currencies']

    dolar = float(dados['USD']['buy'])
    euro = float(dados['EUR']['buy'])
    data_hora = str(datetime.now())

    return Cotacao(dolar=dolar, euro=euro, data_hora=data_hora)


def salvar_cotacao(cotacao) -> None:
    cotacaoDAO.adicionar(cotacao)


def carregar_cotacao_hoje() -> Cotacao:
    registro_cotacao_hoje = cotacaoDAO.buscar_cotacao_hoje()

    if registro_cotacao_hoje is None:
        cotacao = consultar_dados_financeiros()
        salvar_cotacao(cotacao)
        return cotacao
    else:
        registro_cotacao_hoje = cotacaoDAO.buscar_cotacao_hoje()
        return Cotacao(registro_cotacao_hoje[0], registro_cotacao_hoje[1],
                       registro_cotacao_hoje[2], registro_cotacao_hoje[3])


def mostrar_menu():

    print('  ╔══════════════════════════════╗')
    print(f'  ║ Cotação: {data_hora_hoje}  ║')
    print(f'  ║ Dólar: $ {cotacao_hoje.dolar}              ║')
    print(f'  ║ Euro: € {cotacao_hoje.euro}               ║')
    print('  ╚══════════════════════════════╝')
    print('Digite um valor em R$ ou 0 para SAIR')

    valor_reais = float(input('R$ '))

    if valor_reais > 0:
        real_em_dolar = valor_reais * cotacao_hoje.dolar
        real_em_euro = valor_reais * cotacao_hoje.euro
        print(f'\n R$ {valor_reais} = $ {real_em_dolar}')
        print(f' R$ {valor_reais} = € {real_em_euro}')
        print('\n')
        mostrar_menu()
    else:
        sys.exit('Encerrando o programa . . .')


if __name__ == '__main__':
    sqliteFactory = SqliteDAOFactory()
    cotacaoDAO = sqliteFactory.cotacao_dao
    cotacao_hoje = carregar_cotacao_hoje()
    mostrar_menu()