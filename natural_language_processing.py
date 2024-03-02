# importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importing the dataset
# format to read the tsv and train the machine to not take into account the quotations marks
dataset = pd.read_csv("Restaurant_Reviews.tsv", delimiter='\t', quoting=3)

# cleaning the text
import re
import nltk
# download all the stopwords
nltk.download('stopwords')
# importing the stopwords
from nltk.corpus import stopwords
# class to apply stemming to the reviews
from nltk.stem.porter import PorterStemmer
# list to get in the end all the clean reviews
corpus = []
num_of_reviews = len(dataset)
for i in range(0, num_of_reviews):
    # replace any punctuation by a space
    # '^' to specify that we want to replace anything but a-zA-Z
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    # include also the 'not'
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    # applying stemming to each of the word inside the review
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
    # join the words and separate them using space
    review = ' '.join(review)
    # add the review in the corpus
    corpus.append(review)

# creating the bag of words model
from sklearn.feature_extraction.text import CountVectorizer
# getting the 1500 most used words
cv = CountVectorizer(max_features=1500)
#  fit method will take all the words and transform method will put all these words into columns
X = cv.fit_transform(corpus).toarray()
# dependent variable vector
y = dataset.iloc[:, -1].values
# print(len(X[0]))

# splitting the dataset into the training set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=0)

# training the naive bayes model in the training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# predicting the test results
y_pred = classifier.predict(X_test)
# first column the prediction and 2nd column the real data
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))

# making the confusion matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(accuracy_score(y_test, y_pred))



