import glob

import shutil

from sklearn.model_selection import train_test_split

dataset_path = 'C:\\Datasets\\ganyu\\'

all_anime = glob.glob(dataset_path + '*.jpg')

X_train, X_test = train_test_split(all_anime, test_size=0.2, random_state=42, shuffle=True)
X_val, X_test = train_test_split(X_test, test_size=0.5, random_state=42)
print(len(X_train),len(X_test),len(X_val))

for filename in X_train:
    shutil.copy(filename, 'C:\\Real-ESRGAN-anime\\datasets\\anime\\train\\')

for filename in X_test:
    shutil.copy(filename, 'C:\\Real-ESRGAN-anime\\datasets\\anime\\test\\')

for filename in X_val:
    shutil.copy(filename, 'C:\\Real-ESRGAN-anime\\datasets\\anime\\val\\')
