import sqlite3
import dao.sqlite_dao_factory as dao

from dao.cotacao_dao import CotacaoDAO


class SqliteCotacaoDAO(CotacaoDAO):

    def selecionar_cotacao(self, limit=10) -> list:

        conexao = dao.SqliteDAOFactory.criar_conexao()
        cursor = conexao.cursor()

        # dados = []
        query = 'SELECT * FROM Cotacao ORDER BY data_hora_coleta LIMIT ?'

        try:
            dados = cursor.execute(query, (limit,)).fetchall()
            conexao.commit()
        except sqlite3.Error as e:
            raise Exception(f'Erro: {e}')
        finally:
            if conexao:
                conexao.close()

        return dados

    def buscar_cotacao_hoje(self):

        conexao = dao.SqliteDAOFactory.criar_conexao()
        cursor = conexao.cursor()

        # SELECT DATE(data_hora_coleta) FROM Cotacao
        # WHERE DATE(data_hora_coleta) = date('2022-04-04 13:16:11.818143');

        # dados = []
        query = 'SELECT * FROM Cotacao WHERE DATE(data_hora_coleta) = DATE();'

        try:
            dados = cursor.execute(query).fetchone()
        except sqlite3.Error as e:
            raise Exception(f'Erro: {e}')
        finally:
            if conexao:
                conexao.close()

        return dados


    def adicionar(self, cotacao):

        conexao = dao.SqliteDAOFactory.criar_conexao()
        cursor = conexao.cursor()

        query = 'INSERT INTO Cotacao VALUES (null, ?, ?, ?)'
        registro = (cotacao.dolar, cotacao.euro, cotacao.data_hora)

        try:
            cursor.execute(query, registro)
            conexao.commit()
        except sqlite3.Error as e:
            raise Exception(f'Erro: {e}')
        finally:
            if conexao:
                conexao.close()

    def excluir(self, id: int):

        conexao = dao.SqliteDAOFactory.criar_conexao()
        cursor = conexao.cursor()

        query = 'DELETE FROM Cotacao WHERE id_cotacao = ?'

        try:
            cursor.execute(query, (id,))
            conexao.commit()
        except sqlite3.Error as e:
            raise Exception(f'Erro: {e}')
        finally:
            if conexao:
                conexao.close()