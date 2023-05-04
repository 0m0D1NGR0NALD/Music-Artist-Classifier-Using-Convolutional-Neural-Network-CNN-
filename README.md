# Music Artist Classifier Using Convolutional Neural Network(CNN)
This project aims to classify music tracks based on the artist that created them, using Convolutional Neural Networks (CNNs).
CNNs are a type of deep neural network that are commonly used for image classification tasks, but can also be applied to other types of data, including audio.
## Installation
To use this project, you will need to have Python 3.6 or higher installed on your machine, along with the following libraries:
* NumPy
* Librosa
* Matplotlib
* Keras
* Pydub
## Usage
To use this project, you will need to follow these steps:
1. Download the dataset (send email to : ronaldomoding130@gmail.com for information)
2. Extract features and train the model using : features.py
3. Visualize training curves using : visualize_training_curves.py
4. Evaluate and carry out inference using : model_evaluation.py and inference.py
## Preprocessing
The preprocessing steps were applied to the dataset as follows :
1. Load the audio files using the Librosa library.
2. Convert the audio files to the Mel-frequency cepstral coefficients (MFCCs) representation
## Feature Extraction
* Mel Frequency Cepstrl Coefficients (MFCC)
![download](https://user-images.githubusercontent.com/97228745/236163103-6dc2deeb-5d46-4bae-aad1-57441b6d69e4.png)
* Mel Spectrogram
![download](https://user-images.githubusercontent.com/97228745/236163337-44bfdcad-f5b6-403a-be45-ee9500af06d8.png)
* Chroma Vector
![download](https://user-images.githubusercontent.com/97228745/236163656-4d7d2328-18cd-4063-8bf1-df016716a680.png)
## About Inference data
The uploaded samples include songs like :
* Badilisha.mp3 by Chameleon
* Lowooza Kunze.mp3 by Rema
* Sanyu Lyange.mp3 by Juliana
* Sitya Loss.mp3 by Kenzo
