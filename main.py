from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional
import joblib

app = FastAPI()

class Energy_inputs(BaseModel):

    relative_compactness: float
    surface_area: float
    well_area: float
    roof_area: float
    overall_height: float
    orientation: float
    glazing_area: float
    glazing_area_distribution: float


@app.get('/')
def home():
    return{'Energy':'Efficiency'}


@app.post('/predict')
def predict_load(input: Energy_inputs):

    data = input.dict()
    data_input = [data['relative_compactness'],
                data['surface_area'],
                data['well_area'],
                data['roof_area'],
                data['overall_height'],
                data['orientation'],
                data['glazing_area'],
                data['glazing_area_distribution']
                ]

    filepath = 'energy-efficiency-prediction-v-70\energy_efficiency_prediction'
    loaded_model = joblib.load('energy_efficiency_prediction.joblib')
    prediction = loaded_model.predict(data_input)
    return{
        'prediction':prediction[0],
        'accuracy': prediction[1]
            }