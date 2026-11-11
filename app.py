from flask import Flask

app = Flask(__name__)

def sumar(a, b):
    return a + b

@app.route("/")
def inicio():
    return "Aplicacion CI/CD funcionando en Kubernetes"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
