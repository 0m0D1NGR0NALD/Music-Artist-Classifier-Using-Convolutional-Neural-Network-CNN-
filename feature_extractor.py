import numpy
from feature_extraction import get_mfcc,get_melspectrogram,get_chroma_vector,get_tonnetz

# Putting the features together
def get_feature(file_path):
  # Extracting MFCC feature
  mfcc = get_mfcc(file_path)
  mfcc_mean = mfcc.mean(axis=1)
  mfcc_min = mfcc.min(axis=1)
  mfcc_max = mfcc.max(axis=1)
