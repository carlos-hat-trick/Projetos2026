from flask import Flask, render_template

# Criando a aplicação Flask
app = Flask(__name__)

# Criando uma ROTA (o endereço do site)
@app.route("/")
def home():
    # Aqui o Python prepara os dados
     titulo_site = "Aula de Flask - 3o Ano"
    # O Python "renderiza" (desenha) o HTML e envia as variáveis
     return render_template("index.html", titulo=titulo_site)

@app.route("/sobre")
def about():
    titulo_site = "Pagina de sobre (é sobre e esta tudo bem)"
    return render_template("sobre.html" , titulo=titulo_site)

# Rodando o servidor
if __name__ == "__main__":
    app.run(debug=True)  # debug=True faz o site atualizar sozinho quando
    # salvamos