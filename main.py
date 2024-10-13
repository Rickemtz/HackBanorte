from fastapi import FastAPI
from vertexai.generative_models import (
    GenerationConfig,
    GenerativeModel,
    HarmBlockThreshold,
    HarmCategory,
)
import vertexai
from google.cloud import bigquery
from google.cloud import pubsub_v1
import requests

app = FastAPI()

# Configuración de Vertex AI
PROJECT_ID = "glass-potion-437915-b1"
LOCATION = "us-central1"
MODEL_ID = "gemini-1.5-flash-002"
vertexai.init(project=PROJECT_ID, location=LOCATION)

# Configuración de seguridad
safety_settings = {
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
}

# Base de datos de BigQuery
bq_client = bigquery.Client()

@app.get("/")
async def hello_world():
    model = GenerativeModel(
        MODEL_ID,
        system_instruction=[
            """Eres un asistente personalizado del banco Banorte... (Instrucciones completas aquí)"""
        ]
    )

    generation_config = GenerationConfig(
        temperature=1.5,
        top_p=0.95,
        top_k=32,
        candidate_count=1,
        max_output_tokens=8192,
    )

    prompt = "entrada: Ayudame con mi cuenta de bbva porfavor \nrespuesta: "
    contents = [prompt]

    response = model.generate_content(
        contents,
        generation_config=generation_config    
    )

    return response.text

@app.post("/simulate")
async def simulate_financial_decision(decision: str, user_data: dict):
    # Aquí puedes procesar la decisión del usuario y sus datos
    # Realiza cálculos de simulación basados en los datos proporcionados
    simulation_result = {
        "impact": "Ejemplo de impacto proyectado",
        "details": "Detalles de la simulación"
    }
    return simulation_result

@app.get("/update-data")
async def update_financial_data():
    # Usa Pub/Sub para obtener datos actualizados
    publisher = pubsub_v1.PublisherClient()
    topic_name = f"projects/{PROJECT_ID}/topics/your-topic-name"
    data = b"Actualización de datos financieros"
    future = publisher.publish(topic_name, data)
    return {"message": "Datos actualizados", "future": str(future.result())}

@app.get("/get-interest-rates")
async def get_interest_rates():
    # Llama a una API para obtener tasas de interés
    response = requests.get("URL_DE_LA_API_DE_TASAS_DE_INTERES")
    return response.json()
