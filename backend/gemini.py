import google.generativeai as genai

genai.configure(api_key="AIzaSyBgbFnShSt7cXlktanTGgNTUFkx7bOUr50")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[   
    {
    "role": "user",
    "parts": ["Assume you are a dietician. You will be given a person's Blood Sugar, BP, Pulse Rate. Form a comprehensive diet plan for the person for an average Indian."]
  },
  {
    "role": "model",
    "parts": ["Sure thing! What are the details?"]
  },
])

convo.send_message("Blood Sugar: 250mg, BP: 140/90, Pulse Rate: 80")
print(convo.last.text)