# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils
import logging

from ask_sdk_core.skill_builder import SkillBuilder, CustomSkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.api_client import DefaultApiClient
from ask_sdk_model.ui import AskForPermissionsConsentCard
from ask_sdk_model.services import ServiceException
from ask_sdk_model import Response
from league import Lol
from frases import Frases

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Instância objeto Lol -> Responsável pela busca das infos
lol = Lol()

# Instância objeto Frases -> Responsável pelas frases randômicas
frase = Frases()

# Inicio da aplicação
class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        
        attr = handler_input.attributes_manager.session_attributes

        # **** Pega o nome do usuário **** #
        req_envelope = handler_input.request_envelope
        response_builder = handler_input.response_builder
        service_client_fact = handler_input.service_client_factory
        
        nome_usuario = ""
        try:
            nome_usuario = service_client_fact.get_ups_service().get_profile_given_name()
        except Exception as e:
            nome_usuario = "invocador"

        msg1 = frase.saudacao()
        msg2 = frase.inicio()
        
        attr["recent_response"] = msg1 + ". " + msg2
        attr["state"] = ""
                
        return (handler_input.response_builder.speak(msg1 + ". " + msg2).ask(msg2).response)


# Inteção de História dos Campeões
class HistoriaIntentHandler(AbstractRequestHandler):
    """Handler for Historia Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HistoriaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        attr["state"] = "CONTINUAR"
        
        slots = handler_input.request_envelope.request.intent.slots
        campeao = slots['campeao']

        id_camp = campeao.resolutions.resolutions_per_authority[0].values[0].value.id
        nome = campeao.resolutions.resolutions_per_authority[0].values[0].value.name
        msg1 = lol.historia(nome) + ". " + frase.fimMensagemAjuda()
        msg2 = frase.fimMensagemAjuda()

        attr["recent_response"] = msg1

        return (handler_input.response_builder.speak(msg1).ask(msg2).response)

# Inteção de Runa dos Campeões
class RunasIntentHandler(AbstractRequestHandler):
    """Handler for Runas Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RunasIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        attr["state"] = "CONTINUAR"

        slots = handler_input.request_envelope.request.intent.slots
        campeao = slots['campeao']

        id_camp = campeao.resolutions.resolutions_per_authority[0].values[0].value.id
        nome_camp = campeao.resolutions.resolutions_per_authority[0].values[0].value.name
        msg1 = lol.runa(nome_camp) + ". " + frase.fimMensagemAjuda()
        msg2 = frase.fimMensagemAjuda()
        
        attr["recent_response"] = msg1
        
        return (handler_input.response_builder.speak(msg1).ask(msg2).response)

