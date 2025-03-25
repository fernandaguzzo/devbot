import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionInformaClima(Action):
    def name(self) -> Text:
        return "action_informa_clima"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.latest_message['text']

        weather_data = self.get_weather(city)

        print(f"City: {city}")
        print(f"Weather Data: {weather_data}")

        if weather_data:
            response = f"O clima na cidade de {city} está em: {weather_data['current']['temp_c']}°C."
        else:
            response = f"Desculpe, mas não consegui obter a situação do clima da cidade de {city}."

        dispatcher.utter_message(text=response)
        return []

    @staticmethod
    def get_weather(city: str) -> Dict[Text, Any]:
        base_url = "http://api.weatherapi.com/v1/current.json"
        api_key = "SUA_CHAVE_AQUI"
        params = {"key": api_key, "q": city, "aqi": "no"}

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API Request Error: {e}")
            return None
