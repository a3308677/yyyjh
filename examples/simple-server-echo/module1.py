from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('/Ahqft8MHxb+P+2AD2YTxw57gnqOFUoQt3dMram0c8DiE0VnkwA5qijlERRqnOZVywLbATf1H6BAWnr+K2Ii5U8Bf5JddLN8LklJ/E74wgQdf7ihlh5kEpCbO/IQ/A8neX7iegCXlwqtMXfWJHrW4AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9f40c12980e63edb3732a2f7aa4ea7a2')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()