from flask import Flask, request, render_template_string, redirect, url_for
import os
import re

app = Flask(__name__)

# Asegúrate de que el archivo flag.txt contiene la bandera
with open("flag.txt", "r") as f:
    FLAG = f.read().strip()

HTML_INDEX = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CTF Challenge</title>

    <style>
        body {
            background: #1e1e2f;
            color: #fff;
            font-family: 'Segoe UI', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .container {
            background: #2b2b40;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(0,0,0,0.4);
            width: 380px;
            text-align: center;
        }

        h1 {
            margin-bottom: 25px;
            font-size: 28px;
        }

        input[type="text"] {
            width: 90%;
            padding: 12px;
            margin-bottom: 20px;
            border: none;
            border-radius: 8px;
            font-size: 15px;
        }

        input[type="submit"] {
            width: 95%;
            padding: 12px;
            background: #6a5acd;
            border: none;
            border-radius: 8px;
            color: white;
            font-size: 16px;
            cursor: pointer;
            transition: 0.3s;
        }

        input[type="submit"]:hover {
            background: #7b6df2;
        }

        small {
            display: block;
            margin-top: 15px;
            color: #bdbddd;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>CTF Challenge</h1>

        <form method="POST" action="/result">
            <input type="text" name="input" placeholder="Prueba sqli, xss, ssti...">
            <input type="submit" value="Enviar">
        </form>

        <small>¿Podrás romperlo sin ser rickrolleado? 👀</small>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return HTML_INDEX


@app.route('/result', methods=['POST'])
def result():
    user_input = request.form.get('input')
    # Intentamos detectar un xss
    another_pattern = re.compile(r'<script>|</script>|alert|onerror|onload|<|>', re.IGNORECASE)
    
    if another_pattern.search(user_input):
        # si prueban xss se redirecciona
        return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    # Parte vulnerable (deliberadamente)
    template = f"""
    <!DOCTYPE html>
    <html>
    <body style="background:#1e1e2f; color:white; font-family:Segoe UI; padding:40px; font-size:22px;">
        Has introducido: {user_input}
    </body>
    </html>
    """

    return render_template_string(template)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
