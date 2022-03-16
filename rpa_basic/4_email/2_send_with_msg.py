import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다." # 제목
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = "jhm1062@gmail.com" # 받는 사람

# 다수에게 발송할 경우 1
# msg["To"] = "1@gmail.com, 2@gmail.com"

# 다수에게 발생할 경우 2
# to_list = ["1@gmail.com", "2@gmail.com"]
# msg["To"] = ", ".join(to_list)

# 참조
# msg["Cc"] = "1@gmail.com"

# 비밀 참조
# msg["Bcc"] = "1@gmail.com"

msg.set_content("테스트 본문입니다.") # 본문

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)