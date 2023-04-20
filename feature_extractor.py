import numpy
from feature_extraction import get_mfcc,get_melspectrogram,get_chroma_vector,get_tonnetz

# Putting the features together
def get_feature(file_path):
  # Extracting MFCC feature
  mfcc = get_mfcc(file_path)
