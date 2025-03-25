import streamlit as st
import random
import json
import os

# File to store user data
USER_DATA_FILE = 'user_data.json'

# Load user data
def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save user data
def save_user_data(user_data):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(user_data, file, indent=4)

# Initialize user data
user_data = load_user_data()

st.image("IMG_9229.JPG", width=200)

# Chatbot response handling
def handle_user_input(user_input, greetings, farewells, fun_responses):
    user_input = user_input.lower().strip()

    # Greet only once per session
    if user_input in ["hi", "hello", "hey"] and "greeted" not in st.session_state:
        st.session_state["greeted"] = True
        return random.choice(greetings)
    
    # Farewells
    if user_input in ["bye", "goodbye", "see you"]:
        return random.choice(farewells)

    # Fun responses
    for key, response in fun_responses.items():
        if key in user_input:
            return response

    # Default response
    return "I'm not sure how to respond to that. Try asking something else!"

# Chatbot interface with custom chat bubbles
def chat_interface():
    st.title("MasterErin's Chatbot")
    st.write("Start a conversation with the chatbot! Type your message below.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Define unique chatbot responses
    greetings = ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Hey! Hope you're doing well."]
    farewells = ["Goodbye! Have a great day!", "See you later! Take care!", "Bye! Feel free to return if you have more questions."]
    fun_responses = {
        "how are you": "I'm just a virtual assistant, but I'm here and ready to chat!",
        "what's your name": "I am MasterErin, your AI chatbot!",
        "tell me a joke": random.choice([
            "Why don't skeletons fight? Because they don’t have the guts!",
            "Why did the scarecrow win an award? He was outstanding in his field!"
        ]),
        "tell me a story": random.choice([
            "Once upon a time, a curious cat named Whiskers set off on an adventure across the city...",
            "A young girl named Mia found a magic brush that brought her paintings to life..."
        ]),
        "quote": random.choice([
            "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
            "Do what you can, with what you have, where you are. - Theodore Roosevelt"
        ])
    }

    user_input = st.text_input("You:", key="user_input")

    if st.button("Send"):
        if user_input:
            response = handle_user_input(user_input, greetings, farewells, fun_responses)
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("MasterErin", response))

    # CSS for chat bubbles
    chat_styles = """
        <style>
            .chat-container {
                max-width: 600px;
                margin: auto;
            }
            .user-msg {
                background-color: #0084ff;
                color: white;
                padding: 10px 15px;
                border-radius: 15px;
                max-width: 80%;
                text-align: right;
                margin-left: auto;
            }
            .bot-msg {
                background-color: #ff4d4d;
                color: white;
                padding: 10px 15px;
                border-radius: 15px;
                max-width: 80%;
                text-align: left;
                margin-right: auto;
            }
            .chat-bubble {
                display: flex;
                margin-bottom: 10px;
            }
            .chat-container {
                background-color: #f9f9f9;
                padding: 20px;
                border-radius: 10px;
            }
        </style>
    """

    st.markdown(chat_styles, unsafe_allow_html=True)
    
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    # Display chat history with styled bubbles
    for speaker, message in st.session_state.chat_history:
        if speaker == "You":
            st.markdown(f'<div class="chat-bubble user-msg"><b>🧑‍💻 You:</b> {message}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-bubble bot-msg"><b>🤖 MasterErin:</b> {message}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Main app
st.title("MasterErin's Chat Platform")
st.subheader("Login or Create an Account")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    tab1, tab2 = st.tabs(["Login", "Create Account"])
    with tab1:
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username in user_data and user_data[username]["password"] == password:
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.success(f"Welcome, {username}! 🎉")
                chat_interface()
            else:
                st.error("Invalid username or password.")
    with tab2:
        st.subheader("Create an Account")
        new_username = st.text_input("Enter a username")
        new_password = st.text_input("Enter a password", type="password")
        if st.button("Create Account"):
            if new_username in user_data:
                st.warning("Username already exists. Please choose a different one.")
            else:
                user_data[new_username] = {"password": new_password, "profile": {}}
                save_user_data(user_data)
                st.success("Account created successfully! Please login.")
else:
    chat_interface()
