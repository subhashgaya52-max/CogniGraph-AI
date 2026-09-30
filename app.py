import streamlit as st
import re
import networkx as nx
import matplotlib.pyplot as plt

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="CogniGraph AI | Panther",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# PROFESSIONAL CSS
# =========================================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(59,130,246,.12), transparent 25%),
        radial-gradient(circle at 90% 10%, rgba(124,58,237,.12), transparent 25%),
        linear-gradient(135deg,#060b16,#0b1220 50%,#0f172a);
    color: #f8fafc;
}

.block-container {
    max-width: 1400px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#080f1d,#0b1324);
    border-right: 1px solid rgba(148,163,184,.12);
}

section[data-testid="stSidebar"] * {
    color: #e2e8f0;
}

/* TOP BRAND */
.brand {
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:10px 0 25px 0;
}

.brand-left {
    display:flex;
    align-items:center;
    gap:12px;
}

.logo {
    width:46px;
    height:46px;
    display:flex;
    align-items:center;
    justify-content:center;
    border-radius:14px;
    background:linear-gradient(135deg,#2563eb,#7c3aed);
    font-size:24px;
    box-shadow:0 8px 25px rgba(37,99,235,.35);
}

.brand-name {
    font-size:21px;
    font-weight:800;
    color:white;
}

.brand-sub {
    font-size:11px;
    color:#94a3b8;
}

/* HERO */
.hero {
    position:relative;
    overflow:hidden;
    padding:38px 42px;
    border-radius:28px;
    background:
        linear-gradient(135deg,
        rgba(37,99,235,.30),
        rgba(124,58,237,.25)),
        rgba(15,23,42,.75);
    border:1px solid rgba(148,163,184,.16);
    box-shadow:0 25px 70px rgba(0,0,0,.28);
    margin-bottom:25px;
}

.hero:after {
    content:"";
    position:absolute;
    width:220px;
    height:220px;
    right:-60px;
    top:-70px;
    border-radius:50%;
    background:rgba(96,165,250,.13);
    filter:blur(5px);
}

.badge {
    display:inline-block;
    padding:7px 13px;
    border-radius:999px;
    background:rgba(59,130,246,.12);
    color:#93c5fd;
    border:1px solid rgba(96,165,250,.25);
    font-size:12px;
    font-weight:600;
    margin-bottom:15px;
}

.hero h1 {
    font-size:46px;
    font-weight:800;
    margin:0;
    letter-spacing:-1.5px;
}

.hero p {
    color:#cbd5e1;
    font-size:16px;
    margin-top:10px;
}

.hero-highlight {
    color:#a78bfa;
    font-weight:700;
}

/* SECTION */
.section-title {
    font-size:24px;
    font-weight:750;
    margin:28px 0 12px 0;
}

.section-subtitle {
    color:#94a3b8;
    font-size:13px;
    margin-bottom:18px;
}

/* METRICS */
.metric-card {
    padding:22px;
    min-height:125px;
    border-radius:20px;
    background:
        linear-gradient(145deg,
        rgba(30,41,59,.85),
        rgba(15,23,42,.88));
    border:1px solid rgba(148,163,184,.13);
    box-shadow:0 12px 35px rgba(0,0,0,.18);
    transition:.25s;
}

.metric-card:hover {
    transform:translateY(-3px);
    border-color:rgba(96,165,250,.35);
}

.metric-icon {
    font-size:22px;
}

.metric-number {
    font-size:31px;
    font-weight:800;
    margin-top:7px;
}

.metric-label {
    color:#94a3b8;
    font-size:12px;
    margin-top:3px;
}

/* CARDS */
.card {
    padding:22px;
    border-radius:20px;
    background:rgba(15,23,42,.72);
    border:1px solid rgba(148,163,184,.13);
    box-shadow:0 12px 35px rgba(0,0,0,.16);
    margin:8px 0;
}

.card h3 {
    margin-top:0;
}

/* CONCEPT */
.node-card {
    padding:12px 15px;
    margin:8px 0;
    border-radius:13px;
    background:rgba(30,41,59,.68);
    border:1px solid rgba(148,163,184,.11);
    transition:.2s;
}

.node-card:hover {
    transform:translateX(4px);
    border-color:rgba(96,165,250,.30);
}

/* STATUS */
.weak-card {
    padding:15px;
    border-radius:14px;
    background:rgba(127,29,29,.16);
    border:1px solid rgba(248,113,113,.20);
    margin:8px 0;
}

.good-card {
    padding:15px;
    border-radius:14px;
    background:rgba(20,83,45,.16);
    border:1px solid rgba(74,222,128,.20);
    margin:8px 0;
}

/* BUTTONS */
div[data-testid="stButton"] > button {
    width:100%;
    border:none;
    border-radius:13px;
    background:linear-gradient(90deg,#2563eb,#7c3aed);
    color:white;
    font-weight:700;
    padding:11px 15px;
    transition:.25s;
}

div[data-testid="stButton"] > button:hover {
    transform:translateY(-2px);
    box-shadow:0 8px 25px rgba(79,70,229,.30);
}

/* FILE UPLOADER */
[data-testid="stFileUploader"] {
    background:rgba(15,23,42,.55);
    border-radius:18px;
}

/* RADIO */
.stRadio label {
    color:#cbd5e1 !important;
}

/* FOOTER */
.footer {
    text-align:center;
    color:#64748b;
    font-size:12px;
    padding:25px;
    margin-top:30px;
}

.footer b {
    color:#94a3b8;
}

/* HIDE DEFAULT FOOTER */
footer {
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNCTIONS
# =========================================================

def extract_concepts(text):

    words = re.findall(
        r"\b[A-Za-z][A-Za-z-]{3,}\b",
        text.lower()
    )

    stop = {
        "this","that","with","from","have","will",
        "into","their","about","which","when",
        "where","what","there","then","than",
        "also","using","student","students",
        "chapter","concept","learning","knowledge"
    }

    freq = {}

    for w in words:
        if w not in stop:
            freq[w] = freq.get(w, 0) + 1

    concepts = [
        w for w, c in
        sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    ][:8]

    if len(concepts) < 5:
        concepts = [
            "python",
            "variables",
            "functions",
            "loops",
            "lists",
            "dsa",
            "algorithms"
        ]

    return concepts


def build_graph(concepts):

    g = nx.DiGraph()

    g.add_nodes_from(concepts)

    for i in range(1, len(concepts)):
        g.add_edge(
            concepts[i-1],
            concepts[i]
        )

    return g


def draw_graph(g, weak):

    pos = nx.spring_layout(
        g,
        seed=7,
        k=1.5
    )

    fig, ax = plt.subplots(
        figsize=(11, 5.5)
    )

    fig.patch.set_alpha(0)
    ax.set_facecolor("#0f172a")

    node_colors = [
        "#ef4444" if n in weak
        else "#22c55e"
        for n in g.nodes
    ]

    nx.draw_networkx(
        g,
        pos,
        ax=ax,
        node_color=node_colors,
        node_size=2200,
        font_size=9,
        font_weight="bold",
        arrows=True,
        edge_color="#64748b",
        font_color="#f8fafc",
        arrowsize=18
    )

    ax.set_axis_off()

    return fig


# =========================================================
# SAMPLE DATA
# =========================================================

samples = {

"Python Basics":
"""
Python variables store data.
Functions organize reusable logic.
Loops repeat operations.
Lists store multiple values.
Data structures organize information.
Algorithms solve computational problems.
Python is widely used in data science.
""",

"DBMS Basics":
"""
A database stores data.
Tables contain rows and columns.
SQL queries data.
Primary keys identify records.
Foreign keys connect tables.
Relationships connect database tables.
Normalization reduces data redundancy.
""",

"AI Basics":
"""
Artificial intelligence uses algorithms
to perform intelligent tasks.
Machine learning learns patterns from data.
Neural networks learn representations.
Deep learning uses multiple layers.
Generative AI can create text and images.
Large language models understand language.
"""
}


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("""
    <div class="brand">
        <div class="brand-left">
            <div class="logo">🧠</div>
            <div>
                <div class="brand-name">CogniGraph AI</div>
                <div class="brand-sub">SMART EDUCATION PLATFORM</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🐾 PANTHER")

    st.caption("AI-powered personalized learning")

    st.markdown("---")

    st.markdown("### 📍 Navigation")

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "📄 Documents",
            "🧠 Knowledge Graph",
            "📝 AI Quiz",
            "📊 Analytics",
            "🎯 Learning Path",
            "🤖 AI Tutor"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown("### ⚙️ Demo Settings")

    sample = st.selectbox(
        "📚 Select Topic",
        [
            "Python Basics",
            "DBMS Basics",
            "AI Basics"
        ]
    )

    st.markdown("---")

    st.markdown("### 🔄 AI Pipeline")

    st.markdown("📄 **01** Document Ingestion")
    st.markdown("🔗 **02** Knowledge Graph")
    st.markdown("📝 **03** Adaptive Quiz")
    st.markdown("🔴 **04** Gap Detection")
    st.markdown("🛠️ **05** Remediation")


# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">

<div class="badge">
TECHNORAZZ 2026 • TRACK 2 • SMART EDUCATION
</div>

<h1>
🧠 CogniGraph AI
</h1>

<p>
Transform learning material into an
<span class="hero-highlight">
personalized AI learning journey.
</span>
</p>

<p style="font-size:13px;color:#94a3b8">
Document → Knowledge Graph → Diagnostic Quiz →
Learning Gap → Personalized Recovery
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# DOCUMENT INPUT
# =========================================================

st.markdown(
    '<div class="section-title">📄 Learning Material</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Upload your study material and let CogniGraph AI analyze the concepts.</div>',
    unsafe_allow_html=True
)

uploaded = st.file_uploader(
    "Upload learning material",
    type=["txt"],
    label_visibility="collapsed"
)

source = (
    uploaded.read().decode(
        "utf-8",
        errors="ignore"
    )
    if uploaded
    else samples[sample]
)

if not uploaded:

    st.info(
        "💡 Demo dataset loaded. Upload your own .txt learning material to test the system."
    )


with st.expander("👁️ Preview Learning Material"):

    st.write(source)


# =========================================================
# BUILD GRAPH
# =========================================================

if st.button("🚀 Analyze Material & Build AI Knowledge Graph"):

    st.session_state["concepts"] = extract_concepts(
        source
    )

    st.session_state["graph"] = build_graph(
        st.session_state["concepts"]
    )

    st.session_state["built"] = True

    st.session_state.pop(
        "score",
        None
    )

    st.session_state.pop(
        "weak",
        None
    )

    st.success(
        "✅ AI analysis completed successfully!"
    )


# =========================================================
# DASHBOARD METRICS
# =========================================================

if st.session_state.get("built"):

    concepts = st.session_state["concepts"]

    graph = st.session_state["graph"]

    weak = st.session_state.get(
        "weak",
        []
    )

    score = st.session_state.get(
        "score",
        0
    )

    st.markdown(
        '<div class="section-title">📊 Learning Overview</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            f"""
            <div class="metric-card">
            <div class="metric-icon">📚</div>
            <div class="metric-number">01</div>
            <div class="metric-label">DOCUMENT ANALYZED</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="metric-card">
            <div class="metric-icon">🧠</div>
            <div class="metric-number">{len(concepts)}</div>
            <div class="metric-label">CONCEPT NODES</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            f"""
            <div class="metric-card">
            <div class="metric-icon">🎯</div>
            <div class="metric-number">{score}/5</div>
            <div class="metric-label">QUIZ SCORE</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:
        st.markdown(
            f"""
            <div class="metric-card">
            <div class="metric-icon">🔴</div>
            <div class="metric-number">{len(weak)}</div>
            <div class="metric-label">LEARNING GAPS</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# KNOWLEDGE GRAPH
# =========================================================

if st.session_state.get("built"):

    st.markdown(
        '<div class="section-title">🧠 Knowledge Graph</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Visual representation of detected learning concepts and prerequisites.</div>',
        unsafe_allow_html=True
    )

    left, right = st.columns(
        [2.2, 1]
    )

    with left:

        st.pyplot(
            draw_graph(
                graph,
                weak
            ),
            clear_figure=True
        )

    with right:

        st.markdown(
            """
            <div class="card">
            <h3>🔗 Concept Nodes</h3>
            """,
            unsafe_allow_html=True
        )

        for i, concept in enumerate(
            concepts,
            1
        ):

            icon = (
                "🔴"
                if concept in weak
                else "🟢"
            )

            st.markdown(
                f"""
                <div class="node-card">
                {icon} <b>{i}. {concept.title()}</b>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


# =========================================================
# QUIZ
# =========================================================

if st.session_state.get("built"):

    st.markdown(
        '<div class="section-title">📝 Adaptive AI Quiz</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Test your understanding and let AI identify learning gaps.</div>',
        unsafe_allow_html=True
    )

    questions = [

        (
            "What is the main purpose of a variable?",
            [
                "Store a value",
                "Delete a program",
                "Create hardware"
            ]
        ),

        (
            "What does a function provide?",
            [
                "Reusable logic",
                "Only graphics",
                "Internet access"
            ]
        ),

        (
            "What is a loop used for?",
            [
                "Repeating operations",
                "Deleting data",
                "Installing Python"
            ]
        ),

        (
            "What can a list contain?",
            [
                "Multiple values",
                "Only one value",
                "Only images"
            ]
        ),

        (
            "What does DSA commonly mean?",
            [
                "Data Structures and Algorithms",
                "Data Storage App",
                "Digital System Access"
            ]
        )
    ]

    answers = []

    for i, (question, options) in enumerate(
        questions
    ):

        st.markdown(
            f"""
            <div class="card">
            <b>Q{i+1}. {question}</b>
            </div>
            """,
            unsafe_allow_html=True
        )

        answers.append(
            st.radio(
                "Choose your answer:",
                options,
                key=f"q{i}",
                horizontal=True
            )
        )

    if st.button(
        "🔍 Diagnose My Learning Gaps"
    ):

        score = sum(
            answers[i]
            == questions[i][1][0]
            for i in range(5)
        )

        st.session_state["score"] = score

        st.session_state["weak"] = (
            concepts[
                :max(
                    1,
                    5 - score
                )
            ]
        )

        st.success(
            f"🎯 Diagnostic complete — {score}/5 answers correct."
        )


# =========================================================
# GAP ANALYSIS
# =========================================================

if "score" in st.session_state:

    score = st.session_state["score"]

    weak = st.session_state["weak"]

    st.markdown(
        '<div class="section-title">🔴 Learning Gap Analysis</div>',
        unsafe_allow_html=True
    )

    a, b, c = st.columns(3)

    with a:

        st.markdown(
            f"""
            <div class="metric-card">
            <div class="metric-icon">🎯</div>
            <div class="metric-number">{score}/5</div>
            <div class="metric-label">QUIZ SCORE</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with b:

        st.markdown(
            f"""
            <div class="metric-card">
            <div class="metric-icon">🔴</div>
            <div class="metric-number">{len(weak)}</div>
            <div class="metric-label">GAP NODES</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c:

        status = (
            "STRONG"
            if not weak
            else "REVIEW"
        )

        st.markdown(
            f"""
            <div class="metric-card">
            <div class="metric-icon">📈</div>
            <div class="metric-number">{status}</div>
            <div class="metric-label">LEARNING STATUS</div>
            </div>
            """,
            unsafe_allow_html=True
        )


    # GAP LIST

    st.markdown(
        "### ⚠️ Topics Needing Attention"
    )

    for node in weak:

        st.markdown(
            f"""
            <div class="weak-card">
            🔴 <b>{node.title()}</b>
            <br>
            <span style="color:#94a3b8;font-size:13px;">
            This concept requires additional practice.
            </span>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# REMEDIATION
# =========================================================

if "score" in st.session_state:

    st.markdown(
        '<div class="section-title">🎯 Personalized Recovery Path</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">CogniGraph AI recommends a focused recovery path based on your quiz performance.</div>',
        unsafe_allow_html=True
    )

    for index, node in enumerate(
        weak,
        1
    ):

        st.markdown(
            f"""
            <div class="card">

            <h3>
            🔧 Step {index}: Recover {node.title()}
            </h3>

            <p>① 📖 Review the concept definition</p>

            <p>② 💻 Solve 2–3 focused practice questions</p>

            <p>③ 📝 Take a mini re-test</p>

            <p>④ ✅ Move forward after improvement</p>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# AI TUTOR PREVIEW
# =========================================================

if st.session_state.get("built"):

    st.markdown(
        '<div class="section-title">🤖 AI Tutor</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(
        [2, 1]
    )

    with col1:

        st.markdown(
            """
            <div class="card">

            <h3>👋 Ask CogniGraph AI</h3>

            <p style="color:#94a3b8;">
            Get simple explanations for difficult concepts.
            </p>

            <div style="
            padding:16px;
            border-radius:14px;
            background:rgba(30,41,59,.65);
            margin-top:12px;">

            <b>Example Question</b>

            <br><br>

            "Explain inheritance in simple English."

            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="card">

            <h3>✨ AI Capabilities</h3>

            <p>✓ Simple explanations</p>
            <p>✓ Hinglish support</p>
            <p>✓ Examples</p>
            <p>✓ Practice questions</p>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

    🧠 <b>CogniGraph AI</b> &nbsp;•&nbsp;
    🐾 <b>Team Panther</b> &nbsp;•&nbsp;
    Technorazz 2026

    <br><br>

    AI-powered personalized learning platform

    </div>
    """,
    unsafe_allow_html=True
)