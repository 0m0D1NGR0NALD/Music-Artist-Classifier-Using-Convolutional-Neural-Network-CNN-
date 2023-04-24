import os
import numpy
from features_extractor import get_feature

# Calculating features for the dataset
directory = 'path to dataset' # Dataset contains a folder for each class: 'chameleon','juliana','kenzo','rema'
artists = ['chameleon','juliana','kenzo','rema']
features = []
labels = []

for artist in artists:
  print("Calculating features for artist : " + artist)
  for file in os.listdir(directory+"/"+artist):
    file_path = directory+"/"+artist+"/"+file
