import streamlit as st  # type: ignore
import pandas as pd  # type: ignore
import time

# =========================================================================
# PAGE CONFIG
# =========================================================================
st.set_page_config(
    page_title="🪐 StudyVerse Pro",
    page_icon="🪐",
    layout="wide"
)

# =========================================================================
# INITIALIZE SESSION STATES (TRACKING COMPLETIONS)
# =========================================================================
if "streak" not in st.session_state:
    st.session_state.streak = 0
if "messages" not in st.session_state:
    st.session_state.messages = []
if "bot_personality" not in st.session_state:
    st.session_state.bot_personality = "Encouraging Mentor"

# Track which chapters/tasks have been completed
if "completed_chapters" not in st.session_state:
    st.session_state.completed_chapters = {
        "Math: Algebra": False,
        "Math: Trigonometry": False,
        "Math: Probability": False,
        "Science: Biosphere": False,
        "English: Lexicon": False,
        "History: Timeline": False
    }

# =========================================================================
# CUSTOM NEON CYBERPUNK CSS
# =========================================================================
st.markdown("""
<style>
.main {
    background: radial-gradient(circle at center, #1e1b4b 0%, #0f172a 100%);
    color: #e2e8f0;
}
h1, h2, h3 {
    font-family: 'Courier New', Courier, monospace;
}
.stButton>button {
    background: linear-gradient(135deg, #a855f7 0%, #ec4899 100%);
    color: white !important;
    border-radius: 12px;
    border: 1px solid #f472b6;
    padding: 12px 24px;
    font-weight: bold;
    letter-spacing: 1px;
    box-shadow: 0 0 12px rgba(236, 72, 153, 0.3);
    transition: all 0.3s ease;
}
.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 0 25px rgba(168, 85, 247, 0.7);
    border-color: #fff;
}
.glass-card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    margin-bottom: 20px;
}
.cosmic-glow {
    text-align: center;
    font-size: 60px;
    font-weight: 900;
    background: linear-gradient(90deg, #3b82f6, #8b5cf6, #ec4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 30px rgba(139, 92, 246, 0.3);
    letter-spacing: 3px;
}
.streak-badge {
    background: linear-gradient(90deg, #f59e0b, #ef4444);
    padding: 8px 16px;
    border-radius: 20px;
    font-weight: bold;
    display: inline-block;
}
</style>
""", unsafe_allow_html=True)

CORRECT_SOUND = "https://www.soundjay.com/buttons/sounds/button-3.mp3"
WRONG_SOUND = "https://www.soundjay.com/buttons/sounds/button-10.mp3"

def play_sound(sound_url):
    st.audio(sound_url, format="audio/mp3", autoplay=True)

