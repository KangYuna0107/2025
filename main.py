import streamlit as st
import random

# ==============================
# 여행지 데이터베이스 (이미지 추가)
# ==============================
travel_recommendations = {
    "행복 😀": [
        ("제주도", "성산일출봉", "제주 흑돼지",
         "https://images.unsplash.com/photo-1600585152220-90363fe7e115"),  # 제주
        ("부산", "광안리 해변", "돼지국밥",
         "https://images.unsplash.com/photo-1590031904235-c57f92dbda51"),  # 부산
        ("전주", "한옥마을", "비빔밥",
         "https://images.unsplash.com/photo-1567911895159-7e31f73aa8b8"),  # 전주
        ("경주", "불국사", "황남빵",
         "https://images.unsplash.com/photo-1637844529056-bc0df2a444ef"),  # 경주
        ("여수", "돌산대교", "게장백반",
         "https://images.unsplash.com/photo-1575123668916-1c05dbb7b9d2"),  # 여수
    ],
    "우울 😔": [
        ("강릉", "안목 해변 카페거리", "커피",
         "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"),  # 강릉
        ("여수", "오동도", "게장백반",
         "https://images.unsplash.com/photo-1534951009808-766178b47a4f"),
        ("군산", "근대문화거리", "짬뽕",
         "https://images.unsplash.com/photo-1504615755583-2916b52192d0"),
        ("속초", "설악산 케이블카", "오징어순대",
         "https://images.unsplash.com/photo-1501785888041-af3ef285b470"),
        ("통영", "동피랑 벽화마을", "꿀빵",
         "https://images.unsplash.com/photo-1620662736805-6e9d8d05f9a2"),
    ],
    "지침 😵": [
        ("담양", "죽녹원", "죽순 요리",
         "https://images.unsplash.com/photo-1536333197843-cd3d6e8a08b0"),
        ("춘천", "남이섬", "닭갈비",
         "https://images.unsplash.com/photo-1570018144715-624cb190bfcf"),
        ("보성", "녹차밭", "녹차 아이스크림",
         "https://images.unsplash.com/photo-1523906834658-6e24ef2386f9"),
        ("가평", "아침고요수목원", "잣죽",
         "https://images.unsplash.com/photo-1523978591478-c753949ff840"),
        ("태안", "꽃지 해수욕장", "꽃게찜",
         "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"),
    ],
    "따분함 🥱": [
        ("서울", "홍대 거리", "길거리 음식",
         "https://images.unsplash.com/photo-1531297484001-80022131f5a1"),
        ("인천", "차이나타운", "짜장면",
         "https://images.unsplash.com/photo-1573804633927-bfcbcd909acd"),
        ("대구", "동성로", "막창",
         "https://images.unsplash.com/photo-1608500215661-7972ed85e8b4"),
        ("광주", "양림동 문화마을", "송정떡갈비",
         "https://images.unsplash.com/photo-1558185348-d2a69c8db08e"),
        ("부산", "자갈치 시장", "회",
         "https://images.unsplash.com/photo-1586448483651-9f862c48f98f"),
    ],
    "모험 🤩": [
        ("속초", "설악산 등반", "오징어순대",
         "https://images.unsplash.com/photo-1501785888041-af3ef285b470"),
        ("평창", "래프팅 체험", "한우",
         "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"),
        ("제주도", "우도 자전거 여행", "땅콩 아이스크림",
         "https://images.unsplash.com/photo-1600585152220-90363fe7e115"),
        ("단양", "패러글라이딩", "마늘 만두",
         "https://images.unsplash.com/photo-1529927066849-efc527381d6a"),
        ("무주", "덕유산 스키장", "산채비빔밥",
         "https://images.unsplash.com/photo-1516569422785-fb3ee61a3647"),
    ],
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
        margin-bottom: 10px;
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

        지역, 관광지, 음식, 이미지 = choice

        # 카드 형태 출력 - 이미지 + 텍스트
        st.markdown(f"""
            <div class="card">
                <div class="subtitle">📍 {지역}</div>
                <p>{지역}은 한국을 대표하는 여행지예요.<br>
                자연과 문화가 공존하며 사계절 내내 다양한 매력이 있습니다.<br>
                언제 방문해도 특별한 경험을 선사해요.<br>
                행복한 추억을 만들기에 딱 좋은 곳입니다.</p>
            </div>
        """, unsafe_allow_html=True)
        st.image(이미지, use_container_width=True)

        st.markdown(f"""
            <div class="card">
                <div class="subtitle">🏞 관광지 - {관광지}</div>
                <p>{관광지}는 {지역}에서 꼭 가봐야 할 명소입니다.<br>
                아름다운 풍경과 특별한 체험을 제공합니다.<br>
                현지 문화를 더 깊이 느낄 수 있어요.<br>
                사진 찍기에도 최고의 장소랍니다.</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
            <div class="card">
                <div class="subtitle">🍴 음식 - {음식}</div>
                <p>{음식}은 {지역}의 대표 음식이에요.<br>
                현지에서만 느낄 수 있는 특별한 맛이 있습니다.<br>
                여행의 즐거움을 더해주는 별미랍니다.<br>
                {지역}에 간다면 꼭 맛보세요!</p>
            </div>
        """, unsafe_allow_html=True)
