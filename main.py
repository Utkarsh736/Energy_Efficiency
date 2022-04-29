from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional
import uvicorn
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
def predict_load(predict_data: Energy_inputs):

    data = predict_data.dict()
    data_input = [[data['relative_compactness'],
                data['surface_area'],
                data['well_area'],
                data['roof_area'],
                data['overall_height'],
                data['orientation'],
                data['glazing_area'],
                data['glazing_area_distribution']]
                ]

    filepath = "C:/Users/utkar/Energy_Efficiency/energy_efficiency_prediction.joblib"
    loaded_model = joblib.load('energy_efficiency_prediction.joblib')
    prediction = loaded_model.predict(data_input)
    return{
        'Hot Load':prediction[0][0],
        'Cold Load': prediction[0][1]
            }

if __name__ == '__main__':
    uvicorn.run(app)