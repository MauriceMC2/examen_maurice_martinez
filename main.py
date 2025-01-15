from flask import Flask, render_template, request

app = Flask(__name__)

usuarios = {
    "juan": {"password": "admin", "rol": "Administrador"},
    "pepe": {"password": "user", "rol": "Usuario"}
}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        precio_tarro = 9000
        total_sin_descuento = cantidad * precio_tarro

        if 18 <= edad <= 30:
            descuento = total_sin_descuento * 0.15
        elif edad > 30:
            descuento = total_sin_descuento * 0.25
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento - descuento

        return render_template(
            'ejercicio1.html',
            nombre=nombre,
            total_sin_descuento=total_sin_descuento,
            descuento=descuento,
            total_con_descuento=total_con_descuento
        )
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']

        if nombre in usuarios and usuarios[nombre]['password'] == contrasena:
            rol = usuarios[nombre]['rol']
            mensaje = f"Bienvenido {rol.lower()} {nombre}"
            exito = True
        else:
            mensaje = "Usuario o contraseña incorrectos"
            exito = False

        return render_template(
            'ejercicio2.html',
            mensaje=mensaje,
            exito=exito
        )
    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)
