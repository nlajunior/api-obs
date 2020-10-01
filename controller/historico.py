from model.historico import Historico

class HistoricoController():

  def __init__(self):
    self.historico_model = Historico()

  def get_historicos(self, limit):
      logs = []
      try:
          res = self.historico_model.get_all(limit=limit)
          for registro in res:
              logs.append({
                  'id': registro.id,
                  'email_cliente': registro.email_cliente,
                  'endereco_pdf': registro.endereco_pdf,
                  'respondente': registro.respondente,
                  'empresa': registro.empresa,
                  'data_envio': registro.data_envio,
                  'cnpj': registro.cnpj,
                  'faturamento': registro.faturamento,
                  'telefone': registro.telefone,
                  'data_submissao': registro.data_submissao,
                  'email_consultor': registro.email_consultor    
              })
          status = 200
      except Exception as e:
            print(e)
            result=[]
            status=400
      finally:
            return {
                'result': logs,
                'status': status
            }