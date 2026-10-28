import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Poppins:wght@400;600;700&display=swap');

:root{
  --yellow:#FFD500; --yellow-dark:#F2B705; --black:#111111;
  --red:#E63946; --orange:#F28C28; --green:#3BB273; --blue:#2E86DE; --pink:#FF6FA5;
}

[data-testid="stAppViewContainer"]{
  background-color: var(--yellow);
  background-image:
    linear-gradient(to bottom,
      var(--red) 0 6px, var(--orange) 6px 12px, var(--green) 12px 18px, var(--blue) 18px 24px, var(--black) 24px 28px,
      transparent 28px),
    radial-gradient(rgba(0,0,0,.10) 1.6px, transparent 1.7px);
  background-size: 100% 28px, 18px 18px;
  background-repeat: no-repeat, repeat;
  font-family: 'Poppins', sans-serif;
}
[data-testid="stHeader"]{ background: transparent; }

/* ---------- Headings ---------- */
h1, h2, h3{
  font-family: 'Anton', Impact, sans-serif !important;
  letter-spacing: .04em; text-transform: uppercase; color: var(--black);
}
/* Big title = black TV label with yellow text and a hard shadow */
h1{
  display: inline-block; background: var(--black); color: #FFFFFF !important;
  padding: .15em .6em !important; border-radius: 14px;
  transform: rotate(-1.5deg); box-shadow: 8px 8px 0 var(--red);
  margin-top: .5rem;
}
h2{ border-bottom: 5px solid var(--black); display: inline-block; padding-bottom: 2px; }

/* ---------- Sidebar: black "TV set" ---------- */
[data-testid="stSidebar"]{
  background: var(--black);
  border-right: 6px solid var(--red);
}
[data-testid="stSidebar"] *{ color: var(--yellow) !important; }
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3{
  background: none; box-shadow: none; transform: none; border: none; color: var(--yellow) !important;
}

/* ---------- Bordered containers (projects, autobiography cards) = TV frames ---------- */
[data-testid="stVerticalBlockBorderWrapper"]:has(> div > [data-testid="stVerticalBlock"]){
  border-radius: 22px;
}
div[data-testid="stVerticalBlockBorderWrapper"]{
  border: 4px solid var(--black) !important;
  border-radius: 22px !important;
  background: #FFF3B0;
  box-shadow: 7px 7px 0 var(--black);
}
/* the antenna */
div[data-testid="stVerticalBlockBorderWrapper"]{ position: relative; }

/* ---------- Metrics ---------- */
[data-testid="stMetric"]{
  background: var(--black); color: var(--yellow);
  border-radius: 18px; padding: 14px 18px;
  border: 3px solid var(--black); box-shadow: 5px 5px 0 var(--orange);
}
[data-testid="stMetric"] *{ color: var(--yellow) !important; }
[data-testid="stMetricValue"]{ font-family: 'Anton', sans-serif; letter-spacing: .05em; }

/* ---------- Tabs: black pills, white text (About Me ... Contact) ---------- */
[data-testid="stTabs"] [role="tablist"]{ gap: 10px; border-bottom: 4px solid var(--black); }
[data-testid="stTabs"] button[role="tab"],
[data-testid="stTab"]{
  background: var(--black) !important; border: 3px solid var(--black) !important; border-bottom: none !important;
  border-radius: 14px 14px 0 0 !important; padding: 8px 18px !important;
}
[data-testid="stTabs"] button[role="tab"],
[data-testid="stTabs"] button[role="tab"] *,
[data-testid="stTab"],
[data-testid="stTab"] *,
[data-testid="stTab"] p{
  color: #FFFFFF !important; fill: #FFFFFF !important;
  font-family: 'Anton', sans-serif !important; font-size: 1.05rem !important;
  letter-spacing: .06em; text-transform: uppercase;
}
[data-testid="stTabs"] button[role="tab"][aria-selected="true"],
[data-testid="stTab"][aria-selected="true"]{ background: var(--red) !important; }
[data-testid="stTabs"] button[role="tab"]:hover{ background: #333333 !important; }
[data-testid="stTabs"] button[role="tab"][aria-selected="true"]:hover{ background: var(--red) !important; }
[data-baseweb="tab-highlight"]{ background: var(--black) !important; height: 5px !important; }

/* ---------- Buttons ---------- */
.stButton > button, .stDownloadButton > button, .stFormSubmitButton > button, .stLinkButton > a{
  background: var(--black) !important; color: var(--yellow) !important;
  border: 3px solid var(--black) !important; border-radius: 999px !important;
  font-family: 'Anton', sans-serif; letter-spacing: .08em; text-transform: uppercase;
  box-shadow: 4px 4px 0 var(--red); transition: transform .08s;
}
.stButton > button:hover, .stDownloadButton > button:hover,
.stFormSubmitButton > button:hover, .stLinkButton > a:hover{
  transform: translate(-2px,-2px); box-shadow: 6px 6px 0 var(--red); color: #fff !important;
}
[data-testid="stSidebar"] .stLinkButton > a{ background: var(--yellow) !important; border-color: var(--yellow) !important; }
[data-testid="stSidebar"] .stLinkButton > a, [data-testid="stSidebar"] .stLinkButton > a *{ color: var(--black) !important; }

/* ---------- Inputs & forms ---------- */
[data-testid="stForm"]{
  border: 4px solid var(--black); border-radius: 22px; background: #FFF3B0; box-shadow: 7px 7px 0 var(--black);
}
[data-baseweb="input"], [data-baseweb="textarea"], [data-baseweb="select"] > div{
  border-radius: 12px !important; border: 2px solid var(--black) !important;
}

/* ---------- Alerts (info / success / warning) ---------- */
[data-testid="stAlert"]{
  background: var(--black); border: 3px solid var(--black); border-radius: 16px; box-shadow: 5px 5px 0 var(--blue);
}
[data-testid="stAlert"] *{ color: var(--yellow) !important; }

/* ---------- Dividers = caution tape ---------- */
hr{
  border: none !important; height: 14px; opacity: 1 !important;
  background: repeating-linear-gradient(-45deg, var(--black) 0 14px, var(--yellow) 14px 28px);
  border-radius: 4px; margin: 1.5rem 0 !important;
}

/* ---------- Tables, expanders, captions ---------- */
[data-testid="stExpander"]{ border: 3px solid var(--black); border-radius: 16px; background: #FFF3B0; }
[data-testid="stDataFrame"], [data-testid="stTable"]{ border: 3px solid var(--black); border-radius: 12px; overflow: hidden; }
[data-testid="stImage"] img{ border: 4px solid var(--black); border-radius: 18px; box-shadow: 6px 6px 0 var(--black); }
[data-testid="stSidebar"] [data-testid="stImage"] img{ border-color: var(--yellow); box-shadow: none; }
</style>
"""


def apply_theme():
    st.markdown(CSS, unsafe_allow_html=True)