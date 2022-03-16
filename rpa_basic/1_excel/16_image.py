from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb = Workbook()
ws = wb.active

img = Image(r"C:\Users\jhm10\Desktop\pg\파이썬\rpa_basic\1_excel\img.jpeg")

# C3 위치에 img.jpeg 파일의 이미지를 삽입
ws.add_image(img, "C3")

wb.save("sample_image.xlsx")