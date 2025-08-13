import streamlit as st
import random

# 기분별 여행지 데이터
travel_data = {
    "행복해요 😊": [
        {"name": "제주도", "desc": "푸른 바다와 한라산의 조화!", "img": "https://cdn.pixabay.com/photo/2016/11/29/02/29/korea-1868860_1280.jpg"},
        {"name": "부산 해운대", "desc": "활기찬 해변과 맛있는 해산물", "img": "https://cdn.pixabay.com/photo/2017/04/20/21/21/beach-2246261_1280.jpg"}
    ],
    "우울해요 😔": [
        {"name": "강원도 속초", "desc": "조용한 바닷가와 설악산의 평온함", "img": "https://cdn.pixabay.com/photo/2017/09/04/18/59/south-korea-2710856_1280.jpg"},
        {"name": "경주", "desc": "역사와 고즈넉한 분위기 속 힐링", "img": "https://cdn.pixabay.com/photo/2018/04/25/22/46/korea-3351995_1280.jpg"}
    ],
    "모험이 필요해요 🚀": [
        {"name": "네팔 포카라", "desc": "히말라야 트레킹의 시작점", "img": "https://cdn.pixabay.com/photo/2016/09/03/16/40/nepal-1649299_1280.jpg"},
        {"name": "태국 치앙마이", "desc": "액티비티와 문화가 함께", "img": "https://cdn.pixabay.com/photo/2016/02/19/10/00/chiang-mai-1209359_1280.jpg"}
    ]
}

st.title("🌍 기분별 여행지 추천기")

mood = st.selectbox("지금 기분을 선택하세요", list(travel_data.keys()))

if st.button("추천 받기"):
    choice = random.choice(travel_data[mood])
    st.subheader(f"✈️ {choice['name']}")
    st.image(choice['img'], use_column_width=True)
    st.write(choice['desc'])
    st.markdown(f"[Google 지도에서 보기](https://www.google.com/maps/search/{choice['name']})")
