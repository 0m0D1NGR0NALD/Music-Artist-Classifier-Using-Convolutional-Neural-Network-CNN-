import librosa
import numpy

# Mel Frequency Cepstrl Coefficients (MFCC)
def get_mfcc(wav_file_path):
  y, sr = librosa.load(wav_file_path, offset=0, duration=30)
