from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSolucionarProblema(Action):
    def name(self) -> Text:
        return "action_solucionar_problema"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        problema = tracker.get_slot("problema")
        
        
        resposta = self.resolver_problema(problema)

        
        dispatcher.utter_message(text=resposta)

        return []

    def resolver_problema(self, problema: Text) -> Text:
        
        problemas_comuns = {

            "erro ao procurar música": "Reinicie o aplicativo e verificar se sua conexão com a internet.",
            "erro no plano": "Verifique se você está logado corretamente na sua conta e se o pagamento do seu plano foi feito.",
            "não consigo acessar a conta": "Recarregue a página e limpe o cache.",
            "problema com assinatura": "Verifique se o seu plano de assinatura foi renovado.",
            "erro ao carregar a página": "Recarregue a página e limpe o cache."

        }

        
        return problemas_comuns.get(problema.lower(), "Não consegui encontrar uma solução para o seu problema, vou encaminhá-lo para um atendente.")

