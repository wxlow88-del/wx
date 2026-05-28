import streamlit as st  # type: ignore
import pandas as pd  # type: ignore

# =========================================================================
# SECTION 1: BASIC STREAMLIT STRUCTURE
# =========================================================================

# Set page title
st.title("My First Streamlit App")

# Add header
st.header("Welcome to the dashboard")

# Add text
st.write("This is a simple demonstration of Streamlit capabilities")

st.markdown("---")
st.title("Simple Chatbot")

# Initialize chat history state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "quiz_active" not in st.session_state:
    st.session_state.quiz_active = False

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
        
# Chat Input
if prompt := st.chat_input("What's on your mind?"):
    with st.chat_message("user"):
        st.write(prompt)
        
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = f"You said: {prompt}"
    
    with st.chat_message("assistant"):
        st.write(response)
        
    st.session_state.messages.append({"role": "assistant", "content": response})


# =========================================================================
# SECTION 2: YOUR APP'S CODE (Reminder App & Procrastination Quiz)
# =========================================================================
st.markdown("---")
st.header("⏰ Student Productivity & Wellness Tracker")

st.write("### 📝 Your Unfinished Assignments")
col1, col2 = st.columns(2)
with col1:
    st.info("📚 Math Homework (Due: Tonight)")
with col2:
    st.info("🧪 Chemistry Lab Report (Due: Friday)")
    
# In-App Notification Alert
st.warning("⚠️ **NOTIFICATION:** You have 2 assignments due soon! Work on them now?")

btn_col1, btn_col2 = st.columns(2)
with btn_col1:
    if st.button("✅ Yes, I'm working on it!"):
        st.success("Great job! Keep up the productivity! 🎉")
        st.session_state.quiz_active = False
        
with btn_col2:
    if st.button("⏳ Remind me later..."):
        st.session_state.quiz_active = True

# The Quiz punishment logic
if st.session_state.quiz_active:
    st.error("🚨 Procrastination detected! You must solve this quiz to snooze your reminder!")
    st.write("**Question: What is 12 x 12?**")
    
    user_answer = st.text_input("Type your answer here:", key="quiz_input")
    if st.button("Submit Quiz Answer"):
        if user_answer.strip() == "144":
            st.success("🎯 Correct! Your reminder is successfully snoozed. Get back to work soon!")
            st.balloons()
            st.session_state.quiz_active = False
        else:
            st.error("❌ Wrong answer! Try again or face the ultimate guilt of unfinished work!")

# =========================================================================
# SECTION 3: STUDY REVISION HUB
# =========================================================================
st.markdown("---")
st.header("📚 Study Revision Hub")

st.write("Choose a subject to revise today!")

# Subject selection
subject = st.selectbox(
    "Select Subject:",
    ["Mathematics", "Science", "History", "English"]
)

# Different revision content for each subject
if subject == "Mathematics":
    st.subheader("➗ Mathematics Revision")
    
    chapter = st.radio(
        "Choose a chapter:",
        ["Algebra", "Trigonometry", "Probability"]
    )
    
    if chapter == "Algebra":
        st.info("📘 Formula: (a + b)² = a² + 2ab + b²")
        answer = st.text_input("Solve: 5x + 3 = 18")
        
        if st.button("Check Math Answer"):
            if answer.strip() == "3":
                st.success("✅ Correct! Great job!")
            else:
                st.error("❌ Incorrect. Try again!")

    elif chapter == "Trigonometry":
        st.info("📐 sin²θ + cos²θ = 1")
        st.write("Remember SOH CAH TOA!")

    elif chapter == "Probability":
        st.info("🎲 Probability = Number of favourable outcomes / Total outcomes")
        st.write("Example: Probability of getting heads from a coin = 1/2")

elif subject == "Science":
    st.subheader("🧪 Science Revision")
    
    st.write("### Quick Facts")
    st.success("🌍 Water boils at 100°C")
    st.success("⚡ Humans have 206 bones")
    st.success("🌱 Photosynthesis needs sunlight")

    quiz = st.text_input("What gas do plants absorb?")
    
    if st.button("Check Science Answer"):
        if quiz.lower() == "carbon dioxide":
            st.success("✅ Correct!")
        else:
            st.error("❌ Try again!")

