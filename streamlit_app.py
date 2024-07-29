import streamlit as st

st.set_page_config(layout='wide')


st.title("Welcome to STAR CAFE's Chatbot!")

tab1, tab2 = st.tabs(["Home Page", "CHAT HISTORY"])


with tab1:
        st.write(" ")
        st.write(" ")
        st.write(" ")
        c1,c2,c3 = st.columns(3)
        with c2:
            st.link_button("ClICK HERE TO VISIT MENU", url="https://jp5.pythonanywhere.com/star-cafe-menu")
        st.write(" ")
        st.header("MOST FASTEST , SMARTEST AND CONVENIENT WAY TO ORDER A COFFEE")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.header('JUST TYPE "Order me a frappe" AND GET YOUR COFFEE ON YOUR TABLE.')



if prompt := st.chat_input(' ORDER  ME  FRAPPE  AND  AMERICANO  .....'):
        # response = get_reply.reply(prompt)
        response = "REPLY"
        
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Get bot response    
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

with tab2:
        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = [] 
            st.session_state.messages.append({
                "role": "assistant", 
                "content": "Welcome to the chatbot. How can I help you?"
                })

        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])



