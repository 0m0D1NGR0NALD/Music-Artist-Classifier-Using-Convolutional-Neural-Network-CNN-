import numpy
from pydub import AudioSegment
import IPython.display as ipd
from features import model
from features_extractor import get_feature

# Crop wavefile to a 30 secods section and save the resulting file
t1 = 30000 # In milliseconds
t2 = 60000
