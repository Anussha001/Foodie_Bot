import streamlit as st
from conversational_ai import FoodieBotConversationManager

def main():
    st.title("🍔 FoodieBot - Intelligent Food Recommendations")

    groq_api_key = st.secrets.get("GROQ_API_KEY", None)
    if not groq_api_key:
        st.error("Please set GROQ_API_KEY in Streamlit secrets or environment variables.")
        return

    if 'manager' not in st.session_state:
        st.session_state.manager = FoodieBotConversationManager(groq_api_key)
        st.session_state.session_id = f"session_{int(st.time())}"
        st.session_state.messages = []

    with st.sidebar:
        st.header("Session Info")
        # Display metrics about the current session here

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if prompt := st.chat_input("What kind of food are you craving?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        response = st.session_state.manager.process_message(prompt, st.session_state.session_id)
        st.session_state.messages.append({"role": "assistant", "content": response['bot_response']})

if __name__ == "__main__":
    main()
