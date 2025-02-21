#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/21 17:58
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   home.py
# @Desc     :   

from streamlit import title, divider, expander, caption, empty

title("Call a Ollama Model Locally")
divider()
with expander("**TARGET**: Download the Ollama model and run it locally.", expanded=True):
    caption("1. Download the **INSTALLER** from [Ollama](https://ollama.com/).")
    caption("2. Download the **MODEL** you want to use.")
