from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

#EJERCICIO N1
@app.route('/ejercicioN1', methods=['GET', 'POST'])
def ejercicioN1():
    if request.method  == 'POST':
        # Ingresa datos formulario N1
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])
        # Procesa el promedio
        promedio = (nota1 + nota2 + nota3) / 3
        # Comprobar estado (aprobado o reprobado)
        if promedio >= 40 and asistencia >= 75:
            estado = "Aprobado"
        else:
            estado = "Reprobado"
        return render_template('ejercicioN1.html', promedio=promedio, estado=estado)
    return render_template('ejercicioN1.html')

#EJERCICIO N2
@app.route('/ejercicioN2', methods=['GET', 'POST'])
def ejercicioN2():
    if request.method == 'POST':
        # Procesa informacion formulario 2
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        # Identifica el nombre con más caracteres
        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo =max(nombres, key=len)
        cantidad_caracteres = len(nombre_mas_largo)
        return render_template('ejercicioN2.html', nombre_mas_largo=nombre_mas_largo, cantidad_caracteres=cantidad_caracteres)
    return render_template('ejercicioN2.html')

if __name__ == '__main__':
    app.run(debug=True)