# Inteção de dicas para Campeões
class DicasAliadosIntent(AbstractRequestHandler):
    """Handler for Dicas Aliados Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("DicasAliadosIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        attr["state"] = "CONTINUAR"
        
        slots = handler_input.request_envelope.request.intent.slots
        campeao = slots['campeao']

        id_camp = campeao.resolutions.resolutions_per_authority[0].values[0].value.id
        nome_camp = campeao.resolutions.resolutions_per_authority[0].values[0].value.name
        msg1 = lol.dicasAliados(nome_camp) + ". " + frase.fimMensagemAjuda()
        msg2 = frase.fimMensagemAjuda()
        
        attr["recent_response"] = msg1
        
        return (handler_input.response_builder.speak(msg1).ask(msg2).response)


# Inteção de dicas contra Campeões
class DicasContraIntent(AbstractRequestHandler):
    """Handler for Dicas Contra Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("DicasContraIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        attr["state"] = "CONTINUAR"

        slots = handler_input.request_envelope.request.intent.slots
        campeao = slots['campeao']

        id_camp = campeao.resolutions.resolutions_per_authority[0].values[0].value.id
        nome_camp = campeao.resolutions.resolutions_per_authority[0].values[0].value.name
        msg1 = lol.dicasContra(nome_camp) + ". " + frase.fimMensagemAjuda()
        msg2 = frase.fimMensagemAjuda()
        
        attr["recent_response"] = msg1
        
        return (handler_input.response_builder.speak(msg1).ask(msg2).response)

# Inteção de habilidades dos Campeões
class HabilidadesIntent(AbstractRequestHandler):
    """Handler for Habilidades Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HabilidadesIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        attr["state"] = "CONTINUAR"

        slots = handler_input.request_envelope.request.intent.slots
        campeao = slots['campeao']

        id_camp = campeao.resolutions.resolutions_per_authority[0].values[0].value.id
        nome_camp = campeao.resolutions.resolutions_per_authority[0].values[0].value.name
        msg1 = lol.habilidadesCampeao(nome_camp) + ". " + frase.fimMensagemAjuda()
        msg2 = frase.fimMensagemAjuda()
        
        attr["recent_response"] = msg1
        
        return (handler_input.response_builder.speak(msg1).ask(msg2).response)

# Inteção de passiva dos Campeões
class PassivaIntent(AbstractRequestHandler):
    """Handler for Passiva Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PassivaIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        attr["state"] = "CONTINUAR"
        
        slots = handler_input.request_envelope.request.intent.slots
        campeao = slots['campeao']

        id_camp = campeao.resolutions.resolutions_per_authority[0].values[0].value.id
        nome_camp = campeao.resolutions.resolutions_per_authority[0].values[0].value.name
        msg1 = lol.passivaCampeao(nome_camp) + ". " + frase.fimMensagemAjuda()
        msg2 = frase.fimMensagemAjuda()
        
        attr["recent_response"] = msg1
        
        return (handler_input.response_builder.speak(msg1).ask(msg2).response)

# Inteção de Itens
class ItemIntent(AbstractRequestHandler):
    """Handler for Item Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ItemIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        
        # Modifica o atributo de estado da sessão
        attr = handler_input.attributes_manager.session_attributes
        attr["state"] = "CONTINUAR"
                
        slots = handler_input.request_envelope.request.intent.slots
        item = slots['item']

        id_item = item.resolutions.resolutions_per_authority[0].values[0].value.id
        nome_item = item.resolutions.resolutions_per_authority[0].values[0].value.name
        msg1 = lol.descricaoItem(id_item) + ". " + frase.fimMensagemAjuda()
        msg2 = frase.fimMensagemAjuda()
        
        attr["recent_response"] = msg1
        
        return (handler_input.response_builder.speak(msg1).ask(msg2).response)


class BuildRecomendada(AbstractRequestHandler):
    """Handler for build Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BuildRecomendada")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        
        # Modifica o atributo de estado da sessão
        attr = handler_input.attributes_manager.session_attributes
        attr["state"] = "CONTINUAR"
                
        slots = handler_input.request_envelope.request.intent.slots
        campeao = slots['campeao']

        #id_camp = campeao.resolutions.resolutions_per_authority[0].values[0].value.id
        #nome_camp = campeao.resolutions.resolutions_per_authority[0].values[0].value.name
        #msg1 = lol.itensRecomendadosCampeao(nome_camp) + ". " + frase.fimMensagemAjuda()
        #msg2 = frase.fimMensagemAjuda()
        
        msg1 = frase.emDesenvolvimento() + ". " + frase.fimMensagemAjuda()
        msg2 = frase.fimMensagemAjuda()
        
        attr["recent_response"] = msg1
        
        return (handler_input.response_builder.speak(msg1).ask(msg2).response)

class ClasseCampeoes(AbstractRequestHandler):
    """Handler for build Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ClasseCampeoes")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        
        # Modifica o atributo de estado da sessão
        attr = handler_input.attributes_manager.session_attributes
        attr["state"] = "CONTINUAR"
                
        slots = handler_input.request_envelope.request.intent.slots
        campeao = slots['campeao']

        id_camp = campeao.resolutions.resolutions_per_authority[0].values[0].value.id
        nome_camp = campeao.resolutions.resolutions_per_authority[0].values[0].value.name
        msg1 = lol.classeCampeao(nome_camp) + ". " + frase.fimMensagemAjuda()
        msg2 = frase.fimMensagemAjuda()
        
        attr["recent_response"] = msg1
        
        return (handler_input.response_builder.speak(msg1).ask(msg2).response)

# Inteção de Versão do LoL usada
class VersaoIntent(AbstractRequestHandler):
    """Handler for Item Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("VersaoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        
        # Modifica o atributo de estado da sessão
        attr = handler_input.attributes_manager.session_attributes
        attr["state"] = "CONTINUAR"
                
        msg1 = frase.versaoLol() + ". " + frase.fimMensagemAjuda()
        msg2 = frase.fimMensagemAjuda()
        
        attr["recent_response"] = msg1
        
        return (handler_input.response_builder.speak(msg1).ask(msg2).response)


class YesIntentHandler(AbstractRequestHandler):
    """Handler for repeating the response to the user."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        attr = handler_input.attributes_manager.session_attributes
        return ask_utils.is_intent_name("AMAZON.YesIntent")(handler_input) and attr.get("state") == "CONTINUAR"
    
    def handle(self, handler_input):
        msg1 = frase.inicio()
        return handler_input.response_builder.speak(msg1).ask(msg1).response


class NoIntentHandler(AbstractRequestHandler):
    """Handler for repeating the response to the user."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        attr = handler_input.attributes_manager.session_attributes
        return ask_utils.is_intent_name("AMAZON.NoIntent")(handler_input) and attr.get("state") == "CONTINUAR"
    
    def handle(self, handler_input):
        msg1 = frase.fim()
        return handler_input.response_builder.speak(msg1).response


class RepeatHandler(AbstractRequestHandler):
    """Handler for repeating the response to the user."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.RepeatIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In RepeatHandler")
        attr = handler_input.attributes_manager.session_attributes
        response_builder = handler_input.response_builder
        
        # Modifica o atributo de estado da sessão
        attr = handler_input.attributes_manager.session_attributes
        attr["state"] = "CONTINUAR"
        
        msg2 = frase.fimMensagemAjuda()
        
        if "recent_response" in attr:
            response_builder.speak(attr["recent_response"]).ask("Dalalsas auau")
            return response_builder.response
        
        response_builder.speak("Não disse nada para poder repetir").ask(msg2)
        return response_builder.response

# Intenção de Ajuda
class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        
        msg1 = frase.ajuda()
        msg2 = frase.fimMensagemAjuda()
        
        attr["recent_response"] = msg1
        attr["state"] = "CONTINUAR"
        
        return (handler_input.response_builder.speak(msg1).ask(msg2).response)

# Intenção de Cancelar
class CancelIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        
        if(attr["state"] == ""):
            msg1 = frase.fim()
            return (handler_input.response_builder.speak(msg1).response)
        else:
            msg1 = frase.cancelarAcao()
            msg2 = frase.perguntaAjuda()
            attr["state"] = "CONTINUAR"
            return (handler_input.response_builder.speak(msg1).ask(msg2).response)

# Intenção de Parar
class StopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        msg1 = frase.fim()
        return handler_input.response_builder.speak(msg1).response

# Intenção de Cancelar
class HomeIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.NavigateHomeIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.session_attributes
        
        msg1 = frase.inicio()
        msg2 = frase.inicio()

        attr["recent_response"] = msg1
        attr["state"] = ""
        
        return (handler_input.response_builder.speak(msg1).ask(msg2).response)

# Fim de Sessão
class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = frase.fim()

        return (handler_input.response_builder.speak(speak_output).response)


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + ". " + handler_input
        
        return ( handler_input.response_builder.speak(speak_output).response )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        attr = handler_input.attributes_manager.session_attributes
        
        # Modifica o atributo de estado da sessão
        attr = handler_input.attributes_manager.session_attributes
        attr["state"] = "CONTINUAR"
        
        logger.error(exception, exc_info=True)

        speak_output = frase.desculpa() + ". " + frase.perguntaAjuda()

        return (handler_input.response_builder.speak(speak_output).ask(speak_output).response)

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.

sb = CustomSkillBuilder(api_client=DefaultApiClient())

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HistoriaIntentHandler())
sb.add_request_handler(RunasIntentHandler())
sb.add_request_handler(DicasAliadosIntent())
sb.add_request_handler(DicasContraIntent())
sb.add_request_handler(HabilidadesIntent())
sb.add_request_handler(PassivaIntent())
sb.add_request_handler(ItemIntent())
sb.add_request_handler(BuildRecomendada())
sb.add_request_handler(ClasseCampeoes())
sb.add_request_handler(VersaoIntent())

sb.add_request_handler(YesIntentHandler())
sb.add_request_handler(NoIntentHandler())
sb.add_request_handler(RepeatHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(HomeIntentHandler())
sb.add_request_handler(StopIntentHandler())
sb.add_request_handler(CancelIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler())

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()