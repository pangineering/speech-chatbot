import streamlit as st
from PIL import Image
import time
import torch
import torchaudio
import wave
import json

from pathlib import Path
import numpy as np

import os

import glob
from helper import draw_embed, create_spectrogram, read_audio
from transformers import AutoProcessor, AutoModelForCTC
from datetime import date

# Dowload the models
processor = AutoProcessor.from_pretrained("airesearch/wav2vec2-large-xlsr-53-th")

model = AutoModelForCTC.from_pretrained("airesearch/wav2vec2-large-xlsr-53-th")



# Title
st.title('KPop Chatbot')


# Audio Input with textbox

# Chat box