# Programa para entrenar un modelo con scikit learn
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import joblib

if __name__=='__main__':
    # Cargar datos
    url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
    df_ = pd.read_csv(url)
    features = ['Age', 'Sex', 'Embarked', 'Survived']
    df = df_[features]
    print("Dataset:\n", df)
    print("Desc:\n", df.describe())
    print("Tipos:\n", df.dtypes)

    # Preprocesamiento (Llenar celdas vacías)
    categorical_vars = ['Sex','Embarked']
    numerical_vars = ['Age']
    df_num = df.fillna({'Age':0, 'Embarked':'Q'})
    print("Dataset:\n", df)
    
    # Conversión de variables categoricas a one-hot encoding usando el método get_dummies de pandas
    df_ohe = pd.get_dummies(df_num, columns=categorical_vars, dummy_na=True)

    print("Dataset:\n", df_ohe)
    print("Desc:\n", df_ohe.describe())
    print("Tipos:\n", df_ohe.dtypes)

    # Separamos datos en entrenamiento y prueba
    features = ['Age', 'Sex_female', 'Sex_male', 'Sex_nan', 'Embarked_C', 'Embarked_Q', 'Embarked_S', 'Embarked_nan']
    labels = ['Survived']
    #X = df_ohe[features].to_numpy()
    X = df_ohe[features]
    y = df_ohe[labels].to_numpy().ravel()
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)
    print("Train dataset: \n", X_train)
    print("Test dataset: \n", X_test)

    # Entrenamos
    model = make_pipeline(StandardScaler(), MLPClassifier(hidden_layer_sizes=(50,50), max_iter=500))
    #model = MLPClassifier(hidden_layer_sizes=(50,50))
    model.fit(X_train, y_train)

    # Evaluamos
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    acc_train = accuracy_score(y_train, y_train_pred)
    acc_test = accuracy_score(y_test, y_test_pred)    
    print("Acc. Train: ", acc_train)
    print("Acc. Test: ", acc_test)

    # Guardamos modelo
    joblib.dump(model, 'model1.joblib')
    #model_columns = list(X_train.columns)
    joblib.dump(features, 'model_columns.joblib')
    print("Modelo guardado")

