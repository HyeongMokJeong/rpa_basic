# import logging

# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")
# # level를 포함한 상위 레벨 로그만 출력

# # 로그 레벨
# # debug < info < warning < error < critical
# logging.debug("아 이거 누가 짠거야")
# logging.info("자동화 수행 준비")
# logging.warning("이 스크립트는 구형입니다.")
# logging.error("에러가 발생하였습니다.")
# logging.critical("복구가 불가능한 문제가 발생했습니다.")

# 터미널과 파일에 함꼐 로그 남기기
import logging
from datetime import datetime
# 시간, 로그 레벨, 메세지 순으로 작성
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s") 
logger = logging.getLogger()
# 로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림
StreamHandler = logging.StreamHandler()
StreamHandler.setFormatter(logFormatter)
logger.addHandler(StreamHandler)

# 파일
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log")
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("로그를 남겨보는 테스트를 진행합니다.")