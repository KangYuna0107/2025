import streamlit as st
import random

# ==============================
# 여행지 데이터베이스 (각 기분별 20개)
# ==============================
travel_recommendations = {
    "행복 😀": [
        ("제주도", "성산일출봉", "제주 흑돼지"),
        ("부산", "광안리 해변", "돼지국밥"),
        ("전주", "한옥마을", "비빔밥"),
        ("경주", "불국사", "황남빵"),
        ("여수", "돌산대교", "게장백반"),
        ("순천", "순천만 국가정원", "짱뚱어탕"),
        ("통영", "한려수도", "굴 요리"),
        ("서울", "남산타워", "치킨"),
        ("속초", "대포항", "오징어순대"),
        ("강릉", "경포대", "초당두부"),
        ("부여", "백제문화단지", "연잎밥"),
        ("안동", "하회마을", "안동찜닭"),
        ("대구", "팔공산", "막창"),
        ("포항", "호미곶", "과메기"),
        ("인천", "월미도", "짬뽕"),
        ("울산", "대왕암 공원", "고래고기"),
        ("창원", "진해 벚꽃길", "가자미회"),
        ("김해", "수로왕릉", "돼지갈비"),
        ("군산", "선유도", "짬뽕"),
        ("광주", "무등산", "송정떡갈비")
    ],
    # 나머지 기분 데이터도 동일하게...
    # 우울 😔, 지침 😵, 따분함 🥱, 모험 🤩 생략
}

# ==============================
# 세션 상태 (중복 방지용)
# ==============================
if "used_places" not in st.session_state:
    st.session_state.used_places = {m: [] for m in travel_recommendations.keys()}

# ==============================
# CSS 꾸미기
# ==============================
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #fceabb, #f8b500);
    }
    .title {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        background: -webkit-linear-gradient(45deg, #ff4e50, #f9d423);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 30px;
    }
    .card {
        background-color: white;
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 5px 5px 20px rgba(0,0,0,0.2);
    }
    .subtitle {
        font-size: 24px;
        font-weight: bold;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================
# 앱 UI
# ==============================
st.markdown("<div class='title'>🌸 기분 따라 떠나는 국내 여행 🌸</div>", unsafe_allow_html=True)

mood = st.selectbox("👉 오늘 기분을 선택하세요!", list(travel_recommendations.keys()))

if st.button("✨ 추천받기 ✨"):
    candidates = [p for p in travel_recommendations[mood] if p not in st.session_state.used_places[mood]]
    
    if not candidates:
        st.warning("해당 기분의 모든 여행지를 추천했어요! 🔄 다른 기분을 선택해보세요.")
    else:
        choice = random.choice(candidates)
        st.session_state.used_places[mood].append(choice)

        지역, 관광지, 음식 = choice

        # 카드 형태 출력 - 제목 = 지역 이름
        st.markdown(f"""
            <div class="card">
                <div class="subtitle">{지역}</div>
                <p>{지역}은 한국을 대표하는 여행지예요.<br>
                자연과 문화가 공존하며 사계절 내내 다양한 매력이 있습니다.<br>
                언제 방문해도 특별한 경험을 선사해요.<br>
                행복한 추억을 만들기에 딱 좋은 곳입니다.</p>
            </div>
        """, unsafe_allow_html=True)

        # 카드 형태 출력 - 제목 = 관광지 이름
        st.markdown(f"""
            <div class="card">
                <div class="subtitle">{관광지}</div>
                <p>{관광지}는 {지역}에서 꼭 가봐야 할 명소입니다.<br>
                아름다운 풍경과 특별한 체험을 제공합니다.<br>
                현지 문화를 더 깊이 느낄 수 있어요.<br>
                사진 찍기에도 최고의 장소랍니다.</p>
            </div>
        """, unsafe_allow_html=True)

        # 카드 형태 출력 - 제목 = 음식 이름
        st.markdown(f"""
            <div class="card">
                <div class="subtitle">{음식}</div>
                <p>{음식}은 {지역}의 대표 음식이에요.<br>
                현지에서만 느낄 수 있는 특별한 맛이 있습니다.<br>
                여행의 즐거움을 더해주는 별미랍니다.<br>
                {지역}에 간다면 꼭 맛보세요!</p>
            </div>
        """, unsafe_allow_html=True)
