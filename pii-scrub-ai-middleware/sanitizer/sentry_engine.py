import re
from presidio_analyzer import AnalyzerEngine, RecognizerRegistry
from presidio_analyzer.predefined_recognizers import PatternRecognizer

def sanitize_pii(text: str) -> tuple:
    recognizers = [PatternRecognizer(supported_entity="CA_SIN", patterns=["[0-9]{3} [0-9]{3} [0-9]{3}", "[0-9]{9}"]),
                   PatternRecognizer(supported_entity="CA_UCI", patterns=["[0-9]{8}", "[0-9]{10}"])]
    analyzer = AnalyzerEngine(registry=RecognizerRegistry(recognizers=recognizers))
    analyzer_results = analyzer.analyze(text, entities=["CA_SIN", "CA_UCI"], language="en")
    sanitized_text = text
    token_mapping = {}
    for result in analyzer_results:
        token = f"{{{{CLIENT_{len(token_mapping)+1}}}}}"
        sanitized_text = sanitized_text.replace(result.text, token)
        token_mapping[token] = result.text
    return sanitized_text, token_mapping