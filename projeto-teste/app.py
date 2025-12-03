from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# CONFIGURAÇÕES DO EMAIL
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "vthero89@gmail.com"  # CORRIGIDO
SMTP_PASS = "quss nbgy esgp zucv "  # TEM QUE SER A SENHA DE APP DO GMAIL

TO_EMAIL = "amorim.victor@escolar.ifrn.edu.br"  # quem recebe o contato


@app.route("/")
def index():
    return render_template("contact.html")


@app.route("/send", methods=["POST"])
def send_email():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    subject = data.get("subject")
    message = data.get("message")

    body = f"""
Nome: {name}
E-mail: {email}

Mensagem:
{message}
"""

    try:
        msg = MIMEText(body)
        msg["Subject"] = f"[Contato] {subject}"
        msg["From"] = SMTP_USER
        msg["To"] = TO_EMAIL

        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(SMTP_USER, TO_EMAIL, msg.as_string())
        server.quit()

        return "Mensagem enviada com sucesso!"

    except Exception as e:
        print("Erro:", e)
        return "Erro ao enviar a mensagem", 500


if __name__ == "__main__":
    app.run(debug=True)








