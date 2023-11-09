from flask import Flask, render_template
import fdb
from DB import config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

 # Importa o módulo conn.py dentro da pasta DB

host = config.host
port = config.port
database = config.database
user = config.user
password = config.password
fb_library_name = config.fb_library_name


conne = fdb.connect(
host = host,
port = port,
database = database,
user = user,
password = password,
fb_library_name=fb_library_name
)


@app.route('/',methods=["GET"])
def inicio():
    return render_template("index.html")
   


@app.route('/pesquisa', methods=["GET"])
def pesquisa():
    cli = conne.cursor()
    cli.execute('select codclifor, nome from clifor where cliente_ativo=1 ')
    cli_result = cli.fetchall()
    items = []
    for row in cli_result:
        items.append({
            'codclifor': row[0],
            'nome':row[1]
            # Adicione aqui os outros campos que deseja listar
        })
    return items



if __name__ == "__main__":
    app.run(debug=True, port=5000, host='localhost')
