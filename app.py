import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="Miika Koivisto | E-Portfolio",
    page_icon="💻",
    layout="wide"
)

# Load the portfolio background image from assets and convert it to a browser-safe data URI.
background_path = Path("assets/portfolio_network_bg.png")
background_data_uri = ""

if background_path.exists():
    encoded_background = base64.b64encode(background_path.read_bytes()).decode("utf-8")
    background_data_uri = f"data:image/png;base64,{encoded_background}"

# -------------------------
# THEME
# -------------------------

# Permanent dark mode
bg = "#0e1117"
card_bg = "#161b22"
text = "#f0f2f6"
muted = "#a7b0be"
border = "#30363d"
nav_bg = "#161b22"

# -------------------------
# CUSTOM CSS
# -------------------------



st.markdown(f"""
<style>



/* -------------------------
   PAGE
------------------------- */

.stApp {{
    background: {bg} !important;
    color: {text} !important;
}}

[data-testid="stAppViewContainer"] {{
    background: transparent !important;
    position: relative;
    min-height: 100vh;
    overflow-x: hidden;
}}

.network-image-bg {{
    position: fixed;
    inset: -6%;
    z-index: 0;
    pointer-events: none;
    background-color: {bg};
    background-image:
        linear-gradient(rgba(2, 7, 20, 0.34), rgba(2, 7, 20, 0.46)),
        url("{background_data_uri}");
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    transform: scale(1.07);
    animation: networkBackgroundFloat 22s ease-in-out infinite alternate;
    will-change: transform, background-position, filter;
}}

.network-image-bg::after {{
    content: "";
    position: absolute;
    inset: 0;
    background:
        radial-gradient(circle at 72% 35%, rgba(65, 125, 255, 0.08), transparent 28%),
        radial-gradient(circle at 84% 72%, rgba(90, 75, 230, 0.07), transparent 30%);
    animation: networkGlowPulse 10s ease-in-out infinite alternate;
}}

@keyframes networkBackgroundFloat {{
    0% {{
        transform: scale(1.07) translate3d(-1.5%, -0.8%, 0);
        background-position: 48% 50%;
        filter: brightness(0.92);
    }}
    50% {{
        transform: scale(1.10) translate3d(1.2%, 0.7%, 0);
        background-position: 52% 48%;
        filter: brightness(1.00);
    }}
    100% {{
        transform: scale(1.08) translate3d(-0.5%, 1.1%, 0);
        background-position: 50% 53%;
        filter: brightness(0.96);
    }}
}}

@keyframes networkGlowPulse {{
    0% {{
        opacity: 0.45;
        transform: scale(1);
    }}
    100% {{
        opacity: 0.85;
        transform: scale(1.05);
    }}
}}

.block-container {{
    position: relative;
    z-index: 2;
    max-width: 1180px;
    margin: 2.2rem auto 3rem auto;
    padding: 2.2rem 2.4rem 3rem 2.4rem !important;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 22px;
    background: rgba(14, 17, 23, 0.88);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    box-shadow:
        0 24px 70px rgba(0,0,0,0.42),
        0 1px 0 rgba(255,255,255,0.04) inset;
}}

@media (max-width: 900px) {{
    .block-container {{
        margin: 1rem;
        padding: 1.4rem 1.1rem 2rem 1.1rem !important;
        border-radius: 16px;
    }}
}}

@media (prefers-reduced-motion: reduce) {{
    .network-image-bg,
    .network-image-bg::after {{
        animation: none;
    }}
}}

/* -------------------------
   NORMAL TEXT
------------------------- */

p,
li {{
    color: {text};
}}

.hero-title {{
    font-size: 3.5rem;
    font-weight: 700;
    margin-bottom: 0;
    color: {text} !important;
}}

.hero-subtitle {{
    font-size: 1.5rem;
    color: {muted} !important;
    margin-top: 0.3rem;
}}

.hero-text {{
    font-size: 1.05rem;
    line-height: 1.7;
    max-width: 750px;
    color: {text} !important;
}}

.section-title {{
    font-size: 2rem;
    font-weight: 700;
    margin-top: 2rem;
    margin-bottom: 1rem;
    color: {text} !important;
}}




/* -------------------------
   INTRO / ABOUT CARD
------------------------- */

.intro-card {{
    margin-top: 0.4rem;
    padding: 2rem 2.1rem;
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 18px;
    background: linear-gradient(135deg, rgba(22,27,34,0.96), rgba(17,23,34,0.90));
    box-shadow: 0 16px 42px rgba(0,0,0,0.24);
}}

.intro-name {{
    font-size: 3.15rem;
    line-height: 1.05;
    font-weight: 700;
    margin: 0;
    color: #f0f2f6 !important;
}}

.intro-role {{
    margin-top: 0.55rem;
    font-size: 1.25rem;
    font-weight: 500;
    color: #a7b0be !important;
}}

.intro-divider {{
    height: 1px;
    margin: 1.45rem 0 1.3rem 0;
    background: linear-gradient(90deg, rgba(85,145,255,0.65), rgba(255,255,255,0.08), transparent);
}}

.intro-about-title {{
    margin: 0 0 0.7rem 0;
    font-size: 1.35rem;
    font-weight: 700;
    color: #f0f2f6 !important;
}}

.intro-about {{
    margin: 0 0 0.9rem 0;
    font-size: 1rem;
    line-height: 1.72;
    color: #d7dce5 !important;
}}

.intro-about:last-child {{
    margin-bottom: 0;
}}

@media (max-width: 700px) {{
    .intro-card {{
        padding: 1.4rem;
    }}

    .intro-name {{
        font-size: 2.35rem;
    }}
}}

/* -------------------------
   CONTACT CTA
------------------------- */

.contact-cta {{
    margin-top: 1.2rem;
    padding: 2rem;
    border-radius: 12px;
    border: 1px solid {border} !important;
    background: {card_bg} !important;
    box-shadow: none;
}}

.contact-cta h2 {{
    margin: 0 0 0.45rem 0;
    font-size: 2rem;
    color: {text} !important;
}}

.contact-cta p {{
    margin: 0;
    color: {muted} !important;
    font-size: 1.02rem;
    line-height: 1.6;
}}

.contact-meta {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.7rem 1.2rem;
    margin-top: 1.1rem;
    color: {text};
    font-size: 0.95rem;
}}

.contact-copy-row {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    width: 100%;
    padding: 0.75rem 0.9rem;
    border: 1px solid {border};
    border-radius: 9px;
    background: {bg};
}}

.contact-copy-value {{
    color: {text} !important;
    user-select: text;
    -webkit-user-select: text;
}}

.contact-copy-btn {{
    flex-shrink: 0;
    padding: 0.38rem 0.65rem;
    border: 1px solid {border};
    border-radius: 7px;
    background: {card_bg};
    color: {text};
    cursor: pointer;
    font: inherit;
    font-size: 0.82rem;
}}

.contact-copy-btn:hover {{
    border-color: rgba(120, 180, 255, 0.7);
}}

.contact-copy-btn:active {{
    transform: translateY(1px);
}}



/* -------------------------
   SKILL + CERTIFICATION CARDS
------------------------- */

.skill-card {{
    padding: 1.25rem;
    border: 1px solid {border} !important;
    border-radius: 12px;
    min-height: 300px;
    height: 100%;
    box-sizing: border-box;
    background: {card_bg} !important;
    color: {text} !important;
    display: flex;
    flex-direction: column;
}}

.skill-chip-container {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    align-content: flex-start;
}}

.skill-chip {{
    display: inline-flex;
    align-items: center;
    max-width: 100%;
    padding: 0.32rem 0.56rem;
    border-radius: 8px;
    border: 1px solid {border};
    background: {bg};
    color: {text} !important;
    font-size: 0.80rem;
    line-height: 1.2;
    white-space: normal;
    overflow-wrap: anywhere;
    word-break: break-word;
}}

.skill-card * {{
    color: {text} !important;
}}

.skill-card h3 {{
    color: {text} !important;
    margin-top: 0;
}}

.skill-card p {{
    color: {text} !important;
}}


/* Keep the four skill cards visually equal in height */
[data-testid="stHorizontalBlock"]:has(.skill-card) {{
    align-items: stretch;
}}

[data-testid="column"]:has(.skill-card) {{
    display: flex;
}}

[data-testid="column"]:has(.skill-card) > div {{
    width: 100%;
}}




/* Keep every Skills card aligned */
.skill-card {{
    height: 100%;
    min-height: 270px;
    display: flex;
    flex-direction: column;
}}

.skill-card h3 {{
    min-height: 3.2rem;
    margin-top: 0;
    margin-bottom: 1rem;
    display: flex;
    align-items: flex-start;
}}

.skill-card .skill-chips,
.skill-card .chips,
.skill-card .tags {{
    align-content: flex-start;
}}

/* -------------------------
   SHARED CONTENT CARDS
------------------------- */

.content-card {{
    padding: 1.6rem 1.8rem;
    border: 1px solid {border} !important;
    border-radius: 12px;
    background: {card_bg} !important;
    color: {text} !important;
    margin-bottom: 1rem;
}}

.content-card * {{
    color: {text} !important;
}}

.content-card h3 {{
    margin-top: 0;
    margin-bottom: 0.65rem;
}}

.content-card p {{
    line-height: 1.65;
}}

.content-card ul {{
    margin-bottom: 0.9rem;
}}

.content-card a {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    margin-top: 0.6rem;
    padding: 0.62rem 0.9rem;
    border-radius: 8px;
    border: 1px solid {border};
    background: {bg};
    color: {text} !important;
    text-decoration: none !important;
    font-weight: 600;
    transition: transform 0.18s ease, border-color 0.18s ease;
}}

.content-card a:hover {{
    transform: translateY(-2px);
    border-color: rgba(120, 180, 255, 0.75);
}}

/* -------------------------
   PROJECT CARD
------------------------- */

.project-card {{
    padding: 1.5rem;
    border: 1px solid {border} !important;
    border-radius: 12px;
    background: {card_bg} !important;
    color: {text} !important;
}}

.project-card * {{
    color: {text} !important;
}}


/* -------------------------
   EXPERIENCE
------------------------- */

.experience-card {{
    padding: 1.6rem 1.8rem;
    border: 1px solid {border} !important;
    border-radius: 12px;
    background: {card_bg} !important;
    color: {text} !important;
    margin-bottom: 1rem;
}}

.experience-card * {{
    color: {text} !important;
}}

.experience-company {{
    font-size: 1.35rem;
    font-weight: 700;
    margin-bottom: 0.2rem;
    color: {text} !important;
}}

.experience-role {{
    font-size: 1.05rem;
    font-weight: 600;
    color: {muted} !important;
    margin-bottom: 1rem;
}}

.experience-category {{
    font-weight: 700;
    margin-top: 0.8rem;
    color: {text} !important;
}}



/* -------------------------
   METRICS
------------------------- */

[data-testid="stMetric"] {{
    border: 1px solid {border} !important;
    padding: 1rem;
    border-radius: 12px;
    background: {card_bg} !important;
}}

[data-testid="stMetric"] * {{
    color: {text} !important;
}}


/* -------------------------
   EXPANDER
------------------------- */

[data-testid="stExpander"] {{
    background: {card_bg} !important;
    border-color: {border} !important;
}}

[data-testid="stExpander"] * {{
    color: {text} !important;
}}


/* -------------------------
   BUTTONS
------------------------- */

.stLinkButton a,
.stDownloadButton button {{
    border-radius: 8px;
    font-weight: 600;
}}


/* -------------------------
   HIDE STREAMLIT UI
------------------------- */

#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

header {{
    visibility: hidden;
}}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="network-image-bg" aria-hidden="true"></div>
""", unsafe_allow_html=True)






