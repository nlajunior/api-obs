from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import app_active, app_config
config = app_config[app_active]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Role(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String(40),unique=True, nullable=False)

class User(db.Model):
  id=db.Column(db.Integer,primary_key=True)
  username=db.Column(db.String(40),unique=True,nullable=False)
  email=db.Column(db.String(120),unique=True,nullable=False)
  password=db.Column(db.String(200),nullable=False)
  date_created=db.Column(db.DateTime(6),default=db.func.current_timestamp(),nullable=False)
  last_update=db.Column(db.DateTime(6),onupdate=db.func.current_timestamp(),nullable=True)
  recovery_code=db.Column(db.String(200),nullable=True)
  active=db.Column(db.Boolean(),default=1,nullable=True)

  role=db.Column(db.Integer,db.ForeignKey(Role.id),nullable=False)

class Historico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email_cliente = db.Column(db.String(200), unique=False, nullable=True)
    endereco_pdf = db.Column(db.String(200), unique=True, nullable=True)
    respondente = db.Column(db.String(200), nullable=True)
    empresa =  db.Column(db.String(200), nullable=True)
    data_envio = db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=True)
    cnpj = db.Column(db.String(50), nullable=True)
    faturamento = db.Column(db.String(50), nullable=True)
    telefone = db.Column(db.String(50), nullable=True)
    data_submissao = db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=True)
    email_consultor = db.Column(db.String(200), unique=False, nullable=True)

if __name__ == '__main__':
  manager.run()