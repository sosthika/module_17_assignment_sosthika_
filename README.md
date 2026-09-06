# Heart Disease Prediction API

## Objective

This project builds a machine learning API using FastAPI to predict the presence of heart disease.

## Technologies

* Python
* FastAPI
* Scikit-learn
* Pandas
* Joblib
* Docker
* Docker Compose
* Render

## Machine Learning Model

A Random Forest Classifier is trained using the Heart Disease Dataset.

The trained model is saved as:

`model/heart_model.joblib`

## API Endpoints

### GET /health

Checks whether the API is running.

Example response:

```json
{
  "status": "healthy"
}
```

### GET /info

Returns information about the model and input features.

### POST /predict

Returns whether heart disease is predicted.

Example input:

```json
{
  "age": 52,
  "sex": 1,
  "cp": 0,
  "trestbps": 130,
  "chol": 250,
  "fbs": 0,
  "restecg": 1,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 1.0,
  "slope": 1,
  "ca": 0,
  "thal": 2
}
```

Example response:

```json
{
  "heart_disease": true
}
```

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Train the model:

```bash
python train_model.py
```

Run FastAPI:

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://localhost:8000/docs
```

## Run with Docker

Build:

```bash
docker compose build
```

Run:

```bash
docker compose up
```

Open:

```text
http://localhost:8000/docs
```

## Deployment

The application is deployed using Docker on Render.

Live API:

`YOUR_RENDER_URL`

Swagger:

`YOUR_RENDER_URL/docs`

## Project Structure

```text
heart-disease-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── schemas.py
├── model/
│   └── heart_model.joblib
├── heart.csv
├── train_model.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```
