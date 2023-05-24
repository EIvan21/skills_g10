from fastapi import FastAPI,status, UploadFile, File
from PIL import Image
from fastapi.responses import  JSONResponse
from Schemas.flower import Iris as IrisSchema
import pickle
import numpy as np


# Cargamos el modelo en la variable ModPredDTC





# Instanciamos la clase FastAPI() para crear la aplicación con la variable app
app = FastAPI()

# Creamos el primer endpoint
@app.get("/",status_code=status.HTTP_200_OK)
async def root():
    return {"message": "Hello world"}

# El segundo endpoint que recibe como variable una data de tipo IrisSchema
@app.post("/predict/SVC", status_code=status.HTTP_200_OK , tags={"Predictions"})
async def predict_flower_SVC(data: IrisSchema):
    """ Esta función predice el tipo de flor
    Setosa, Versicolor o Virginica"""
    ModPredDTC = pickle.load(open("RegressionModels/SVCModel.pkl","rb"))
    prediction = ModPredDTC.predict([[data.sepalLength,data.sepalWidth,data.petalLength,data.petalWidth]])
    flower = ""
    
    if prediction[0] == 0:
        flower = "Setosa"
    elif prediction[0] == 1:
        flower = "Versicolor"
    else:
        flower = "Virginica"
    
    return JSONResponse(content={"message": "Esta flor es: " + flower})

# El tercer endpoint que recibe como variable una data de tipo IrisSchema
@app.post("/predict/Tree", status_code=status.HTTP_200_OK , tags={"Predictions"})
async def predict_flower_Tree(data: IrisSchema):
    """ Esta función predice el tipo de flor
    Setosa, Versicolor o Virginica"""
    ModPredTree = pickle.load(open("RegressionModels/TreeModel.pkl","rb"))
    prediction = ModPredTree.predict([[data.sepalLength,data.sepalWidth,data.petalLength,data.petalWidth]])
    flower = ""
    
    if prediction[0] == 0:
        flower = "Setosa"
    elif prediction[0] == 1:
        flower = "Versicolor"
    else:
        flower = "Virginica"
    
    return JSONResponse(content={"message": "Esta flor es: " + flower})

# El tercer endpoint que recibe como variable una data de tipo IrisSchema
@app.post("/predict/Linear", status_code=status.HTTP_200_OK , tags={"Predictions"})
async def predict_flower_Linear(data: IrisSchema):
    """ Esta función predice el tipo de flor
    Setosa, Versicolor o Virginica"""
 
    ModPredLinear = pickle.load(open("RegressionModels/LinearModel.pkl","rb"))
    prediction = ModPredLinear.predict([[data.sepalLength,data.sepalWidth,data.petalLength,data.petalWidth]])
    flower = ""
    
    if prediction[0] == 0:
        flower = "Setosa"
    elif prediction[0] == 1:
        flower = "Versicolor"
    else:
        flower = "Virginica"
    
    return JSONResponse(content={"message": "Esta flor es: " + flower})


@app.post("/predict-digit/")
async def predict_digit(image: UploadFile = File(...)):
    count = 1
    
    ModClasclf = pickle.load(open("ClassificationModels/ClfModel.pkl","rb"))
    
    img = Image.open(image.file)
    img = img.convert("L").resize((8, 8))
    img.save("Images/img" + str(count) + ".jpg")
    count +=1
    img_array = np.array(img)/8
    img_array = img_array.reshape(1, -1)
    prediction = ModClasclf.predict(img_array)
  

    return {"prediction": int(prediction)}