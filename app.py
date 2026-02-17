from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template(
        "index.html",
        empresa="D´CARPI",
        rubro="Salsas y Condimentos",
        mensaje="Empresa especializada en la producción y distribución de salsas y condimentos de alta calidad."
    )

@app.route('/producto/<nombre>')
def producto(nombre):
    return render_template("producto.html", nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)