elif subject == "History":
    st.subheader("🏛️ History Revision")
    
    st.write("### Important Dates")
    
    history_df = pd.DataFrame({
        "Event": [
            "World War 1 Begins",
            "Malaysia Independence",
            "Moon Landing"
        ],
        "Year": [
            1914,
            1957,
            1969
        ]
    })

    st.table(history_df)

elif subject == "English":
    st.subheader("📖 English Revision")
    
    word = st.text_input("Enter a word to learn its synonym:")
    
    synonyms = {
        "happy": "joyful",
        "sad": "unhappy",
        "smart": "intelligent"
    }

    if word:
        if word.lower() in synonyms:
            st.success(f"✨ Synonym: {synonyms[word.lower()]}")
        else:
            st.warning("No synonym found in mini dictionary.")

# Study progress tracker
st.markdown("---")
st.write("### 🎯 Daily Study Progress")

progress = st.slider("How much have you studied today?", 0, 100, 40)

st.progress(progress / 100)

if progress >= 80:
    st.balloons()
    st.success("🔥 Amazing productivity today!")
elif progress >= 50:
    st.info("👍 Good progress! Keep going!")
else:
    st.warning("📚 Time to focus and study more!")
    import streamlit as st  # type: ignore
import pandas as pd  # type: ignore
import base64

# =========================================================================
# PAGE CONFIG
# =========================================================================
st.set_page_config(
    page_title="🎓 StudyVerse",
    page_icon="📚",
    layout="wide"
)

# =========================================================================
# CUSTOM CSS (COLORS + THEME)
# =========================================================================
st.markdown("""
<style>

body {
    background-color: #0f172a;
}

.main {
    background: linear-gradient(to bottom right, #1e293b, #0f172a);
    color: white;
}

h1, h2, h3 {
    color: #f8fafc !important;
}

.stButton>button {
    background: linear-gradient(90deg, #8b5cf6, #ec4899);
    color: white;
    border-radius: 15px;
    border: none;
    padding: 10px 20px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #ec4899, #8b5cf6);
}

.stTextInput input {
    border-radius: 10px;
    border: 2px solid #8b5cf6;
}

.stSelectbox div[data-baseweb="select"] {
    border-radius: 10px;
}

.css-1d391kg {
    background-color: #111827;
}

.glow {
    text-align: center;
    font-size: 50px;
    color: white;
    text-shadow: 0 0 10px #a855f7,
                 0 0 20px #a855f7,
                 0 0 40px #ec4899;
}

.card {
    background-color: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 0 15px rgba(236,72,153,0.4);
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================================
# SOUND EFFECT FUNCTION
# =========================================================================
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()

    b64 = base64.b64encode(data).decode()

    md = f"""
    <audio autoplay="true">
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """

    st.markdown(md, unsafe_allow_html=True)

# =========================================================================
# TITLE
# =========================================================================
st.markdown('<h1 class="glow">🎓 STUDYVERSE</h1>', unsafe_allow_html=True)

st.write("### Your Ultimate Productivity & Revision Companion 🚀")

# =========================================================================
# SIMPLE CHATBOT
# =========================================================================
st.markdown("---")
st.header("🤖 AI Study Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Ask me anything about studying..."):
    
    with st.chat_message("user"):
        st.write(prompt)

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    response = f"📚 Study Bot says: Keep going! You asked: {prompt}"

    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

# =========================================================================
# PRODUCTIVITY TRACKER
# =========================================================================
st.markdown("---")
st.header("⏰ Productivity Tracker")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    <h3>📘 Math Homework</h3>
    <p>Due Tonight</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>🧪 Chemistry Report</h3>
    <p>Due Friday</p>
    </div>
    """, unsafe_allow_html=True)

st.warning("⚠️ You still have unfinished assignments!")

btn1, btn2 = st.columns(2)

with btn1:
    if st.button("✅ Start Studying"):
        st.success("🔥 Great! Productivity Mode Activated!")
        st.balloons()

with btn2:
    if st.button("😴 Remind Me Later"):
        st.error("🚨 Procrastination Detected!")

