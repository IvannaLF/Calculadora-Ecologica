# Importar
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, lights, device):
    # Variables que permiten calcular el consumo energético de los aparatos
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# La primera página
@app.route('/')
def index():
    return render_template('index.html')
# Segunda página
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# La tercera página
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size = size, 
                            lights = lights                           
                           )

# Cálculo
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
# El formulario
@app.route('/form')
def form():
    return render_template('form.html')

#Resultados del formulario
@app.route('/submit', methods=['POST'])
def submit_form():
    # Declarar variables para la recogida de datos
    name = request.form['name']
    email = request.form['email'] #request = Una peticion, solicitamos el campo email. Entonces el formulario devuelve lo que esta guardado en el campo email
    address = request.form['address']
    date = request.form['date']
    with open('form.text', 'a',) as f: #"a" significa agregar. Si pusieramos una "w" estaria escribiendo, en vez de agregar
        f.write(name + "," + email + "," + address + "," + date + '\n')
    # Cada vez que se contesta el formulario, se van escribiendo las nuevas respuestas en el archivo form.text


    # Puedes guardar tus datos o enviarlos por correo electrónico
    return render_template('form_result.html', 
                           # Coloque aquí las variables que se van a enviar al archivo "form_result"
                           name=name,
                           email=email,
                           address=address,
                           date=date
                           )

app.run(debug=True)
