import streamlit as st
import sqlite3
from datetime import datetime

# DB 연결
conn = sqlite3.connect("diary.db", check_same_thread=False)
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS diary (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    content TEXT
)
""")
conn.commit()

st.title("📖 모두의 일기장")

# 입력창
content = st.text_area("오늘의 일기를 작성해 주세요")

if st.button("등록하기"):
    if content.strip():
        cur.execute("INSERT INTO diary (date, content) VALUES (?, ?)", 
                    (datetime.now().strftime("%Y-%m-%d %H:%M"), content.strip()))
        conn.commit()
        st.success("일기가 등록되었습니다!")
    else:
        st.warning("내용을 입력해주세요.")

st.subheader("📜 최근 일기")
cur.execute("SELECT date, content FROM diary ORDER BY id DESC")
rows = cur.fetchall()

for date, content in rows:
    st.markdown(f"**{date}**")
    st.write(content)
    st.markdown("---")