# -------------------------
# INTRO / ABOUT
# -------------------------

st.markdown('<div id="home" class="anchor"></div>', unsafe_allow_html=True)

left, right = st.columns([1.8, 1], gap="large")

with left:
    st.markdown("""
<div class="intro-card">
<div class="intro-name">Miika Koivisto</div>
<div class="intro-role">IT Development • Automation • AI</div>
<div class="intro-divider"></div>
<div class="intro-about-title">About Me</div>
<p class="intro-about">I’m an IT professional with a background in developing and improving digital solutions, automation and business systems. My experience has given me the opportunity to work across different areas of IT, from system development and integrations to process automation and solving practical business needs with technology.</p>
<p class="intro-about">I enjoy understanding how things work, identifying opportunities for improvement and turning ideas into practical solutions. I’m systematic and solution-oriented in my work, but I also value collaboration, continuous learning and sharing knowledge with others.</p>
<p class="intro-about">I’m especially interested in how AI can be applied to real-world problems and existing business processes. As the next step in my career, I’m looking to move toward AI engineering, building on my existing IT experience while developing deeper expertise in AI-driven applications and intelligent automation.</p>
</div>
""", unsafe_allow_html=True)

with right:
    st.image("asset/profile.jpeg", width=280)

st.write("")

button1, button2, button3, button4 = st.columns(4)

