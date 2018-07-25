from django.shortcuts import render

# Create your views here.

from ner.Parameters import logger
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from ner import spacy_predict_ner


@csrf_exempt
def getEntityResponse(request, inputString):
    
    logger.debug ('Request reached in ner views')
    logger.info ('User input -->'+ inputString )
    response = spacy_predict_ner.predict_ner(inputString)
    logger.debug ('response -->'+ response )

    return HttpResponse( response)
