import streamlit as st
import random

# ===== 페이지 기본 설정 =====
st.set_page_config(page_title="공포 타로", page_icon="🔮", layout="centered")

# ===== 공포 분위기 CSS 디자인 =====
st.markdown("""
    <style>
    /* 전체 배경을 어둡게 */
    .stApp {
        background-color: #0a0a0a;
        color: #d4d4d4;
    }
    /* 제목 스타일 */
    .title {
        text-align: center;
        color: #b30000;
        font-size: 48px;
        font-weight: bold;
        text-shadow: 2px 2px 8px #ff0000;
    }
    /* 설명 글씨 */
    .subtitle {
        text-align: center;
        color: #888;
        font-size: 18px;
    }
    /* 운세 결과 박스 */
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

# ===== 운세 데이터 (자유롭게 추가/수정하세요!) =====
tarot_cards = [
    {"name": "🃏 죽음의 카드", "fortune": "오늘 밤, 너의 뒤를 따라오는 것이 있다..."},
    {"name": "🃏 거울의 카드", "fortune": "거울을 조심해라. 그 안의 네가 웃고 있을지도..."},
    {"name": "🃏 그림자 카드", "fortune": "혼자라고 생각했지? 방 안엔 항상 누군가 있었다."},
    {"name": "🃏 침묵의 카드", "fortune": "오늘은 이름을 부르는 소리를 들어도 절대 돌아보지 마라."},
    {"name": "🃏 행운의 카드", "fortune": "행운! 오늘은 아무 일도 일어나지 않는다... 아마도."},
    {"name": "🃏 속삭임 카드", "fortune": "잠들기 전, 귓가의 속삭임에 답하지 마라."},
    {"name": "🃏 문의 카드", "fortune": "닫아둔 문이 열려 있다면, 그건 네가 연 게 아니다."},
    {"name": "🃏 시계의 카드", "fortune": "새벽 3시 33분, 절대 시계를 보지 마라."},
]

# ===== 제목 영역 =====
st.markdown('<p class="title">🔮 저주받은 타로 🔮</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">운명의 카드를 한 장 선택하라... 되돌릴 수 없으니.</p>', unsafe_allow_html=True)
st.write("")  # 여백

# ===== 카드 선택 영역 =====
# 화면에 보여줄 카드 개수
num_cards = 5

# 컬럼을 나눠서 카드 버튼을 가로로 배치
cols = st.columns(num_cards)

# session_state로 선택된 운세를 저장 (새로고침해도 유지)
if "result" not in st.session_state:
    st.session_state.result = None

# 카드 버튼 만들기
for i in range(num_cards):
    with cols[i]:
        if st.button(f"🂠\n카드 {i+1}", key=f"card_{i}"):
            # 버튼을 누르면 랜덤으로 운세 선택
            st.session_state.result = random.choice(tarot_cards)

# ===== 결과 표시 영역 =====
if st.session_state.result:
    result = st.session_state.result
    st.markdown(f"""
        <div class="result-box">
            <h2>{result['name']}</h2>
            <p>{result['fortune']}</p>
        </div>
    """, unsafe_allow_html=True)

    # 다시 뽑기 버튼
    st.write("")
    if st.button("🔄 다시 운명을 마주하기"):
        st.session_state.result = None
        st.rerun()
