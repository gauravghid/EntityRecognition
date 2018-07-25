from django.apps import AppConfig
from ner import spacy_train
from ner import train_data
import spacy
from spacy.attrs import ORTH, LEMMA, TAG, ENT_TYPE, ENT_IOB
from ner.Parameters import logger

class NerConfig(AppConfig):
    name = 'ner'
    invoice_model = None
    approver_model = None
    en_Model = None


    def train_models():
     logger.info ('Training NER models in app start up')
     #spacy_train.train_invoice()
     spacy_train.train_approver ()


    def initialiseModels ():
      #NerConfig.invoice_model = spacy.load(train_data.invoice_model_path)
      NerConfig.approver_model = spacy.load(train_data.approver_model_path)
      NerConfig.en_Model = spacy.load('en') 
      NerConfig.en_Model.tokenizer.add_special_case('taiwan', [{ORTH: 'taiwan', LEMMA: 'Taiwan', TAG: 'NNP', ENT_TYPE: 'GPE', ENT_IOB: 3}])               
      NerConfig.en_Model.tokenizer.add_special_case('philippines', [{ORTH: 'philippines', LEMMA: 'Philippines', TAG: 'NNP', ENT_TYPE: 'GPE', ENT_IOB: 3}])


  # App start
    def ready(self):
      
      NerConfig.train_models()
      NerConfig.initialiseModels ()

    def getModels( ):
      
      return NerConfig.approver_model, NerConfig.en_Model, NerConfig.invoice_model;
