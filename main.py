from fastapi import FastAPI,status
from fastapi.responses import  JSONResponse
from Schemas.flower import Iris as IrisSchema
import pickle

# Cargamos el modelo en la variable ModPredDTC
ModPredDTC = pickle.load(open("RegressionModels/SVCModel.pkl","rb"))


# Instanciamos la clase FastAPI() para crear la aplicación con la variable app
app = FastAPI()

# Creamos el primer endpoint
@app.get("/",status_code=status.HTTP_200_OK)
async def root():
    return {"message": "Hello world"}

# El segundo endpoint que recibe como variable una data de tipo IrisSchema
@app.post("/predict", status_code=status.HTTP_200_OK)
async def predict_flower(data: IrisSchema):
    """ Esta función predice el tipo de flor
    Setosa, Versicolor o Virginica"""
 
    prediction = ModPredDTC.predict([[data.sepalLength,data.sepalWidth,data.petalLength,data.petalWidth]])
    flower = ""
    
    if prediction[0] == 0:
        flower = "Setosa"
    elif prediction[0] == 1:
        flower = "Versicolor"
    else:
        flower = "Virginica"
    
    return JSONResponse(content={"message": "Esta flor es: " + flower})

