from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    titulo_site = "Alee"
#    dados_alee = {
#        "nome": "Alee",
#        "Projetos": [
#           "CAOS (Álbum , 2024)",
#          "CAOS DLX (Álbum , 2025)",
#            "SPAM (Ep , 2026)",
#           "PARA:TODAS QUE FINGI AMAR (Álbum , 2026)"
#       ]
#   }
#preciso achar uma jeito de formatar essas coisas de cima 

    return render_template("index.html" , titulo = titulo_site ,) #alee = dados_alee , )

if __name__ == "__main__":
    app.run(debug=True)