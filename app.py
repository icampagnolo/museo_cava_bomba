#progetto di Alessandro Contarini per il Museo Cava Bomba di Cinto Euganeo
#5^AI
#20/10/2022
#gestione webApp


from flask import Flask,render_template,redirect, request
import json



app = Flask(__name__)            



@app.route('/')
def tipo():
         pagina ='intro.html'
         return render_template(pagina)


print("QUI")


@app.route('/sceglistanza',methods=['GET'])
def index():
        if request.method=='GET':
                
                if request.args.get("stanza") =='1':
                        Dati_per_template = { }
                        return render_template("stanza1.html",**Dati_per_template)
                elif request.args.get("stanza") =='2':
                        Dati_per_template = {}
                        return render_template("stanza2.html",**Dati_per_template)
                elif request.args.get("stanza") =='3':
                        Dati_per_template = {}
                        return render_template("stanza3.html",**Dati_per_template)
                else:
                        pagina ='intro.html'
                        return render_template(pagina)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True) 
