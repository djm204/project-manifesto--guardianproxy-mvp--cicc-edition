from presidio_analyzer import AnalyzerEngine
from presidio_anomaly_detector import AnomalyDetector
from custom_recognizers import SinRecognizer, UciRecognizer

analyzer = AnalyzerEngine()
anomaly_detector = AnomalyDetector()

analyzer.registry.add_recognizer(SinRecognizer())
analyzer.registry.add_recognizer(UciRecognizer())

def sanitize_pii(text):
    """Sanitize PII from given text."""
    analysis_results = analyzer.analyze(text=text, language='en')
    anomalies = anomaly_detector.detect_anomalies(results=analysis_results)
    
    sanitized_text = text
    token_mapping = {}
    
    for result in analysis_results:
        pii = result.entity_text
        token = "{{CLIENT_" + str(len(token_mapping) + 1) + "}}"
        sanitized_text = sanitized_text.replace(pii, token)
        token_mapping[token] = pii
        
    return sanitized_text, token_mapping