import chainlit as cl
from chainlit import *
import requests
from get_reply import reply

# https://drive.google.com/uc?id=1qEFRPuwAJxxjORe-6vaC-WyLgTot_vaF
@cl.on_message
async def main(message: str):

    response = reply(message)
    await cl.Message(content=response).send()

