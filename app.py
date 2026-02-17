from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    # Página principal con el propósito del negocio (D´CARPI)
    return render_template("index.html", empresa="D´CARPI", rubro="Salsas y Condimentos")

# Ruta dinámica adaptada al negocio
@app.route('/producto/<nombre>')
def producto(nombre):
    # Mensaje coherente para el negocio
    return render_template("producto.html", nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)
