import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
df=sns.load_dataset("mpg")
df.isnull().sum()