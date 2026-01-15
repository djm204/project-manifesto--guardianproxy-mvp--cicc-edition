from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.nlp_engine import NlpEngineProvider
from presidio_analyzer.recognizer_registry import RecognizerRegistry

def sanitize_pii(raw_text):
    # Initialize Presidio's analyzer engine with a local Spacy model
    nlp_engine_provider = NlpEngineProvider(nlp_artifacts_dir='en_core_web_trf')
    recognizer_registry = RecognizerRegistry()
    analyzer_engine = AnalyzerEngine(nlp_engine_provider=nlp_engine_provider, recognizer_registry=recognizer_registry)

    # Analyze the text
    results = analyzer_engine.analyze(correlation_id='correlation-id', text=raw_text, entities=[], language='en')

    # Generate masked string and token mapping
    masked_string = raw_text
    token_mapping = {}
    for result in results:
        masked_string = masked_string.replace(result.entity_text, "{{" + result.entity_type + "}}")
        token_mapping[result.entity_type] = result.entity_text

    return masked_string, token_mapping