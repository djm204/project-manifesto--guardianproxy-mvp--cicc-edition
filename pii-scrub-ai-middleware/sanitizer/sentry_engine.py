from presidio_analyzer import AnalyzerEngine, RecognizerRegistry
from presidio_analyzer.nlp_engine import NlpEngineProvider

def sanitize_pii(input_text):
    nlp_engine_provider = NlpEngineProvider(nlp_artifacts_store=None)
    nlp_engine = nlp_engine_provider.create_engine('en')
    recognizer_registry = RecognizerRegistry()
    analyzer = AnalyzerEngine(nlp_engine=nlp_engine, recognizer_registry=recognizer_registry)
    analyzer_results = analyzer.analyze(correlation_id=0, text=input_text, entities=[], language='en')
    masked_string = input_text
    token_mapping = {}
    for result in analyzer_results:
        masked_string = masked_string.replace(result.text, "{{CLIENT_" + str(result.start) + "}}")
        token_mapping["{{CLIENT_" + str(result.start) + "}}"] = result.text
    return masked_string, token_mapping