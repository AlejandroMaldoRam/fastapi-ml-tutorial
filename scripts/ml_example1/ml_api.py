# API for using our ML model with FastAPI
import joblib
import pandas as pd
from TitanicPassenger import TitanicPassenger
from fastapi import FastAPI

# Initialize FastAPI class.
app = FastAPI()

# Load model
model = joblib.load('model1.joblib')
model_columns = joblib.load("model_columns.joblib")

# Operations
@app.get("/")
async def index():
    return {"message": "Titanic survival prediction"}

@app.post("/predict")
async def predict(data: TitanicPassenger):
    data_dict = data.model_dump()
    print("Raw data:", data_dict)
    query_df = pd.DataFrame(data=[data_dict])
    print("df:\n", query_df)
    query = pd.get_dummies(query_df)
    print("query df:\n", query)
    query = query.reindex(columns=model_columns, fill_value=0)
    print("query df:\n", query)

    prediction = list(model.predict(query))
    print("prediction: ", prediction)
    #return jsonify({'prediction': str(prediction)})
    return {"prediction": str(prediction[0])}

@app.route("/predict", methods=['GET'])
def predict_help():
    return "Por favor usa tipo de mensaje POST..."