with button1:
    st.link_button("GitHub", "https://github.com/MiikaKoivisto", use_container_width=True)

with button2:
    st.link_button("LinkedIn", "https://www.linkedin.com/in/miikakoivisto98", use_container_width=True)

with button3:
    english_cv = Path("assets/Koivisto_Miika_Resume.pdf")
    if english_cv.exists():
        with english_cv.open("rb") as pdf_file:
            st.download_button(
                label="CV — English",
                data=pdf_file,
                file_name=english_cv.name,
                mime="application/pdf",
                use_container_width=True
            )
    else:
        st.button("CV — English", disabled=True, use_container_width=True)

with button4:
    finnish_cv = Path("assets/Koivisto_Miika_Resume_FI.pdf")
    if finnish_cv.exists():
        with finnish_cv.open("rb") as pdf_file:
            st.download_button(
                label="CV — Suomi",
                data=pdf_file,
                file_name=finnish_cv.name,
                mime="application/pdf",
                use_container_width=True
            )
    else:
        st.button("CV — Suomi", disabled=True, use_container_width=True)

st.divider()

# -------------------------
# SKILLS
# -------------------------

st.markdown(
    '<div id="skills" class="anchor"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">Skills</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="skill-card">
        <h3>AI & Cloud</h3>
        <div class="skill-chip-container">
            <span class="skill-chip">Azure OpenAI</span>
            <span class="skill-chip">Azure AI Search</span>
            <span class="skill-chip">Microsoft Foundry</span>
            <span class="skill-chip">RAG</span>
            <span class="skill-chip">Vector Embeddings</span>
            <span class="skill-chip">Hybrid Search</span>
            <span class="skill-chip">Microsoft Azure</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="skill-card">
        <h3>Programming</h3>
        <div class="skill-chip-container">
            <span class="skill-chip">Python</span>
            <span class="skill-chip">JavaScript</span>
            <span class="skill-chip">HTML</span>
            <span class="skill-chip">CSS</span>
            <span class="skill-chip">JSON</span>
            <span class="skill-chip">XML</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="skill-card">
        <h3>Automation & APIs</h3>
        <div class="skill-chip-container">
            <span class="skill-chip">REST API</span>
            <span class="skill-chip">Postman</span>
            <span class="skill-chip">Power Automate</span>
            <span class="skill-chip">Power Apps</span>
            <span class="skill-chip">UiPath</span>
            <span class="skill-chip">RPA</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="skill-card">
        <h3>Systems & Low-code platforms</h3>
        <div class="skill-chip-container">
            <span class="skill-chip">PIM</span>
            <span class="skill-chip">ERP Systems</span>
            <span class="skill-chip">WMS</span>
            <span class="skill-chip">Cloudinary</span>
            <span class="skill-chip">SharePoint</span>
            <span class="skill-chip">Docker</span>
            <span class="skill-chip">AWS</span>
            <span class="skill-chip">Streamlit</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# PROJECTS
# -------------------------

st.markdown(
    '<div id="projects" class="anchor"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">Featured Project</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="content-card">
<h3>Microsoft 365 RAG Assistant</h3>
<p>An end-to-end Retrieval-Augmented Generation application for answering Microsoft 365 support questions using a custom knowledge base.</p>

<p><strong>What I built</strong></p>
<ul>
<li>Document ingestion and chunking pipeline</li>
<li>Vector embeddings with Azure OpenAI</li>
<li>Hybrid keyword + vector retrieval</li>
<li>Azure AI Search indexing</li>
<li>Relevance filtering</li>
<li>Grounded LLM answer generation</li>
<li>Retrieval evaluation</li>
<li>Streamlit user interface</li>
</ul>

<a href="https://github.com/MiikaKoivisto/Azure-AI-RAG-Project"
   target="_blank"
   rel="noopener noreferrer">
   View Project on GitHub
</a>
<br>
<a href="https://azure-ai-rag-project-dfmv5waazkbkrkca3dw54f.streamlit.app/"
   target="_blank"
   rel="noopener noreferrer">
   Try assistant
</a>
</div>

""", unsafe_allow_html=True)

st.write("")

# HOW IT WORKS

st.markdown(
    '<div class="section-title">How the RAG Assistant Works</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("### 1. Question")
    st.write("User submits a Microsoft 365 support question.")

with col2:
    st.markdown("### 2. Embedding")
    st.write("The question is converted into a vector embedding.")

with col3:
    st.markdown("### 3. Retrieval")
    st.write("Azure AI Search performs hybrid retrieval.")

with col4:
    st.markdown("### 4. Context")
    st.write("Relevant document chunks are added to the prompt.")

with col5:
    st.markdown("### 5. Answer")
    st.write("Azure OpenAI generates a grounded response.")



st.write("")

metric1, metric2, metric3 = st.columns(3)

with metric1:
    st.metric(
        "Top-1 Accuracy",
        "91.7%"
    )

with metric2:
    st.metric(
        "Top-2 Accuracy",
        "100%"
    )

with metric3:
    st.metric(
        "Evaluation Queries",
        "12"
    )

st.write("")

with st.expander("See Streamlit UI"):
    st.image(
        "assets/StreamlitUI.png",
        caption="Microsoft 365 RAG Assistant"
    )

with st.expander("See RAG Debug View"):
    st.image(
        "assets/StreamlitUI1.png",
        caption="Retrieved chunks and RAG debug information"
    )

# -------------------------
# EXPERIENCE
# -------------------------

st.markdown(
    '<div id="experience" class="anchor"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">Experience</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="experience-card">

<div class="experience-company">
LVI-Dahl Suomi Oy
</div>

<div class="experience-role">
IT-Asiantuntija / IT Development · 04/2024 – 09/2026
</div>

<div class="experience-category">
Development & APIs
</div>

<ul>
<li>Developed and modernized internal store and picking applications</li>
<li>Built, tested and troubleshot REST API integrations</li>
<li>Tested and documented integrations between business systems</li>
</ul>

<div class="experience-category">
Automation
</div>

<ul>
<li>Automated weekly and monthly e-commerce content publishing</li>
<li>Automated internal forms, approval processes and information flows with Power Automate</li>
</ul>

<div class="experience-category">
Systems & Data
</div>

<ul>
<li>Worked with e-commerce, PIM and ERP environments</li>
<li>Maintained product information and certificate data quality</li>
</ul>

</div>
""", unsafe_allow_html=True)

# -------------------------
# EDUCATION
# -------------------------

st.markdown(
    '<div id="education" class="anchor"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">Education</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="content-card">
<h3>Bachelor of Business Administration</h3>
<p><strong>Business Information Technology</strong></p>
<p>HAMK University of Applied Sciences | 08/2021 – 06/2025</p>
</div>
""", unsafe_allow_html=True)

# -------------------------
# CERTIFICATIONS
# -------------------------
st.markdown(
    '<div id="certifications" class="anchor"></div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="section-title">Certifications</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="skill-card">
        <h3>Microsoft Azure AI</h3>
        <p>
        Azure AI development and Microsoft Foundry training.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="skill-card">
        <h3>Cloud & AI</h3>
        <p>
        Microsoft cloud and artificial intelligence technologies.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="skill-card">
        <h3>View Credentials</h3>
        <p>
        View my completed certifications and credentials.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "View Certifications",
        "https://learn.microsoft.com/en-us/users/miikakoivisto-5797/achievements?tab=applied-skills-tab"
    )


# -------------------------
# CONTACT
# -------------------------

st.markdown(
    '<div id="contact" class="anchor"></div>',
    unsafe_allow_html=True
)

st.markdown("""<div class="contact-cta">
<h2>Contact Me</h2>
<div class="contact-meta" style="flex-direction: column;">
<div class="contact-copy-row">
<span class="contact-copy-value">📧 Miikak123@gmail.com</span>
<button class="contact-copy-btn" onclick="navigator.clipboard.writeText('Miikak123@gmail.com'); this.innerText='Copied!'; setTimeout(() => this.innerText='Copy', 1200);">Copy</button>
</div>
<div class="contact-copy-row">
<span class="contact-copy-value">📞 +358 505731282</span>
<button class="contact-copy-btn" onclick="navigator.clipboard.writeText('+358505731282'); this.innerText='Copied!'; setTimeout(() => this.innerText='Copy', 1200);">Copy</button>
</div>
</div>
</div>""", unsafe_allow_html=True)