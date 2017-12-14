from __future__ import print_function
import vamp
import librosa

audio_file = 'music/train01.wav'
audio, sr = librosa.load(audio_file, sr=44100, mono=True)
data = vamp.collect(audio, sr, "mtg-melodia:melodia")