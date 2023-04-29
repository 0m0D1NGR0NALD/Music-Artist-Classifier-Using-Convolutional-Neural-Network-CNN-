import numpy
from pydub import AudioSegment
import IPython.display as ipd
from features import model
from features_extractor import get_feature

artists = ['chameleon','juliana','kenzo','rema']

# Path to inference data samples
chameleon = 'Badilisha.mp3'
rema = 'Lowooza Kunze.mp3'
juliana = 'Sanyu Lyange.mp3'
kenzo = 'Sitya Loss.mp3'

# Selecting sample
song = chameleon

# Crop wavefile to a 30 secods section and save the resulting file
t1 = 30000 # In milliseconds
t2 = 60000

waveFile = AudioSegment.from_file(song)
waveFile = waveFile[t1:t2]
waveFile.export('audio_sample.wav', format="wav")

# Play the audio file
ipd.Audio('audio_sample.wav', autoplay=True)

# Use trained model to classify the audio file
file_path = "audio_sample.wav"
feature = get_feature(file_path)
prob = model.predict(feature.reshape(1,498))
pred = numpy.argmax(prob)

# Print predicted artist's name
print(artists[pred])
