#test_FM.py

'''
    author: em
    project: group 7
    class: CS-534 Artificial Intelligence WPI
    date: July 23, 2023

    test implementation of KM model

'''
from KM.KM import *
import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler

filename = "Data/datasets/CIDDS/training/CIDDS_Internal_train.csv"
TRAIN_FULL = False

def main():
    k = 5           #num clusters

    df = pd.read_csv(filename)
    df 

    km_model = KM(k, "testKM")
    print(km_model.get_model_name())

    X, y = km_model.prepare_data(df)

    #full train set
    if (TRAIN_FULL):
        X_train, X_test, y_train,  y_test = train_test_split(X, y, test_size=.33)
    else:
        #train /test a subset
        X_train = X.iloc[:20000]
        y_train = y.iloc[:20000]
        X_test = X.iloc[20000:30000]
        y_test = y.iloc[20000:30000]

    scaler = RobustScaler()
    scaler.fit_transform(X_train)
    scaler.transform(X_test)
    
    print("training...")
    
    start = time.time()
    trained = km_model.train_model(X_train, y_train)
    train_time = time.time() - start
    print("done training clusters! training time: " + str(train_time))

    print("testing...")
    start = time.time()
    predict = km_model.test_model(X_test)
    test_time = time.time() - start
    print("done testing! testing time: " + str(test_time))

    print("training scores")
    km_model.evaluate(X_train, y_train, trained.labels_)

    print()

    #print("testing scores")
    km_model.evaluate(X_test, y_test, predict)

    #print("training clustering visualized")
    km_model.render_model(predict, X_test, y_test)

if __name__ == "__main__":
    main()