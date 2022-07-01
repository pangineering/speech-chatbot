import streamlit as st
from PIL import Image
import time
import torch
import torchaudio
import wave
import json
from synthesizer import Synthesizer
from encoder import inference as encoder
from vocoder import inference as vocoder
from pathlib import Path
import numpy as np
import soundfile as sf
import os
import librosa
import sounddevice as sd
import wavio
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