from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import xgboost as xgb
import pandas as pd
import pickle

if __name__ == "__main__":

    # Reading Data
    data = pd.read_csv("dataset.csv")

    # Creating data and target variables 
    X = data.drop(columns='infectionProb')
    y = data['infectionProb']

    # Train Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.3)

    # Initializing Model
    # clf = xgb.XGBClassifier()
    clf = LogisticRegression()

    # Fitting Data to out Model
    clf.fit(X_train.values, y_train.values)

    # Its important to use binary mode 
    file = open('model.pkl', 'ab') 
      
    # source, destination 
    pickle.dump(clf, file)                      
    file.close() 

    # Predicting new Values 
    # y_pred = clf.predict(X_test)

