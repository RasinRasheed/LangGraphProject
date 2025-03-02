import streamlit as st
from datetime import datetime

from langchain_core.messages import AIMessage, HumanMessage
from src.langGraphAgenticAI.UI.streamlitUI.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config() #config
        self.user_control = {}
        
