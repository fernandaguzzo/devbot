from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionRecomendarFilme(Action):
    def name(self) -> Text:
        return "action_recomendar_filme"
    def run (self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
             
             genero = tracker.get_slot("genero")
             filmes = self.obter_recomendacoes(genero)

             if filmes:
                   dispatcher.utter_message(text=f"Para o gênero {genero}, recomendo: {', '.join(filmes)}")
             else:
                   dispatcher.utter_message(text="Desculpe, não encontrei recomendações para esse gênero.")

             return []
    
    def obter_recomendacoes(self, genero: Text) -> List[Text]:
          filmes_por_genero = {
                "comedia": ["Se Beber, Não Case!", "Minha Mãe é Uma Peça", "Deadpool"],
                "ação": ["Mad Max: Estrada da Fúria", "John Wick", "Missão Impossível: Efeito Fallout"],
                "drama": ["Um Sonho de Liberdade", "O Poderoso Chefão", "A Lista de Schindler"],
                "suspense": ["Psicose", "O Silêncio dos Inocenter", "Seven - Os Sete Crimes Capitais"],
                "terror": ["O Iluminado", "Invocação do Mal", "Hereditário"],
                "romance": ["Um Lugar Chamado Notting Hill", "Orgulho e Preconceito", "A Culpa é das Estrelas"],
                "ficção científica": ["Interestelar", "Blade Runner 2049", "A Chegada"],
                "documentário": ["A 13ª Emenda", "Planeta Terra", "Free Solo"],
                "animação": ["Toy Story", "Soul", "Your Name."],
                "faroeste": ["Era Uma Vez no Oeste", "Os Imperdoáveis", "Bravura Indômita"]
          }
          
          return filmes_por_genero.get(genero.lower(), [])
