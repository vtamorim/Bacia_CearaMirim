from flask import Flask, request, jsonify
from email_validator import validate_email, EmailNotValidError
from email_sender import enviar_email
app = Flask(__name__)

from flask_cors import CORS
CORS(app)

@app.route("/api/contato", methods=["POST"])
def contato():
    data = request.json
    pri_nome = data.get("pri_nome")
    ult_nome = data.get("ult_nome")
    email = data.get("email")
    mensagem = data.get("mensagem")

    # validações
    if not pri_nome or not ult_nome or not email or not mensagem:
        return jsonify({"success": False, "error": "Preencha todos os campos."}), 400

    try:
        validate_email(email)
    except EmailNotValidError:
        return jsonify({"success": False, "error": "E-mail inválido."}), 400

    try:
        enviar_email(pri_nome, ult_nome, email, mensagem)
        return jsonify({"success": True, "message": "Mensagem enviada com sucesso!"})
    except Exception as e:
        print("Erro ao enviar e-mail:", e)
        return jsonify({"success": False, "error": "Erro ao enviar o e-mail."}), 500


if __name__ == "__main__":
    app.run(debug=True)