# =========================================================================
# SOUND EFFECTS
# =========================================================================
CORRECT_SOUND = "https://www.soundjay.com/buttons/sounds/button-3.mp3"
WRONG_SOUND = "https://www.soundjay.com/buttons/sounds/button-10.mp3"

def play_sound(sound_url):
    st.audio(sound_url, format="audio/mp3", autoplay=True)

# =========================================================================
# REVISION HUB
# =========================================================================
st.markdown("---")
st.header("📚 Revision Hub")

subject = st.selectbox(
    "Choose your subject:",
    ["Mathematics", "Science", "English", "History"]
)

if subject == "Mathematics":

    st.subheader("➗ Mathematics")

    chapter = st.radio(
        "Select Topic:",
        ["Algebra", "Trigonometry", "Probability"]
    )

    if chapter == "Algebra":

        st.info("📘 Formula: (a+b)² = a² + 2ab + b²")

        answer = st.text_input("Solve: 2x + 8 = 20")

        if st.button("Check Answer"):
            if answer == "6":
                st.success("✅ Correct!")
                play_sound(CORRECT_SOUND)
                st.balloons()
            else:
                st.error("❌ Wrong answer!")
                play_sound(WRONG_SOUND)

elif subject == "Science":

    st.subheader("🧪 Science")

    st.success("🌱 Photosynthesis uses sunlight.")
    st.success("⚡ Humans have 206 bones.")
    st.success("🌍 Earth revolves around the Sun.")

    science = st.text_input("What planet do we live on?")

    if st.button("Submit Science Quiz"):
        if science.lower() == "earth":
            st.success("🌎 Correct!")
        else:
            st.error("❌ Try again!")

elif subject == "English":

    st.subheader("📖 English")

    word = st.text_input("Enter a word:")

    synonyms = {
        "happy": "joyful",
        "sad": "unhappy",
        "smart": "intelligent"
    }

    if word:
        if word.lower() in synonyms:
            st.success(
                f"✨ Synonym: {synonyms[word.lower()]}"
            )
        else:
            st.warning("No synonym found.")

elif subject == "History":

    st.subheader("🏛️ History")

    history_df = pd.DataFrame({
        "Event": [
            "WW1 Begins",
            "Malaysia Independence",
            "Moon Landing"
        ],
        "Year": [1914, 1957, 1969]
    })

    st.dataframe(history_df)

# =========================================================================
# =========================================================
# AUTO STUDY PROGRESS TRACKER
# =========================================================

st.markdown("---")
st.header("📊 Smart Study Progress Tracker")

# =========================================================
# SUBJECT DATA
# =========================================================

subjects = {
    "Mathematics": [
        "Algebra",
        "Trigonometry",
        "Probability",
        "Calculus"
    ],

    "Science": [
        "Biology",
        "Chemistry",
        "Physics",
        "Astronomy"
    ],

    "English": [
        "Grammar",
        "Essay Writing",
        "Vocabulary",
        "Comprehension"
    ],

    "History": [
        "World War 1",
        "World War 2",
        "Malaysia Independence",
        "Cold War"
    ]
}

# =========================================================
# SESSION STORAGE
# =========================================================

if "completed_topics" not in st.session_state:
    st.session_state.completed_topics = {}

# =========================================================
# SUBJECT SELECT
# =========================================================

selected_subject = st.selectbox(
    "Choose Subject",
    list(subjects.keys())
)

topics = subjects[selected_subject]

st.subheader(f"📚 {selected_subject} Chapters")

# =========================================================
# CREATE CHECKBOXES
# =========================================================

completed_count = 0

for topic in topics:

    key_name = f"{selected_subject}_{topic}"

    checked = st.checkbox(
        f"✅ {topic}",
        key=key_name
    )

    if checked:
        completed_count += 1

# =========================================================
# CALCULATE PROGRESS
# =========================================================

total_topics = len(topics)

progress_percentage = int(
    (completed_count / total_topics) * 100
)

# =========================================================
# DISPLAY PROGRESS
# =========================================================

st.write(f"### 🎯 {selected_subject} Progress")

st.progress(progress_percentage / 100)

st.success(
    f"{progress_percentage}% completed"
)

