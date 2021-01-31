###################################################################### Para descargar mp4

from pytube import YouTube
import os


def downloadYouTube(videourl, path):
    yt = YouTube(videourl)
    yt = yt.streams.filter(only_audio=True).first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)


downloadYouTube("https://www.youtube.com/watch?v=WWy7ZWQiG8s", "./dl")

###################################################################### Para convertir a wav
import os
import ffmpy

inputdir = "/home/cristina/Desktop/hack/"
outdir = "/home/cristina/Desktop/hack/"

for filename in os.listdir(inputdir):
    actual_filename = filename[:-4]
    if filename.endswith(".mp4"):
        os.system(
            "ffmpeg -i {} -acodec pcm_s16le -ar 16000 {}/{}.wav".format(
                filename, outdir, actual_filename
            )
        )
    else:
        continue

##################################################################### Para cortar audio

from pydub import AudioSegment
import math


class SplitWavAudioMubin:
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + "/" + filename

        self.audio = AudioSegment.from_wav(self.filepath)

    def get_duration(self):
        return self.audio.duration_seconds

    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + "/" + split_filename, format="wav")

    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 60)
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + "_" + self.filename
            self.single_split(i, i + min_per_split, split_fn)
            print(str(i) + " Done")
            if i == total_mins - min_per_split:
                print("All splited successfully")


# # folder = '/home/cristina/Desktop/hack'
filename = "5_ESSENTIAL_Tools_for_New_Coders.wav"
# # split_wav = SplitWavAudioMubin(folder, file)
split_filename = "split_" + filename
# # split_wav.single_split(1,2,split_filename)


###################################################################### Para extraer frecuencias
# Load the required libraries:
#   * scipy
#   * numpy
#   * matplotlib
from scipy.io import wavfile
from matplotlib import pyplot as plt
import numpy as np

# # Load the data and calculate the time of each sample
samplerate, data = wavfile.read(split_filename)

import sys
from aubio import source, pitch

win_s = 4096
hop_s = 512

s = source(split_filename, samplerate, hop_s)
samplerate = s.samplerate

tolerance = 0.8

pitch_o = pitch("yin", win_s, hop_s, samplerate)
pitch_o.set_unit("midi")
pitch_o.set_tolerance(tolerance)

pitches = []
confidences = []

total_frames = 0
while True:
    samples, read = s()
    pitch = pitch_o(samples)[0]
    pitches += [pitch]
    confidence = pitch_o.get_confidence()
    confidences += [confidence]
    total_frames += read
    if read < hop_s:
        break

k_pitches = np.array(pitches) / 1000.0


def FeatureSpectralFlatness(X, f_s):
    norm = X.mean(axis=0, keepdims=True)
    norm[norm == 0] = 1
    vtf = np.exp(X.mean(axis=0, keepdims=True)) / norm
    return np.squeeze(vtf, axis=0)


def spectral_centroid(x, samplerate):
    magnitudes = np.abs(np.fft.rfft(x))
    length = len(x)
    freqs = np.abs(np.fft.fftfreq(length, 1.0 / samplerate)[: length // 2 + 1])
    magnitudes = magnitudes[: length // 2 + 1]
    return np.sum(magnitudes * freqs) / np.sum(magnitudes)


import csv
import scipy
from scipy import stats
import urllib.parse

urllib.parse.quote("châteu", safe="")
import parselmouth

snd = parselmouth.Sound(split_filename)
pitch = snd.to_pitch()


def get_pitch(pitch):
    pitch_values = pitch.selected_array["frequency"]
    pitch_values[pitch_values == 0] = np.nan
    pitch_values_l = list(pitch_values)
    pitch_values_np = np.asarray(pitch_values_l)
    return pitch_values_np


f0_prev = get_pitch(pitch)
f0 = np.array([value for value in f0_prev if not math.isnan(value)])

with open("video.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter=",")
    # writer.writerow(["Name", "Mean" ,"SD", "Median", "Q25", "Q75",'skew','kurt','entropy','Flatness','mode','centroid','Flatness','Mode', 'f0.mean', 'f0.min','f0.max'])
    writer.writerow(
        [
            str(filename),
            k_pitches.mean(),
            k_pitches.std(),
            np.quantile(k_pitches, 0.5),
            np.quantile(k_pitches, 0.25),
            np.quantile(k_pitches, 0.75),
            np.quantile(k_pitches, 0.75) - np.quantile(k_pitches, 0.25),
            scipy.stats.skew(k_pitches, axis=0, bias=True),
            scipy.stats.kurtosis(
                k_pitches, axis=0, fisher=True, bias=True, nan_policy="propagate"
            ),
            FeatureSpectralFlatness(k_pitches, samplerate),
            float(scipy.stats.mode(k_pitches)[0]),
            f0.mean(),
            f0.min(),
            f0.max(),
            0,
        ]
    )

# # load the model from disk
import joblib

# with open('video.csv', 'r') as file :
#     line = list(csv.reader(file , delimiter = ','))
#     line1 = [float(x) for x in line[0][1:]]
import pandas as pd

classifer = joblib.load("/home/cristina/Desktop/hack/model.pickle")
pr = pd.read_csv("video.csv")
pred_cols = list(pr.columns.values)[1:]
pred_cols1 = [float(x) for x in pred_cols]
pred = classifer.predict([pred_cols1])
print(pred)