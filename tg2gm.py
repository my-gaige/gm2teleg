import imaplib
import telegram

# Настройки
EMAIL = "magnitka.rita@gmail.com"
PASSWORD = "Qweasd321!"  # для Gmail нужен App Password
BOT_TOKEN = "7600418424:AAFe-JjejJNmeJ9ZzE-ZwlS7Br1OspBA530"
CHAT_ID = "5124503377"

bot = telegram.Bot(token=BOT_TOKEN)

def check_mail():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")
    
    status, messages = mail.search(None, "UNSEEN")
    if status != "OK": return
    
    for num in messages[0].split():
        _, msg = mail.fetch(num, "(BODY[HEADER])")
        headers = msg[0][1].decode()
        
        # Парсим отправителя и тему
        from_line = [h for h in headers.split("\r\n") if "From:" in h][0]
        subject = [h for h in headers.split("\r\n") if "Subject:" in h][0]
        
        bot.send_message(
            chat_id=CHAT_ID,
            text=f"✉️ Новое письмо\n{from_line}\n{subject}"
        )

if __name__ == "__main__":
    check_mail()
    