# =========================================================
# MOTIVATION SYSTEM
# =========================================================

if progress_percentage == 100:

    st.balloons()

    st.success(
        f"🏆 Amazing! You completed all {selected_subject} chapters!"
    )

elif progress_percentage >= 75:

    st.info(
        "🔥 Almost there! Keep going!"
    )

elif progress_percentage >= 50:

    st.info(
        "👍 Great progress so far!"
    )

else:

    st.warning(
        "📚 Start studying to increase progress!"
    )

# =========================================================
# OVERALL PROGRESS
# =========================================================

st.markdown("---")
st.subheader("🌍 Overall Study Completion")

overall_total = 0
overall_completed = 0

for subject_name, subject_topics in subjects.items():

    overall_total += len(subject_topics)

    for topic in subject_topics:

        key_name = f"{subject_name}_{topic}"

        if st.session_state.get(key_name, False):
            overall_completed += 1

overall_progress = int(
    (overall_completed / overall_total) * 100
)

st.progress(overall_progress / 100)

st.write(
    f"📈 Overall Completion: {overall_progress}%"
)

# =========================================================
# ACHIEVEMENTS
# =========================================================

if overall_progress == 100:

    st.success("🏅 Ultimate Study Master!")

elif overall_progress >= 75:

    st.success("🥇 Elite Student!")

elif overall_progress >= 50:

    st.info("🥈 Rising Scholar!")

else:

    st.warning("✨ Keep learning every day!")
# =========================================================================
# SOUND EFFECTS
# =========================================================================
def play_correct_sound():
    st.markdown("""
        <audio autoplay>
        <source src="https://www.soundjay.com/buttons/sounds/button-3.mp3" type="audio/mp3">
        </audio>
    """, unsafe_allow_html=True)

def play_wrong_sound():
    st.markdown("""
        <audio autoplay>
        <source src="https://www.soundjay.com/buttons/sounds/button-10.mp3" type="audio/mp3">
        </audio>
    """, unsafe_allow_html=True)
# =========================================================
# 🐹 HAMSTER VIRTUAL PET SYSTEM
# =========================================================

