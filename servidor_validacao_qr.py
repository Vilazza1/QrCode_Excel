
from flask import Flask, render_template_string
import os
import json

app = Flask(__name__)
ARQUIVO_USADOS = "usados.json"

# Garante que o arquivo de controle exista
if not os.path.exists(ARQUIVO_USADOS):
    with open(ARQUIVO_USADOS, "w") as f:
        json.dump([], f)

@app.route("/")
def home():
    return "✅ Servidor de Validação de QRCode ativo!"

@app.route("/validar/<codigo>")
def validar_qrcode(codigo):
    # Lê códigos usados
    with open(ARQUIVO_USADOS, "r") as f:
        usados = json.load(f)

    if codigo in usados:
        mensagem = "⚠️ QRCODE JÁ USADO!<br><small>Este código já foi validado anteriormente.</small>"
        cor = "#ff4d4d"
    else:
        mensagem = "✅ QRCODE VÁLIDO!<br><small>Bem-vindo ao evento 🎉</small>"
        usados.append(codigo)
        with open(ARQUIVO_USADOS, "w") as f:
            json.dump(usados, f, indent=4)
        cor = "#4CAF50"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Validação QRCode</title>
        <style>
            body {{ font-family: Arial, sans-serif; background: #f7f7f7; text-align: center; padding: 50px; }}
            .box {{ background: {cor}; padding: 30px; border-radius: 12px; color: white; font-size: 24px; max-width: 500px; margin: auto; }}
        </style>
    </head>
    <body>
        <div class="box">{mensagem}</div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
