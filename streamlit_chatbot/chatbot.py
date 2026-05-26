import streamlit as st
import pandas as pd
 # Set page title
  st.title("My First Streamlit App")

  # Add header
  st.header("Welcome to the dashboard")
 
  # Add text
  st.write("This is a simple demonstration of Streamlit capabilities")
# Creating a Simple Streamlit Chatbot
def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def main():
    st.title("Simple Chatbot")
    
    initialize_session_state()

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    if prompt := st.chat_input("What's on your mind?"):
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)
        
        # Add user message to history
```        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Add simple bot response
        response = f"You said: {prompt}"
        
        # Display bot message
        with st.chat_message("assistant"):
            st.write(response)
        
        # Add bot message to history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
# Sample DataFrame
df = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'January'],
    'Price': [1000, 1500, 2000, 1200]
})

# Add sidebar
st.sidebar.header("Filters")

# Add dropdown
selected_month = st.sidebar.selectbox(
    "Select Month",
    options=df['Month'].unique()
)

# Add slider
price_range = st.sidebar.slider(
    "Select Price Range",
    min_value=0,
    max_value=3000,
    value=(0, 3000)
)
# ==========================================
# FUN REMINDER APP 🎀
# Reminder app with:
# ✅ Pop-up reminder notifications
# ✅ "Remind Me Later" punishment quiz
# ✅ Beautiful decorations
# ✅ Task management
# ==========================================

import tkinter as tk
from tkinter import messagebox
import random

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("✨ Study Guardian Reminder App ✨")
root.geometry("700x500")
root.config(bg="#ffe6f2")

tasks = []

# ---------------- TITLE ----------------
title = tk.Label(
    root,
    text="🌸 Study Guardian 🌸",
    font=("Comic Sans MS", 24, "bold"),
    bg="#ffe6f2",
    fg="#ff3399"
)
title.pack(pady=10)

subtitle = tk.Label(
    root,
    text="Finish your work before the guardian catches you 👀",
    font=("Arial", 11),
    bg="#ffe6f2",
    fg="#993366"
)
subtitle.pack()

# ---------------- TASK ENTRY ----------------
frame = tk.Frame(root, bg="#ffe6f2")
frame.pack(pady=20)

task_entry = tk.Entry(frame, width=40, font=("Arial", 14))
task_entry.grid(row=0, column=0, padx=10)

def add_task():
    task = task_entry.get()

    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, "📌 " + task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

add_btn = tk.Button(
    frame,
    text="➕ Add Task",
    command=add_task,
    bg="#ff66b3",
    fg="white",
    font=("Arial", 12, "bold"),
    relief="raised"
)
add_btn.grid(row=0, column=1)

# ---------------- TASK LIST ----------------
listbox = tk.Listbox(
    root,
    width=60,
    height=10,
    font=("Arial", 12),
    bg="white",
    fg="#cc0066",
    selectbackground="#ff99cc"
)
listbox.pack(pady=10)

# ---------------- COMPLETE TASK ----------------
def complete_task():
    selected = listbox.curselection()

    if selected:
        task_index = selected[0]
        completed_task = tasks.pop(task_index)
        listbox.delete(task_index)

        messagebox.showinfo(
            "Great Job!",
            f"🎉 You completed:\n{completed_task}"
        )
    else:
        messagebox.showwarning("Warning", "Select a task first!")

complete_btn = tk.Button(
    root,
    text="✅ Complete Task",
    command=complete_task,
    bg="#66cc66",
    fg="white",
    font=("Arial", 12, "bold")
)
complete_btn.pack(pady=5)

# ---------------- QUIZ QUESTIONS ----------------
quiz_questions = [
    ("What is 5 + 3?", "8"),
    ("What color is the sky?", "blue"),
    ("What is 10 - 4?", "6"),
    ("Type the word: focus", "focus"),
    ("What is 9 x 2?", "18")
]

# ---------------- REMINDER POPUP ----------------
def reminder_popup():
    if len(tasks) > 0:

        popup = tk.Toplevel(root)
        popup.title("⚠ Reminder!")
        popup.geometry("400x250")
        popup.config(bg="#fff0f5")

        msg = tk.Label(
            popup,
            text="📚 You still have unfinished work!",
            font=("Comic Sans MS", 16, "bold"),
            bg="#fff0f5",
            fg="#ff0066"
        )
        msg.pack(pady=20)

        task_label = tk.Label(
            popup,
            text="Current Task:\n" + random.choice(tasks),
            font=("Arial", 13),
            bg="#fff0f5",
            fg="#660033"
        )
        task_label.pack(pady=10)

        # ---------- FINISH NOW ----------
        def finish_now():
            popup.destroy()
            messagebox.showinfo(
                "Motivation",
                "🔥 YOU CAN DO IT! Go finish your work!"
            )

        # ---------- REMIND ME LATER ----------
        def remind_later():
            popup.destroy()
            show_quiz()

        finish_btn = tk.Button(
            popup,
            text="💪 Finish Now",
            command=finish_now,
            bg="#66cc66",
            fg="white",
            font=("Arial", 11, "bold"),
            width=15
        )
        finish_btn.pack(pady=5)

        later_btn = tk.Button(
            popup,
            text="😴 Remind Me Later",
            command=remind_later,
            bg="#ff6666",
            fg="white",
            font=("Arial", 11, "bold"),
            width=15
        )
        later_btn.pack(pady=5)

    # repeat reminder every 20 seconds
    root.after(20000, reminder_popup)

# ---------------- QUIZ WINDOW ----------------
def show_quiz():

    question, answer = random.choice(quiz_questions)

    quiz = tk.Toplevel(root)
    quiz.title("🧠 Punishment Quiz")
    quiz.geometry("400x250")
    quiz.config(bg="#e6f7ff")

    title = tk.Label(
        quiz,
        text="⚡ Punishment Time! ⚡",
        font=("Comic Sans MS", 18, "bold"),
        bg="#e6f7ff",
        fg="#0066cc"
    )
    title.pack(pady=10)

    q_label = tk.Label(
        quiz,
        text=question,
        font=("Arial", 14),
        bg="#e6f7ff"
    )
    q_label.pack(pady=10)

    answer_entry = tk.Entry(quiz, font=("Arial", 14))
    answer_entry.pack(pady=10)

    def check_answer():
        user_answer = answer_entry.get().lower()

        if user_answer == answer:
            messagebox.showinfo(
                "Correct!",
                "🎉 Okay fine... reminder delayed."
            )
            quiz.destroy()

        else:
            messagebox.showerror(
                "Wrong!",
                "❌ Wrong answer! Try again!"
            )

    submit_btn = tk.Button(
        quiz,
        text="Submit",
        command=check_answer,
        bg="#3399ff",
        fg="white",
        font=("Arial", 12, "bold")
    )
    submit_btn.pack(pady=10)

# ---------------- DECORATIONS ----------------
decor = tk.Label(
    root,
    text="🌸✨💖🌈🦄⭐📚✨🌸",
    font=("Arial", 20),
    bg="#ffe6f2"
)
decor.pack(pady=20)

# Start reminder system
root.after(20000, reminder_popup)

# Run app
root.mainloop()