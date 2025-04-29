import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionBuscarPorTitulo(Action):
    def name(self) -> Text:
        return "action_buscar_por_titulo"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict]:
        titulo = next(tracker.get_latest_entity_values("titulo"), None)
        if not titulo:
            dispatcher.utter_message(text="Qual é o título do livro que você procura?")
            return []
        
        url = f"https://openlibrary.org/search.json?title={titulo}"
        response = requests.get(url)
        data = response.json()

        if data.get("numFound", 0) > 0:
            livros = data.get("docs", [])[:3]
            mensagens = [f"- {livro.get('title', 'Título desconhecido')} por {', '.join(livro.get('author_name', []))}" for livro in livros]
            dispatcher.utter_message(text="Aqui estão alguns resultados:\n" + "\n".join(mensagens))
        else:
            dispatcher.utter_message(text="Desculpe, não encontramos nenhum resultado para o título informado.")
        
        return []

class ActionBuscarPorAutor(Action):
    def name(self) -> Text:
        return "action_buscar_por_autor"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict]:
        autor = next(tracker.get_latest_entity_values("autor"), None)
        if not autor:
            dispatcher.utter_message(text="Qual autor você quer buscar?")
            return []
    
        url = f"https://openlibrary.org/search.json?author={autor}"
        response = requests.get(url)
        data = response.json()

        if data.get("numFound", 0) > 0:
            livros = data.get("docs", [])[:3]
            mensagens = [f" - {livro.get('title', 'Título desconhecido')} ({livro.get('first_publish_year', 'Ano desconhecido')})" for livro in livros]
            dispatcher.utter_message(text="Aqui estão alguns livros do autor:\n" + "\n".join(mensagens))
        else:
            dispatcher.utter_message(text="Desculpe, não encontramos nenhum livro para o autor informado.")
        
        return []

class ActionBuscarPorAssunto(Action):
    def name(self) -> Text:
        return "action_buscar_por_assunto"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict]:
        assunto = next(tracker.get_latest_entity_values("assunto"), None)
        if not assunto:
            dispatcher.utter_message(text="Sobre qual assunto você gostaria de buscar livros?")
            return []
        
        url = f"https://openlibrary.org/search.json?subject={assunto}"
        response = requests.get(url)
        data = response.json()

        if data.get("numFound", 0) > 0:
            livros = data.get("docs", [])[:3]
            mensagens = [f" - {livro.get('title', 'Título desconhecido')} por {', '.join(livro.get('author_name', []))} ({livro.get('first_publish_year', 'Ano desconhecido')})" for livro in livros]
            dispatcher.utter_message(text="Aqui estão alguns livros sobre o assunto:\n" + "\n".join(mensagens))
        else:
            dispatcher.utter_message(text="Desculpe, não encontramos nenhum livro sobre o assunto informado.")
        
        return []
