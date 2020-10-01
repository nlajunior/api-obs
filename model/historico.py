# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from config import app_active, app_config

config = app_config[app_active]

db = SQLAlchemy(config.APP)

class Historico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email_cliente = db.Column(db.String(200), unique=False, nullable=True)
    endereco_pdf = db.Column(db.String(200), unique=True, nullable=True)
    respondente = db.Column(db.String(200), nullable=True)
    empresa =  db.Column(db.String(200), nullable=True)
    date_envio = db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=True)
    cnjp = db.Column(db.String(50), nullable=True)
    faturamento = db.Column(db.String(50), nullable=True)
    telefone = db.Column(db.String(50), nullable=True)
    data_submissao = db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=True)
    email_consultor = db.Column(db.String(200), unique=False, nullable=True)
  
    def get_all(self, limit=None):
        try:
            if limit is None:
                res = db.session.query(Historico).order_by(Historico.data_submissao).all()
            else:
                res = db.session.query(Historico).order_by(Historico.data_submissao).limit(limit).all()
        except Exception as e:
            res = []
            print(e)
        finally:
            db.session.close()
            return res     