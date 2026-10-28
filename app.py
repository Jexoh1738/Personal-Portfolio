"""
CS 365 - Applied AI | Autobiography and Portfolio App
Everything marked  TODO  is yours to fill in.
"""
import os
from datetime import date

import pandas as pd
import streamlit as st
from PIL import Image, ImageDraw

import streamlit.components.v1 as components

from theme import apply_theme


NAME = "Mark Lou A. Villagonzalo"
SECTION = "F2"
PROGRAM = "BS Computer Science"
YEAR_LEVEL = "3rd Year"
SCHOOL = "Cebu Institute of Technology University"
TAGLINE = "I'm willing and sometimes able"
EMAIL = "marklou.villagonzalo@cit.edu"
GITHUB = "https://github.com/Jexoh1738"
PHOTO_FILE = "profile.jpg"  

SHORT_BIO = "I am going through all of my classes learning as much as I can. Taking this semester day by day, enjoying life and academics."

PLAYLIST_URL = "https://www.youtube.com/embed/watch?v=zBKKZQkMHlA&list=RDzBKKZQkMHlA&start_radio=1&rv=zBKKZQkMHlA"


AUTOBIOGRAPHY = {
    "Background": "Growing up from a not so well off family, I learned to be resourceful and determined.",
    "Education": "University of San Carlos - South Campus, Saint Louis University, Cebu Institute of Technology University",
    "Interests": "Gaming, Programming, Reading Manga, Writing, Billiards, and Learning new things.",
    "Goals": "Working and helping out my family, happy and content with life, and being able to help others in need.",
}

MILESTONES = [
    {"Year": 1999, "Milestone": "Born in Cebu City, Philippines"},
    {"Year": 2012, "Milestone": "Finished elementary school at University of San Carlos - South Campus"},
    {"Year": 2017, "Milestone": "Finished high school at Saint Louis University, First ever batch of Senior High School"},
    {"Year": 2019, "Milestone": "Started college at Cebu Institute of Technology University, taking up Computer Science"},
    {"Year": 2020, "Milestone": "Continued college at Saint Louis University"},
    {"Year": 2024, "Milestone": "Went back to Cebu Institute of Technology University to continue my studies in Computer Science"},
]

# Rate yourself honestly, 1 (beginner) to 10 (expert). Replace names and numbers.
SKILLS = pd.DataFrame(
    [
        {"Skill": "Python", "Category": "Programming", "Level": 7},
        {"Skill": "SQL", "Category": "Programming", "Level": 5},
        {"Skill": "HTML/CSS", "Category": "Web", "Level": 6},
        {"Skill": "Java", "Category": "Programming", "Level": 6},
        {"Skill": "C", "Category": "Programming", "Level": 9},
        {"Skill": "C++", "Category": "Programming", "Level": 8},
        {"Skill": "C#", "Category": "Programming", "Level": 7},
        {"Skill": "Machine Learning", "Category": "Data", "Level": 4},
        {"Skill": "Communication", "Category": "Soft Skills", "Level": 8},
        {"Skill": "Teamwork", "Category": "Soft Skills", "Level": 9},
    ]
)  

PROJECTS = [
    {
        "title": "CivicGuard",
        "type": "App",
        "role": "Backend Developer",
        "tools": ["Java"], 
        "year": 2025,
        "description": "An app that helps citizens and LGUs report and track issues in their communities during calamities.",
        "outcome": "Won best idea in our class",
        "link": "https://github.com/kworuu/CivicGuard",
    },
    {
        "title": "Telegram Bot",
        "type": "Management Tool",
        "role": "Lead Developer",
        "tools": ["Python"],  
        "year": 2025,
        "description": "A bot for managing and automating tasks via Telegram group.",
        "outcome": "Improved efficiency in group management",
        "link": "https://github.com/Jexoh1738/TelegramBot",
    },
    {
        "title": "AlgoMastery",
        "type": "Mobile App",
        "role": "Lead Developer",
        "tools": ["Kotlin"],
        "year": 2025,
        "description": "A mobile app for mastering algorithms and data structures, specifically designed for students taking up the subject.",
        "outcome": "Working but not fully deployable yet, still in development",
        "link": "https://github.com/Jexoh1738/AlgoMaster_Final",
    },
]

