import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def enviar_email(pri_nome, ult_nome, email, mensagem):
    REMETENTE = "vthero89@gmail.com"  
    SENHA = "wlvm zrki cfgc aquo"         
    DESTINO = "pg96081@gmail.com"    

    msg = MIMEMultipart()
    msg["From"] = REMETENTE
    msg["To"] = DESTINO
    msg["Subject"] = f"Contato de {pri_nome} {ult_nome}"
    msg.add_header("Reply-To", email)

    corpo_html = f"""
    <h2>Novo contato recebido</h2>
    <p><strong>Nome:</strong> {pri_nome} {ult_nome}</p>
    <p><strong>E-mail:</strong> {email}</p>
    <p><strong>Mensagem:</strong><br>{mensagem}</p>
    """

    msg.attach(MIMEText(corpo_html, "html"))

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(REMETENTE, SENHA)
        smtp.send_message(msg)
