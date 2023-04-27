import pandas as pd
import matplotlib.pyplot as plt
from features import model

# Storing model history of performance within variable 'metrics'
metrics = pd.DataFrame(model.history.history)
