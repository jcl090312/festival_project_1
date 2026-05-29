import streamlit as st
import random
import os
import base64

# ===== 페이지 기본 설정 =====
st.set_page_config(page_title="공포 타로", page_icon="🔮", layout="centered")

# ===== 공포 분위기 CSS 디자인 =====
st.markdown("""
    <style>
    .stApp {
        background-color: #0a0a0a;
        color: #d4d4d4;
    }
    .title {
        text-align: center;
        color: #b30000;
        font-size: 48px;
        font-weight: bold;
        text-shadow: 2px 2px 8px #ff0000;
    }
    .subtitle {
        text-align: center;
        color: #888;
        font-size: 18px;
    }
    .result-box {
        background-color: #1a1a1a;
        border: 2px solid #b30000;
        border-radius: 10px;
        padding: 25px;
        margin-top: 20px;
        text-align: center;
        font-size: 22px;
        color: #ff4d4d;
        box-shadow: 0px 0px 20px #b30000;
    }
    </style>
""", unsafe_allow_html=True)

# ===== 효과음 자동 재생 함수 =====
def play_sound(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
                <audio autoplay>
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
            """
            st.markdown(md, unsafe_allow_html=True)

# ===== 타로 카드 데이터 =====
tarot_cards = [
    {"name": "🃏 죽음의 카드", "fortune": "오늘 밤, 너의 뒤를 따라오는 것이 있다...", "image": "images/card1.png"},
    {"name": "🃏 거울의 카드", "fortune": "거울을 조심해라. 그 안의 네가 웃고 있을지도...", "image": "images/card2.png"},
    {"name": "🃏 그림자 카드", "fortune": "혼자라고 생각했지? 방 안엔 항상 누군가 있었다.", "image": "images/card3.png"},
    {"name": "🃏 침묵의 카드", "fortune": "오늘은 이름을 부르는 소리를 들어도 절대 돌아보지 마라.", "image": "images/card4.png"},
    {"name": "🃏 행운의 카드", "fortune": "행운! 오늘은 아무 일도 일어나지 않는다... 아마도.", "image": "images/card5.png"},
    {"name": "🃏 속삭임 카드", "fortune": "잠들기 전, 귓가의 속삭임에 답하지 마라.", "image": "images/card6.png"},
    {"name": "🃏 문의 카드", "fortune": "닫아둔 문이 열려 있다면, 그건 네가 연 게 아니다.", "image": "images/card7.png"},
    {"name": "🃏 시계의 카드", "fortune": "새벽 3시 33분, 절대 시계를 보지 마라.", "image": "images/card8.png"},
    {"name": "🃏 피의 카드", "fortune": "손에 묻은 붉은 것을, 너는 기억하지 못할 것이다.", "image": "images/card9.png"},
    {"name": "🃏 인형의 카드", "fortune": "네 방의 인형은, 매일 밤 자리를 바꾼다.", "image": "images/card10.png"},
]

CARD_BACK = "images/back.png"

# ===== 제목 영역 =====
st.markdown('<p class="title">🔮 저주받은 타로 🔮</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">운명의 카드를 한 장 선택하라... 되돌릴 수 없으니.</p>', unsafe_allow_html=True)
st.write("")

# ===== session_state 초기화 =====
if "result" not in st.session_state:
    st.session_state.result = None

num_cards = 5  # 화면에 보여줄 카드 개수

# ===== 카드 선택 영역 =====
cols = st.columns(num_cards)
for i in range(num_cards):
    with cols[i]:
        if os.path.exists(CARD_BACK):
            st.image(CARD_BACK, use_container_width=True)
        if st.button(f"카드 {i+1}", key=f"card_{i}"):
            st.session_state.result = random.choice(tarot_cards)
            play_sound("sounds/creepy.mp3")

# ===== 결과 표시 영역 =====
if st.session_state.result:
    result = st.session_state.result

    if os.path.exists(result["image"]):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(result["image"], use_container_width=True)

    st.markdown(f"""
        <div class="result-box">
            <h2>{result['name']}</h2>
            <p>{result['fortune']}</p>
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    if st.button("🔄 다시 운명을 마주하기"):
        st.session_state.result = None
        st.rerun()
