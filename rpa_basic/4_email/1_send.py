import smtplib
from account import *

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() # 연결이 잘 수립되는지 확인
    smtp.starttls() # 모든 내용 암호화
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인

    subject = "test mail" # 제목
    body = "mail body" # 내용

    msg = f"Subject: {subject}\n{body}"
    smtp.sendmail(EMAIL_ADDRESS, "jhm1062@gmail.com", msg)
    # 발신자, 수신자, 정해진 형식의 메세지