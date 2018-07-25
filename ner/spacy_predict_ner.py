#!/usr/bin/env python
# coding: utf8

import spacy
from ner.apps import NerConfig
from ner.Parameters import logger
import json

#To get NER predictions from input string
def predict_ner (inputString):

  logger.info ('Input string : ' + inputString)
  
  entities = []
  approver_model, en_Model, invoice_model = NerConfig.getModels ()
  approver_doc = approver_model(inputString)
  for ent in approver_doc.ents:
      logger.debug(ent.label_, ent.text)
      entities.append ({'Label' : ent.label_, 'text' : ent.text, 'start' : ent.start_char, 'end' : ent.end_char })

  en_doc = en_Model(inputString)
  for ent in en_doc.ents:
      logger.debug(ent.label_, ent.text)
      entities.append ({'Label' : ent.label_, 'text' : ent.text, 'start' : ent.start_char, 'end' : ent.end_char })
  
  logger.info ('Entity results : ' + json.dumps(entities))

  return json.dumps(entities);
