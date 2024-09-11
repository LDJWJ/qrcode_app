import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# 앱 제목 설정
st.title("QR Code Generator")

# 사용자가 입력할 텍스트 또는 URL
input_data = st.text_input("Enter the text or URL to generate QR Code:")

# 버튼 클릭 시 QR 코드 생성
if st.button("Generate QR Code"):
    if input_data:
        # QR 코드 생성
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(input_data)
        qr.make(fit=True)

        # 이미지를 PIL 형식으로 변환
        img = qr.make_image(fill='black', back_color='white')

        # 이미지를 스트림으로 변환하여 화면에 표시
        img_buffer = BytesIO()
        img.save(img_buffer, format="PNG")
        st.image(img_buffer.getvalue(), caption="Generated QR Code", use_column_width=True)
    else:
        st.error("Please enter text or URL.")
