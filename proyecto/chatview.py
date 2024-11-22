import os
from miproyecto.settings import BASE_DIR  # Si chatview.py está en una carpeta dentro de 'backend'
import dialogflow_v2 as dialogflow
import uuid
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def chatbot_response(request):
    # Obtener la pregunta del usuario
    question = request.data.get('question')
    
    # Obtener o generar un session_id
    session_id = request.data.get('sessionId', str(uuid.uuid4()))  # Generar una sesión si no se envía
    
    # Llamar a Dialogflow
    response_text = get_dialogflow_response(question, session_id)
    
    # Devolver la respuesta al frontend
    return Response({"response": response_text, "sessionId": session_id})

def get_dialogflow_response(text, session_id):
    try:
        # Configuración de Dialogflow para la versión 1.1.1
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(BASE_DIR, 'miproyecto', 'dialogflow_credentials', 'newagent-bwow-0a22843302cb.json')

        # Inicializar cliente
        dialogflow_client = dialogflow.SessionsClient()
        session = dialogflow_client.session_path("newagent-bwow", session_id)

        # Crear consulta de texto
        text_input = dialogflow.types.TextInput(text=text, language_code='es')
        query_input = dialogflow.types.QueryInput(text=text_input)

        # Obtener respuesta de Dialogflow
        response = dialogflow_client.detect_intent(session=session, query_input=query_input)

        return response.query_result.fulfillment_text

    except Exception as e:
        return f"Error en Dialogflow: {str(e)}"