st.set_page_config(
    page_title=f"{NAME} | Portfolio",
    page_icon="Portfolio",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_theme()

st.session_state.setdefault("likes", 0)
st.session_state.setdefault("feedback_log", [])


def load_photo():
    """Show your photo if profile.jpg exists, else a labeled stand-in."""
    if os.path.exists(PHOTO_FILE):
        return Image.open(PHOTO_FILE), f"This is me"
    img = Image.new("RGB", (400, 400), "#2b6cb0")
    d = ImageDraw.Draw(img)
    d.ellipse((130, 70, 270, 210), fill="white")
    d.ellipse((70, 230, 330, 480), fill="white")
    d.text((120, 370), "PHOTO STAND-IN", fill="white")
    return img, "Stand-in photo (add profile.jpg to replace)"


@st.cache_data
def skills_csv(df: pd.DataFrame) -> bytes:
    return df.to_csv(index=False).encode("utf-8")


photo, photo_caption = load_photo()
with st.sidebar:
    st.subheader("🎵 My playlist")
    components.html(
        f"""
        <iframe style="border-radius:12px" src="{PLAYLIST_URL}"
                width="100%" height="352" frameborder="0"
                allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
                loading="lazy"></iframe>
        """,
        height=360,
    )
    st.caption("Press play and enjoy the site with some music.")

    st.divider()

    st.subheader("Display options")
    show_milestones = st.checkbox("Show milestone timeline", value=True)
    show_tools = st.checkbox("Show project tools", value=True)

    st.divider()
    st.link_button("GitHub", GITHUB, width="stretch")


st.title(f" {NAME}")
st.subheader(TAGLINE)
st.caption(f"CS 365 · Applied AI · Section {SECTION} · {date.today():%B %d, %Y}")
st.info(f"Welcome! Use the tabs below to explore my story, skills, and projects.")


m1, m2, m3, m4 = st.columns(4)
m1.metric("Projects", len(PROJECTS))
m2.metric("Skills listed", len(SKILLS))
m3.metric("Top skill level", f"{SKILLS['Level'].max()}/10")
m4.metric("Average skill", f"{SKILLS['Level'].mean():.1f}/10",
          delta=f"{SKILLS['Level'].mean() - 5:+.1f} vs. midpoint")

st.divider()

tab_about, tab_story, tab_skills, tab_projects, tab_contact = st.tabs(
    [" About Me", " Autobiography", " Skills", " Projects", " Contact"]
)

with tab_about:
    c1, c2 = st.columns([1, 2], gap="large")
    with c1:
        st.image(photo, caption=photo_caption, width="stretch")
    with c2:
        st.header("About Me")
        st.markdown(
            f"""
**Name:** {NAME}  
**Program:** {PROGRAM}  
**Year:** {YEAR_LEVEL}  
**School:** {SCHOOL}  
**Section:** {SECTION}
"""
        )
        st.write(SHORT_BIO)

        if st.button("👍 Like this portfolio"):
            st.session_state.likes += 1
            st.toast("Thanks for the like!", icon="💙")
        st.write(f"Likes this session: **{st.session_state.likes}**")

with tab_story:
    st.header("My Autobiography")
    left, right = st.columns(2, gap="large")
    sections = list(AUTOBIOGRAPHY.items())
    for i, (title, text) in enumerate(sections):
        with (left if i % 2 == 0 else right):
            with st.container(border=True):
                st.subheader(title)
                st.write(text)

    if show_milestones:
        st.subheader("Milestones")
        miles = pd.DataFrame(MILESTONES)
        st.table(miles.set_index("Year"))

        year_choice = st.select_slider(
            "Slide through my timeline",
            options=miles["Year"].tolist(),
        )
        st.success(miles.loc[miles["Year"] == year_choice, "Milestone"].iloc[0])

    full_text = f"{NAME}\n{PROGRAM}, {YEAR_LEVEL}\n\n{SHORT_BIO}\n\n" + "\n\n".join(
        f"{k.upper()}\n{v}" for k, v in AUTOBIOGRAPHY.items()
    )
    st.download_button(
        "⬇️ Download my autobiography (.txt)",
        data=full_text,
        file_name="autobiography.txt",
        mime="text/plain",
    )

with tab_skills:
    st.header("Skills")
    st.write("TODO: One or two sentences describing how you built these skills.")

    f1, f2 = st.columns([1, 2])
    with f1:
        cats = st.multiselect(
            "Categories",
            options=sorted(SKILLS["Category"].unique()),
            default=sorted(SKILLS["Category"].unique()),
        )
        min_level = st.slider("Minimum level", 1, 10, 1)
        chart_type = st.radio("Chart type", ["Bar", "Line"], horizontal=True)

    filtered = SKILLS[(SKILLS["Category"].isin(cats)) & (SKILLS["Level"] >= min_level)]

    with f2:
        if filtered.empty:
            st.warning("No skills match those filters.")
        else:
            chart_data = filtered.set_index("Skill")["Level"]
            if chart_type == "Bar":
                st.bar_chart(chart_data)
            else:
                st.line_chart(chart_data)

    st.subheader("Skill table")
    st.dataframe(
        filtered,
        width="stretch",
        hide_index=True,
        column_config={
            "Level": st.column_config.ProgressColumn(
                "Level", min_value=0, max_value=10, format="%d/10"
            )
        },
    )
    st.download_button(
        "⬇️ Download skills (.csv)",
        data=skills_csv(filtered),
        file_name="skills.csv",
        mime="text/csv",
    )

with tab_projects:
    st.header("Projects")

    p1, p2 = st.columns(2)
    with p1:
        types = ["All"] + sorted({p["type"] for p in PROJECTS})
        type_filter = st.selectbox("Filter by type", types)
    with p2:
        sort_by = st.selectbox("Sort by", ["Newest first", "Oldest first", "Title A-Z"])

    shown = [p for p in PROJECTS if type_filter in ("All", p["type"])]
    if sort_by == "Newest first":
        shown.sort(key=lambda p: p["year"], reverse=True)
    elif sort_by == "Oldest first":
        shown.sort(key=lambda p: p["year"])
    else:
        shown.sort(key=lambda p: p["title"])

    for p in shown:
        with st.container(border=True):
            a, b = st.columns([3, 1])
            with a:
                st.subheader(p["title"])
                st.markdown(f"**Role:** {p['role']}")
                st.write(p["description"])
                if show_tools:
                    st.markdown("**Tools:** " + " ".join(f"`{t}`" for t in p["tools"]))
            with b:
                st.metric("Year", p["year"])
                st.caption(p["type"])
            with st.expander("Outcome and link"):
                st.write(p["outcome"])
                st.link_button("Open project", p["link"])

    st.subheader("Tools across my projects")
    tool_counts = pd.Series([t for p in PROJECTS for t in p["tools"]]).value_counts()
    st.bar_chart(tool_counts)

with tab_contact:
    st.header("Contact & Feedback")
    cc1, cc2 = st.columns([1, 1], gap="large")

    with cc1:
        st.write("Send me a message or leave feedback on this portfolio.")
        with st.form("feedback_form", clear_on_submit=True):
            f_name = st.text_input("Your name")
            f_email = st.text_input("Your email")
            f_topic = st.selectbox("Topic", ["Feedback", "Collaboration", "Question", "Other"])
            f_rating = st.slider("Rate this portfolio", 1, 5, 4)
            f_msg = st.text_area("Message", height=120)
            f_agree = st.checkbox("I'm okay with being contacted back")
            submitted = st.form_submit_button("Send")

        if submitted:
            if not f_name or not f_msg:
                st.error("Please enter your name and a message.")
            else:
                st.session_state.feedback_log.append(
                    {"Name": f_name, "Topic": f_topic, "Rating": f_rating, "Message": f_msg}
                )
                st.success(f"Thank you, {f_name}! Your message was received.")
                st.balloons()

    with cc2:
        st.subheader("Reach me directly")
        st.markdown(f" {EMAIL}")
        st.markdown(f" [GitHub]({GITHUB})")
        # st.markdown(f"💼 [LinkedIn]({LINKEDIN})")

        st.subheader("Messages this session")
        if st.session_state.feedback_log:
            log = pd.DataFrame(st.session_state.feedback_log)
            st.dataframe(log, width="stretch", hide_index=True)
            st.metric("Average rating", f"{log['Rating'].mean():.1f} / 5")
        else:
            st.caption("No messages yet. Be the first!")

#Footer
st.divider()
st.caption(f"© {date.today().year} {NAME} · {SECTION} · Built with Streamlit")
