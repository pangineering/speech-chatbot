import streamlit as st
from PIL import Image
import logging
import time
import torch
import torchaudio
import wave
import json
import os
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
from pathlib import Path
import numpy as np
from settings import IMAGE_DIR, DURATION, WAVE_OUTPUT_FILE
from src.sound import sound
from setup_logging import setup_logging
from modeules.sr_modules import SR_Module
import os

import glob
from transformers import AutoProcessor, AutoModelForCTC
from datetime import date

setup_logging()
logger = logging.getLogger('app')

# init the models
# processor = AutoProcessor.from_pretrained(
#     "airesearch/wav2vec2-large-xlsr-53-th")

# model = AutoModelForCTC.from_pretrained("airesearch/wav2vec2-large-xlsr-53-th")

# Functions


def get_spectrogram(type='mel'):
    logger.info("Extracting spectrogram")
    y, sr = librosa.load(WAVE_OUTPUT_FILE, duration=DURATION)
    ps = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
    logger.info("Spectrogram Extracted")
    format = '%+2.0f'
    if type == 'DB':
        ps = librosa.power_to_db(ps, ref=np.max)
        format = ''.join[format, 'DB']
        logger.info("Converted to DB scale")
    return ps, format


def display(spectrogram, format):
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(spectrogram, y_axis='mel', x_axis='time')
    plt.title('Mel-frequency spectrogram')
    plt.colorbar(format=format)
    plt.tight_layout()
    st.pyplot(clear_figure=False)


# Title
st.title('KPop Chatbot')


# Audio Input
if st.button('Record'):
        with st.spinner(f'Recording for {DURATION} seconds ....'):
            sound.record()
        st.success("Recording completed")

if st.button('Play'):
        # sound.play()
    try:
        audio_file = open(WAVE_OUTPUT_FILE, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/wav')
    except:
        st.write("Please record sound first")

if st.button('Send'):
    sr = SR_Module(audio=WAVE_OUTPUT_FILE)
    text = sr.get_audio()
    st.text(text)
    #print(text)
# Chat box