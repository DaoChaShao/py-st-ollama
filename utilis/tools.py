#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/2/21 17:56
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   tools.py
# @Desc     :   

from requests import post
from streamlit import sidebar, header, selectbox, caption, slider
from time import perf_counter


def parameters() -> tuple[str, int, int]:
    with sidebar:
        header("Parameters")
        options: list = ["qwen2.5:14b", "phi4:latest", "llama3.1:latest"]
        model: str = selectbox(
            "Model", ["Select a Model"] + options, help="Select a model"
        )
        if model in options:
            caption(f"The model you selected is: **{model}**")

        temperature: int = slider("Temperature", 0.0, 2.0, 0.8, help="The randomness of the output.")
        if temperature:
            caption(f"The temperature you selected is: **{temperature}**")

        top_p: int = slider("Top P", 0.0, 1.0, 0.9, help="The probability of the output.")
        if top_p:
            caption(f"The top P you selected is: **{top_p}**")

        return model, temperature, top_p


def model_caller(model_name: str, temperature: float, top_p: int, prompt: str) -> str:
    """ Call the Ollama model locally via requests package.

    :param model_name: the name of the model
    :param temperature: the randomness of the output
    :param top_p: the probability of the output
    :param prompt: the input from the user
    :return: the response from the model
    """
    URL: str = "http://localhost:11434/api/generate"

    payload: dict = {
        "model": model_name,
        "temperature": temperature,
        "top_p": top_p,
        "stream": False,
        "prompt": prompt,
    }

    response = post(URL, json=payload)
    print(response.json()["response"])
    return response.json()["response"]


class Timer(object):
    def __init__(self, precision: int = 5, description: str = None):
        self._precision = precision
        self._description = description

    def __enter__(self):
        self._start = perf_counter()
        return self

    def __exit__(self, *args):
        self._end = perf_counter()
        self._elapsed = self._end - self._start

    def __repr__(self):
        return f"{self._description} took {self._elapsed:.{self._precision}f} seconds."
