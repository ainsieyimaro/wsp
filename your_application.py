from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

your_application = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    message_body = request.form.get('Body', '')
    resp = MessagingResponse()

    # Aquí puedes añadir la lógica para responder a los mensajes recibidos
    if message_body.lower() == 'hola':
        resp.message("¡Hola! ¿Cómo puedo ayudarte?")
    else:
        resp.message("Lo siento, no entendí ese mensaje.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