elif menu == "🐹 Study Hamster":

    st.header("🐹 Study Hamster")

    st.write(
        "Your hamster grows stronger when you study! 📚"
    )

    # =====================================================
    # SESSION STATES
    # =====================================================

    if "hamster_xp" not in st.session_state:
        st.session_state.hamster_xp = 0

    if "hamster_hunger" not in st.session_state:
        st.session_state.hamster_hunger = 100

    if "hamster_happiness" not in st.session_state:
        st.session_state.hamster_happiness = 100

    if "hamster_name" not in st.session_state:
        st.session_state.hamster_name = "Mochi"

    # =====================================================
    # NAME CUSTOMIZATION
    # =====================================================

    hamster_name = st.text_input(
        "Name Your Hamster",
        value=st.session_state.hamster_name
    )

    st.session_state.hamster_name = hamster_name

    # =====================================================
    # LEVEL SYSTEM
    # =====================================================

    xp = st.session_state.hamster_xp

    if xp < 20:

        hamster = "🐹"
        level = "Baby Hamster"

    elif xp < 50:

        hamster = "🐹🎀"
        level = "Cute Hamster"

    elif xp < 100:

        hamster = "🐹📚"
        level = "Study Hamster"

    elif xp < 200:

        hamster = "🐹👑"
        level = "Elite Hamster"

    else:

        hamster = "🐹🔥"
        level = "Legendary Hamster"

    # =====================================================
    # DISPLAY PET
    # =====================================================

    st.markdown(f"""
    <div class="card">
    <h1 style='text-align:center;font-size:90px'>
    {hamster}
    </h1>

    <h2 style='text-align:center'>
    {st.session_state.hamster_name}
    </h2>

    <h3 style='text-align:center'>
    {level}
    </h3>
    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # STATS
    # =====================================================

    st.subheader("📊 Hamster Stats")

    st.write(f"⭐ XP: {xp}")
    st.progress(min(xp / 200, 1.0))

    st.write(
        f"😊 Happiness: {st.session_state.hamster_happiness}%"
    )

    st.progress(
        st.session_state.hamster_happiness / 100
    )

    st.write(
        f"🍎 Hunger: {st.session_state.hamster_hunger}%"
    )

    st.progress(
        st.session_state.hamster_hunger / 100
    )

    # =====================================================
    # ACTION BUTTONS
    # =====================================================

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    # FEED
    with col1:

        if st.button("🥕 Feed Hamster"):

            st.session_state.hamster_hunger += 10

            if st.session_state.hamster_hunger > 100:
                st.session_state.hamster_hunger = 100

            st.success(
                f"{st.session_state.hamster_name} is full and happy!"
            )

    # PLAY
    with col2:

        if st.button("🎾 Play With Hamster"):

            st.session_state.hamster_happiness += 10

            if st.session_state.hamster_happiness > 100:
                st.session_state.hamster_happiness = 100

            st.success(
                f"{st.session_state.hamster_name} loved playing!"
            )

    # STUDY
    with col3:

        if st.button("📚 Study Together"):

            st.session_state.hamster_xp += 15

            st.session_state.hamster_happiness += 5

            st.success(
                f"{st.session_state.hamster_name} gained XP!"
            )

            st.balloons()

    # =====================================================
    # AUTO DECAY
    # =====================================================

    st.session_state.hamster_hunger -= 1
    st.session_state.hamster_happiness -= 1

    if st.session_state.hamster_hunger < 0:
        st.session_state.hamster_hunger = 0

    if st.session_state.hamster_happiness < 0:
        st.session_state.hamster_happiness = 0

    # =====================================================
    # STATUS MESSAGES
    # =====================================================

    st.markdown("---")

    if st.session_state.hamster_hunger <= 30:

        st.warning(
            f"🥺 {st.session_state.hamster_name} is hungry!"
        )

    if st.session_state.hamster_happiness <= 30:

        st.warning(
            f"😢 {st.session_state.hamster_name} feels lonely!"
        )

    if (
        st.session_state.hamster_happiness >= 80
        and st.session_state.hamster_hunger >= 80
    ):

        st.success(
            f"🌟 {st.session_state.hamster_name} is extremely happy!"
        )

    # =====================================================
    # DAILY REWARD
    # =====================================================

    st.markdown("---")

    st.subheader("🎁 Daily Reward")

    if st.button("Claim Daily Seeds 🌻"):

        reward = random.randint(5, 20)

        st.session_state.hamster_xp += reward

        st.success(
            f"🎉 You gained {reward} XP!"
        )

    # =====================================================
    # ACCESSORY SHOP
    # =====================================================

    st.markdown("---")

    st.subheader("🛍️ Hamster Accessories")

    accessories = [
        "🎀 Pink Ribbon",
        "👑 Tiny Crown",
        "🕶️ Cool Glasses",
        "🎓 Graduation Hat"
    ]

    selected_accessory = st.selectbox(
        "Choose Accessory",
        accessories
    )

    if st.button("Equip Accessory"):

        st.success(
            f"{st.session_state.hamster_name} equipped {selected_accessory}!"
        )

    # =====================================================
    # STUDY BONUS
    # =====================================================

    st.markdown("---")

    st.subheader("🚀 Study Rewards")

    st.info("""
    📚 Complete study tasks to level up faster!

    Rewards:
    - Correct quizzes = +10 XP
    - Complete chapters = +15 XP
    - High productivity = +20 XP
    """)

    # =====================================================
    # ACHIEVEMENTS
    # =====================================================

    st.markdown("---")

    st.subheader("🏆 Hamster Achievements")

    if xp >= 200:

        st.success(
            "🐹🔥 Legendary Hamster Unlocked!"
        )

    elif xp >= 100:

        st.success(
            "👑 Elite Hamster Unlocked!"
        )

    elif xp >= 50:

        st.info(
            "📚 Study Hamster Unlocked!"
        )

    else:

        st.warning(
            "✨ Keep studying to unlock evolutions!"
        )
```
```python id="8ht9ms"
menu = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Dashboard",
        "🤖 AI Study Chat",
        "📚 Revision Hub",
        "⏰ Productivity",
        "🎯 Progress Tracker",
        "🐹 Study Hamster"
    ]
)
```

