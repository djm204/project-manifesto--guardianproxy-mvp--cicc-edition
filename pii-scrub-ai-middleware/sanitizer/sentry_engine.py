from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.nlp_engine import NlpEngineProvider
from presidio_analyzer.recognizer_registry import RecognizerRegistry

def sanitize_pii(input_text):
    # Create configuration containing execution mode and the list of requested recognizers
    configuration = {
        "nlp_engine_name": "spacy",
        "models": [{"lang_code": "en", "model_name": "en_core_web_trf"}],
        "denial_list": [],
        "recognizers": []
    }
    
    # Create NLP engine based on configuration
    provider = NlpEngineProvider(nlp_configuration=configuration)
    nlp_engine = provider.create_engine()
    
    # Create recognizer registry
    registry = RecognizerRegistry(nlp_engine=nlp_engine, supported_languages=["en"])
    
    # Create analyzer engine
    engine = AnalyzerEngine(registry=registry, nlp_engine=nlp_engine)
    
    # Use the analyzer engine to recognize and sanitize PII
    results = engine.analyze(text=input_text, entities=[], language="en")
    
    # Create a dictionary to store the mappings from tokens to original PII
    token_mapping = {}
    
    # Replace all PII with tokens and store the mappings
    for result in results:
        token = f"{{{{CLIENT_{len(token_mapping) + 1}}}}}"
        token_mapping[token] = result.text
        input_text = input_text.replace(result.text, token)
    
    return input_text, token_mapping