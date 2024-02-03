import get_reply
import streamlit as st

# https://drive.google.com/uc?id=1qEFRPuwAJxxjORe-6vaC-WyLgTot_vaF
st.title("Welcome to STAR CAFE's Chatbot!")

tab1, tab2 = st.tabs(["Home Page", "CHAT HISTORY"])

with tab1:
    col1, col2= st.columns(2, gap = "large")

    with col1:
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write("MOST FASTEST & CONVENIENT WAY")
        st.write("TO ORDER A COFFEE")
        st.write(" ")
        st.write(" ")
        st.write('Just type "Order me a frappe".')



    # with col2:    
    #     st.image(image= "https://drive.google.com/uc?id=1qEFRPuwAJxxjORe-6vaC-WyLgTot_vaF", width=300 )


if prompt := st.chat_input(' ORDER  ME  FRAPPE  AND  AMERICANO  .....'):
        response = get_reply.reply(prompt)
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



