import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 
from sklearn import linear_model 
from sklearn import tree 
from sklearn import ensemble
from sklearn.metrics import accuracy_score
import time
import pickle

# STATIC 
SEED = 42
DATA_DIR = "dataset/iris.csv"
## Fungsi Standardisasi

if __name__ == "__main__":
    # DATA LOADING
    df = pd.read_csv(DATA_DIR)

    # DATA PREPROCESSING
    ## Feature Selection
    df.drop(['Id'], axis=1, inplace=True)
    # TRAIN TEST SPLITTING
    train, test = train_test_split(df, test_size=0.1, random_state=SEED)
    X_train = train.drop(['Species'], axis=1)
    y_train = train['Species']
    X_test = test.drop(['Species'], axis=1)
    y_test = test['Species']
    ## Standardisasi 
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    # MODELLING AND EVALUATION
    models = {
        'logistic_regression': linear_model.LogisticRegression(),
        'decision_tree': tree.DecisionTreeClassifier(criterion='gini'),
        'random_forest': ensemble.RandomForestClassifier(n_estimators=100, random_state=SEED)
    }
    for model_name, model in models.items():
        ## TRAINING
        start = time.perf_counter()
        model_ = model.fit(X_train, y_train)
        end = time.perf_counter()

        ## EVALUATIONS
        y_train_pred = model_.predict(X_train)
        # Prediksi untuk unseen data
        y_test_pred = model_.predict(X_test)
        scores_train = accuracy_score(y_train, y_train_pred)
        scores_test = accuracy_score(y_test, y_test_pred)
        print(f"""{model_name}'s Performance in Accuracy
            Training : {scores_train}
            Testing : {scores_test}
            Training Times : {(end-start):.3f} seconds
        """)
        ## SAVE BEST MODEL
        if model_name == "decision_tree":
            with open('best_model.pkl', 'wb') as f:
                pickle.dump(model_, f)
