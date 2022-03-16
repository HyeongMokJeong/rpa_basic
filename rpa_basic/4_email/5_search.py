from imap_tools import MailBox
from account import *

# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")
# mailbox.logout()

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # 전체 메일 가져오기
    # for msg in mailbox.fetch():# (limit=5, reverse=True) 
    #     print("[{}] {}".format(msg.from_, msg.subject))


    # 읽지 않은 메일 가져오기
    # for msg in mailbox.fetch('(UNSEEN)'): 
    #     print("[{}] {}".format(msg.from_, msg.subject))


    # 특정인이 보낸 메일 가져오기
    # for msg in mailbox.fetch('(FROM jhm1062@gmail.com)', limit=3, reverse=True): 
    #     print("[{}] {}".format(msg.from_, msg.subject))


    # 특정 글자를 포함하는 메일 가져오기 (본문, 내용)
    # for msg in mailbox.fetch('(TEXT "test mail")'): 
        # 띄어쓰기로 구분하여 test, mail 각각을 포함하는 메일을 찾음
    #     print("[{}] {}".format(msg.from_, msg.subject))


    # 특정 글자를 포함하는 메일(제목만)
    # for msg in mailbox.fetch('(SUBJECT "test mail")'): 
    #      print("[{}] {}".format(msg.from_, msg.subject))


    # 한글 필터링
    # for msg in mailbox.fetch(limit=5, reverse=True):
    #     if "테스트" in msg.subject: 
    #         print("[{}] {}".format(msg.from_, msg.subject))


    # 특정날짜 이후로 보낸 메일 가져오기
    # for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020)', limit=5, reverse=True): 
    #     print("[{}] {}".format(msg.from_, msg.subject))


    # 특정날짜에 보낸 메일 가져오기
    # for msg in mailbox.fetch('(ON 07-Nov-2020)', limit=5, reverse=True): 
    #     print("[{}] {}".format(msg.from_, msg.subject))


    # 두 가지 이상의 조건을 모두 만족하는 메일 (AND 조건)
    # for msg in mailbox.fetch('(ON 08-Jul-2021 SUBJECT "test mail")', limit=5, reverse=True): # 특정날짜 이후로 보낸 메일 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))


    # 두 가지 이상의 조건 중 하나라도 만족하는 메일 (OR 조건)
    for msg in mailbox.fetch('(OR ON 08-Jul-2021 SUBJECT "test mail")', limit=5, reverse=True): # 특정날짜 이후로 보낸 메일 가져오기
        print("[{}] {}".format(msg.from_, msg.subject))