# =========================================================================
# SIDEBAR: STATS & SETTINGS
# =========================================================================
with st.sidebar:
    st.markdown("## 🛸 System Core")
    
    st.markdown(f"""
    <div style='text-align: center; margin-bottom: 20px;'>
        <p style='margin-bottom: 5px; color: #94a3b8;'>Current Study Streak</p>
        <span class='streak-badge'>🔥 {st.session_state.streak} Answers Right</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🛠️ Bot AI Module")
    st.session_state.bot_personality = st.selectbox(
        "Select Companion Matrix:",
        ["Encouraging Mentor", "Cyborg Drill Sergeant", "Sarcastic Genius"]
    )

# =========================================================================
# HEADER AREA
# =========================================================================
st.markdown('<h1 class="cosmic-glow">STUDYVERSE PRO</h1>', unsafe_allow_html=True)

# =========================================================================
# MAIN GRID: PRODUCTIVITY RADAR
# =========================================================================
st.markdown("## 📡 Mission Control Radar")
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="glass-card"><h3 style=\'color: #60a5fa;\'>📘 Orbital Assignment: Mathematics</h3><p style=\'color: #94a3b8;\'>Status: Critical</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="glass-card"><h3 style=\'color: #f472b6;\'>🧪 Lab Report: Quantum Chemistry</h3><p style=\'color: #94a3b8;\'>Status: Pending</p></div>', unsafe_allow_html=True)

# =========================================================================
# THE CHATBOT
# =========================================================================
with st.expander("🤖 Access AI Study Companion"):
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input("Communicate with your AI study droid..."):
        with st.chat_message("user"):
            st.write(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        p_choice = st.session_state.bot_personality
        if p_choice == "Cyborg Drill Sergeant":
            response = f"🎖️ Drop and give me 20 flashcards! Procrastination is a system error! You asked: '{prompt}'."
        elif p_choice == "Sarcastic Genius":
            response = f"🧠 Oh, an existential question about '{prompt}'? Let's get back to your modules first."
        else:
            response = f"✨ Star-student, you're doing incredibly well. Regarding '{prompt}', let's keep working!"

        with st.chat_message("assistant"):
            st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# =========================================================================
# GAMIFIED REVISION HUB
# =========================================================================
st.markdown("---")
st.header("🌌 Sub-Space Revision Hub")

subject = st.selectbox("Boot Sector Subject:", ["Quantum Mathematics", "Bio-Chemical Science", "Universal Linguistics", "Chronological History"])

# Helper function to easily mark a core module as completed
def render_complete_button(chapter_key):
    if not st.session_state.completed_chapters[chapter_key]:
        if st.button("🚀 Mark Chapter as Completed", key=f"btn_{chapter_key}"):
            st.session_state.completed_chapters[chapter_key] = True
            st.success(f"🎉 {chapter_key} logged into core memory!")
            st.balloons()
            time.sleep(1)
            st.rerun()
    else:
        st.info("✅ This chapter is completed and synced to your progress!")
        if st.button("🔄 Reset Chapter Progress", key=f"reset_{chapter_key}"):
            st.session_state.completed_chapters[chapter_key] = False
            st.rerun()

if subject == "Quantum Mathematics":
    st.subheader("➗ Operator Module: Mathematics")
    chapter = st.radio("Select Sub-Node Topic:", ["Algebra", "Trigonometry", "Probability"])
    
    if chapter == "Algebra":
        st.info("Formula Data-Stream: $(a+b)^2 = a^2 + 2ab + b^2$")
        math_ans = st.text_input("Solve for Matrix $x$: $4x - 12 = 20$")
        if st.button("Compute Answer Verification"):
            if math_ans.strip() == "8":
                st.success("🎯 Puzzle Correctly Handled!")
                st.session_state.streak += 1
                play_sound(CORRECT_SOUND)
            else:
                st.error("🚨 Inversion error.")
                st.session_state.streak = 0
                play_sound(WRONG_SOUND)
        render_complete_button("Math: Algebra")

    elif chapter == "Trigonometry":
        st.info("📐 $sin^2θ + cos^2θ = 1$")
        render_complete_button("Math: Trigonometry")

    elif chapter == "Probability":
        st.info("🎲 Probability = Favorable Outcomes / Total Outcomes")
        render_complete_button("Math: Probability")

elif subject == "Bio-Chemical Science":
    st.subheader("🧪 Biosphere Analysis")
    st.write("Rapid Quiz: What gas do paths absorb for photosynthesis?")
    sci_ans = st.text_input("Type compound signature here:")
    if st.button("Analyze Substance"):
        if "carbon dioxide" in sci_ans.lower() or "co2" in sci_ans.lower():
            st.success("🌱 Biological scan match positive!")
            st.session_state.streak += 1
            play_sound(CORRECT_SOUND)
        else:
            st.error("☣️ Scan failed.")
            st.session_state.streak = 0
            play_sound(WRONG_SOUND)
    render_complete_button("Science: Biosphere")

elif subject == "Universal Linguistics":
    st.subheader("📖 Lexicon Bank")
    word_query = st.text_input("Input local keyword (Try: happy, sad, smart):")
    synonyms = {"happy": "radiant / euphoric", "sad": "melancholic", "smart": "hyper-cognitive"}
    if word_query and word_query.lower() in synonyms:
        st.success(f"✨ Translatron outputs: **{synonyms[word_query.lower()]}**")
    render_complete_button("English: Lexicon")

elif subject == "Chronological History":
    st.subheader("🏛️ Timeline Data-Grids")
    history_df = pd.DataFrame({
        "Event": ["WW1 Begins", "Malaysia Independence", "Moon Landing"],
        "Year": [1914, 1957, 1969]
    })
    st.dataframe(history_df, use_container_width=True)
    render_complete_button("History: Timeline")

# =========================================================================
# AUTO-DETECTING PROGRESS TRACKER (THE UPDATE)
# =========================================================================
st.markdown("---")
st.header("🎯 Auto-Detecting Progress Core")

# Calculate metrics dynamically
total_chapters = len(st.session_state.completed_chapters)
completed_count = sum(1 for status in st.session_state.completed_chapters.values() if status)
calculated_percentage = int((completed_count / total_chapters) * 100)

# Display Stats
col_stat1, col_stat2 = st.columns(2)
col_stat1.metric("Modules Completed", f"{completed_count} / {total_chapters}")
col_stat2.metric("Sync Completion Percentage", f"{calculated_percentage}%")

# Progress bar
st.progress(calculated_percentage / 100)

# System Status Prompts
if calculated_percentage == 100:
    st.success("🔥 ULTIMATE OVERLOAD: 100% Core systems synced! You are a productivity powerhouse today!")
elif calculated_percentage >= 50:
    st.info("🛡️ Steady operational profile. Keep knocking out those chapters!")
else:
    st.warning("📚 Operational efficiency low. Check-in and mark chapters as completed to advance power grids.")
    