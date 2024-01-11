# ementador.py

# import spacy_universal_sentence_encoder
import spacy

class Ementador:
    def __init__(self):
        # self.nlp = spacy_universal_sentence_encoder.load_model('pt_core_news_lg')
        self.nlp = spacy.load('pt_core_news_lg')

    def calcular_similaridade(self, texto_1, texto_2):
        doc_1 = self.nlp(texto_1)
        doc_2 = self.nlp(texto_2)
        return doc_1.similarity(doc_2)
