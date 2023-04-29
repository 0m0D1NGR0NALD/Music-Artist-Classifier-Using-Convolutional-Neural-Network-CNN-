import numpy
from pydub import AudioSegment
import IPython.display as ipd
from features import model
from features_extractor import get_feature

# Path to inference data samples
chameleon = 'Badilisha.mp3'
rema = 'Lowooza Kunze.mp3'

# Crop wavefile to a 30 secods section and save the resulting file
t1 = 30000 # In milliseconds
t2 = 60000
