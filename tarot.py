import streamlit as st
import random
import os
import base64

# ===== 페이지 기본 설정 =====
st.set_page_config(page_title="저주받은 타로", page_icon="💀", layout="wide")

# ===== 공포 분위기 CSS 디자인 (강화 버전) =====
st.markdown("""
    <style>
    /* 전체 배경: 어두운 핏빛 그라데이션 */
    .stApp {
        background: radial-gradient(circle at center, #1a0000 0%, #000000 80%);
        color: #b0b0b0;
        font-family: 'Times New Roman', serif;
    }

    /* 제목: 핏빛 + 깜빡임 + 떨림 효과 */
    .title {
        text-align: center;
        color: #cc0000;
        font-size: 60px;
        font-weight: bold;
        text-shadow: 0 0 10px #ff0000, 0 0 20px #990000, 0 0 40px #660000;
        animation: flicker 3s infinite, shake 5s infinite;
        letter-spacing: 4px;
    }

    /* 부제목 */
    .subtitle {
        text-align: center;
        color: #777;
        font-size: 20px;
        font-style: italic;
        text-shadow: 0 0 5px #990000;
    }

    /* 깜빡이는 애니메이션 */
    @keyframes flicker {
        0%, 100% { opacity: 1; }
        45% { opacity: 1; }
        50% { opacity: 0.4; }
        55% { opacity: 1; }
        70% { opacity: 0.7; }
    }

    /* 미세하게 떨리는 애니메이션 */
    @keyframes shake {
        0%, 100% { transform: translate(0, 0); }
        25% { transform: translate(-1px, 1px); }
        50% { transform: translate(1px, -1px); }
        75% { transform: translate(-1px, -1px); }
    }

    /* 결과 박스: 핏빛 글로우 + 펄럭임 */
    .result-box {
        background-color: #0d0000;
        border: 2px solid #990000;
        border-radius: 8px;
        padding: 30px;
        margin-top: 25px;
        text-align: center;
        font-size: 24px;
        color: #ff3333;
        box-shadow: 0 0 30px #cc0000, inset 0 0 20px #330000;
        text-shadow: 0 0 8px #ff0000;
        animation: pulse 2s infinite;
    }

    /* 박스가 숨쉬듯 빛나는 효과 */
    @keyframes pulse {
        0%, 100% { box-shadow: 0 0 20px #990000, inset 0 0 15px #330000; }
        50% { box-shadow: 0 0 45px #ff0000, inset 0 0 25px #660000; }
    }

    /* 버튼 스타일: 핏빛 테두리 */
    .stButton > button {
        background-color: #1a0000;
        color: #cc0000;
        border: 1px solid #990000;
        border-radius: 5px;
        font-weight: bold;
        box-shadow: 0 0 8px #660000;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        background-color: #330000;
        color: #ff4444;
        box-shadow: 0 0 20px #ff0000;
        border: 1px solid #ff0000;
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

# ===== 타로 카드 데이터 (20장으로 대폭 확장!) =====
tarot_cards = [
    {"name": "💀 죽음의 카드", "fortune": "오늘 밤, 너의 뒤를 따라오는 것이 있다...", "image": "images/card1.png"},
    {"name": "🪞 거울의 카드", "fortune": "거울을 조심해라. 그 안의 네가 웃고 있을지도...", "image": "images/card2.png"},
    {"name": "👤 그림자 카드", "fortune": "혼자라고 생각했지? 방 안엔 항상 누군가 있었다.", "image": "images/card3.png"},
    {"name": "🤫 침묵의 카드", "fortune": "이름을 부르는 소리를 들어도 절대 돌아보지 마라.", "image": "images/card4.png"},
    {"name": "🍀 행운의 카드", "fortune": "행운! 오늘은 아무 일도 일어나지 않는다... 아마도.", "image": "images/card5.png"},
    {"name": "🗣️ 속삭임 카드", "fortune": "잠들기 전, 귓가의 속삭임에 답하지 마라.", "image": "images/card6.png"},
    {"name": "🚪 문의 카드", "fortune": "닫아둔 문이 열려 있다면, 그건 네가 연 게 아니다.", "image": "images/card7.png"},
    {"name": "🕒 시계의 카드", "fortune": "새벽 3시 33분, 절대 시계를 보지 마라.", "image": "images/card8.png"},
    {"name": "🩸 피의 카드", "fortune": "손에 묻은 붉은 것을, 너는 기억하지 못할 것이다.", "image": "images/card9.png"},
    {"name": "🪆 인형의 카드", "fortune": "네 방의 인형은, 매일 밤 자리를 바꾼다.", "image": "images/card10.png"},
    {"name": "🌑 어둠의 카드", "fortune": "불을 끄는 순간, 어둠 속의 눈이 너를 본다.", "image": "images/card11.png"},
    {"name": "👁️ 응시의 카드", "fortune": "창밖을 보지 마라. 무언가가 너를 마주 보고 있다.", "image": "images/card12.png"},
    {"name": "🦴 백골의 카드", "fortune": "땅 밑에서 누군가 너의 이름을 새기고 있다.", "image": "images/card13.png"},
    {"name": "🕯️ 촛불의 카드", "fortune": "촛불이 저절로 꺼진다면, 숨을 멈추고 기다려라.", "image": "images/card14.png"},
    {"name": "📞 통화의 카드", "fortune": "발신번호 없는 전화를 받았다면, 이미 늦었다.", "image": "images/card15.png"},
    {"name": "🛏️ 침대의 카드", "fortune": "침대 밑에서 들리는 숨소리는 너의 것이 아니다.", "image": "images/card16.png"},
    {"name": "🎭 가면의 카드", "fortune": "웃는 얼굴 뒤에 무엇이 있는지, 묻지 마라.", "image": "images/card17.png"},
    {"name": "🌧️ 폭우의 카드", "fortune": "비 내리는 밤, 젖지 않은 발자국이 따라온다.", "image": "images/card18.png"},
    {"name": "⛓️ 사슬의 카드", "fortune": "지하실 소리는 무시해라. 그것은 풀려나길 원한다.", "image": "images/card19.png"},
    {"name": "🕷️ 거미의 카드", "fortune": "오늘 밤 너의 입 속으로 무언가 기어들어갈 것이다.", "image": "images/card20.png"},
]

CARD_BACK = "images/back.png"

# ===== 제목 영역 =====
st.markdown('<p class="title">💀 저주받은 타로 💀</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">운명의 카드를 한 장 선택하라... 되돌릴 수 없으니.</p>', unsafe_allow_html=True)
st.write("")

# ===== session_state 초기화 =====
if "result" not in st.session_state:
    st.session_state.result = None

# 화면에 보여줄 카드 개수와 한 줄에 놓을 카드 수
num_cards = 12       # 보여줄 카드 총 개수
cards_per_row = 6    # 한 줄에 몇 장씩 배치할지

# ===== 카드 선택 영역 (여러 줄로 배치) =====
card_index = 0
for row in range(0, num_cards, cards_per_row):
    cols = st.columns(cards_per_row)
    for col in cols:
        if card_index < num_cards:
            with col:
                if os.path.exists(CARD_BACK):
                    st.image(CARD_BACK, use_container_width=True)
                if st.button(f"🂠 {card_index+1}", key=f"card_{card_index}"):
                    st.session_state.result = random.choice(tarot_cards)
                    play_sound("sounds/creepy.mp3")
            card_index += 1

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
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔄 다시 운명을 마주하기"):
            st.session_state.result = None
            st.rerun()
