from fastapi import HTTPException, APIRouter
import google.generativeai as genai
import json

inference_router = APIRouter()

with open("secrets.json") as secrets_file:
    secrets = json.load(secrets_file)

gemini_api = secrets["GEMINI-API"]

genai.configure(api_key=gemini_api)

generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
    safety_settings=safety_settings,
)


@inference_router.get("/test/")
async def test():
    return {"message": "Test GET call From Inference APIs"}


@inference_router.post("/dietPlan/")
async def dietPlan(json_data: dict):

    pulserate = json_data.get("pulserate", "NOT AVAILABLE")
    syspressure = json_data.get("syspressure", "NOT AVAILABLE")
    diapressure = json_data.get("diapressure", "NOT AVAILABLE")
    bloodsugar = json_data.get("bloodsugar", "NOT AVAILABLE")

    message = f"""Blood Sugar: {bloodsugar} mg/dL, Blood Pressure {syspressure}/{diapressure},
      Pulse Rate {pulserate} beats per minute."""

    convo = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    """As a dietitian, you will be provided with information on Blood Sugar, Blood Pressure, Pulse Rate, Step Count, and Sleep. 

                    Provide a brief report on any irregularities or the status of each vital. 
                    Format the report as 1-2 lines, including irregularities if any, or else just description.
                    (If irregularities, mention if immediate care is needed or if prevention is fine.)
                    If any data is NOT AVAILABLE, ignore it and provide feedback on the rest.

                    And then, please suggest a comprehensive diet plan for the day, including Breakfast, Lunch, Dinner, and Snacks.
                    End the report with the diet plan for the day and some additional tips."""
                ],
            },
            {
                "role": "model",
                "parts": [
                    "Okay, provide me with the vitals information. I will provide in the format required as to my best knowledge."
                ],
            },
        ]
    )

    convo.send_message(message)

    return {"message": convo.last.text}


@inference_router.post("/exercisePlan/")
async def exercisePlan(json_data: dict):

    stepcount = json_data.get("stepcount", "NOT AVAILABLE")
    sleep = json_data.get("sleep", "NOT AVAILABLE")
    pulserate = json_data.get("pulserate", "NOT AVAILABLE")
    syspressure = json_data.get("syspressure", "NOT AVAILABLE")
    diapressure = json_data.get("diapressure", "NOT AVAILABLE")
    bloodsugar = json_data.get("bloodsugar", "NOT AVAILABLE")

    message = f"""Blood Sugar: {bloodsugar} mg/dL, Blood Pressure {syspressure}/{diapressure}, Pulse Rate {pulserate} beats per minute.
    Step Count: {stepcount} steps, Sleep: {sleep} hours. This is for the chronicaly sick, mention very light exercises that even old people can do."""

    convo = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    """As a fitness trainer, you will be provided with information on Blood Sugar, Blood Pressure, Pulse Rate, Step Count, and Sleep. 

                    Provide a brief report on the status of step count and sleep.
                    Format the report as 1-2 lines, including irregularities if any, or else just description.
                    If any data is NOT AVAILABLE, ignore it and provide feedback on the rest.

                    And then, please suggest a comprehensive exercise plan for the day, including Warm-up, Cardio, Strength, and Cool-down.
                    End the report with the exercise plan for the day and some additional tips."""
                ],
            },
            {
                "role": "model",
                "parts": [
                    "Okay, provide me with the vitals information. I will provide in the format required as to my best knowledge."
                ],
            },
        ]
    )

    convo.send_message(message)

    return {"message": convo.last.text}


@inference_router.post("/EODReport/")
async def EODReport(json_data: dict):

    pulserate = json_data.get("pulserate", "NOT AVAILABLE")
    syspressure = json_data.get("syspressure", "NOT AVAILABLE")
    diapressure = json_data.get("diapressure", "NOT AVAILABLE")
    bloodsugar = json_data.get("bloodsugar", "NOT AVAILABLE")
    stepcount = json_data.get("stepcount", "NOT AVAILABLE")
    sleep = json_data.get("sleep", "NOT AVAILABLE")

    message = f"""Blood Sugar: {bloodsugar} mg/dL, Blood Pressure {syspressure}/{diapressure}, Pulse Rate {pulserate} beats per minute.
    Step Count: {stepcount} steps, Sleep: {sleep} hours."""

    convo = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    """As a EVALUATOR, you will be provided with information on Blood Sugar, Blood Pressure, Pulse Rate, Step Count, and Sleep. 

                    Provide a brief report on the status of each vital.
                    Format the report as 2-3 lines for each category (Blood Sugar, Blood Pressure, Pulse Rate, Step Count and Sleep),
                    including irregularities if any, or else just description. Also provide beneficiary tips that may improve the 
                    state of the vital. If any data is NOT AVAILABLE, ignore it."""
                ],
            },
            {
                "role": "model",
                "parts": [
                    "Okay, provide me with the vitals information. I will provide in the format required as to my best knowledge."
                ],
            },
        ]
    )

    convo.send_message(message)

    return {"message": convo.last.text}
