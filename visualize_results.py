import pandas as pd
import matplotlib.pyplot as plt
from features import model

# Storing model history of performance within variable 'metrics'
metrics = pd.DataFrame(model.history.history)

# Plot of train set loss and validation set loss
metrics[['loss','val_loss']].plot()

# Labelling Graph
plt.grid()
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epochs')
plt.legend(['train','validation'])
plt.show()

# Plot of train set accuracy and validation set accuracy
metrics[['sparse_categorical_accuracy','val_sparse_categorical_accuracy']
# Labelling Graph
plt.grid()
