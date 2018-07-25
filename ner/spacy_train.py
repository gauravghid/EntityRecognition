#!/usr/bin/env python

from __future__ import unicode_literals, print_function

import plac
import random
from pathlib import Path
import spacy
import time
import datetime
from spacy.util import minibatch
from ner import train_data
from ner.Parameters import logger


# training data
@plac.annotations(
    model=("Model name. Defaults to blank 'en' model.", "option", "m", str),
    new_model_name=("New model name for model meta.", "option", "nm", str),
    output_dir=("Optional output directory", "option", "o", Path),
    n_iter=("Number of training iterations", "option", "n", int))
def train_model(model, new_model_name, output_dir, LABEL, TRAIN_DATA, n_iter=20):
    """Set up the pipeline and entity recognizer, and train the new entity."""
    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        logger.info("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank('en')  # create blank Language class
        logger.info("Created blank 'en' model")
    # Add entity recognizer to model if it's not in the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner)
    # otherwise, get it, so we can add labels to it
    else:
        ner = nlp.get_pipe('ner')

    #ner.add_label('APPROVER')   # add new entity label to entity recognizer
    ner.add_label(LABEL)
    if model is None:
        optimizer = nlp.begin_training()
    else:
        # Note that 'begin_training' initializes the models, so it'll zero out
        # existing entity types.
        optimizer = nlp.entity.create_optimizer()

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            losses = {}

            batches = minibatch(TRAIN_DATA)
            for batch in batches:
               texts, annotations = zip(*batch)
               nlp.update(texts, annotations, sgd=optimizer, drop=0.25,
                          losses=losses)
               logger.info(str (itn) + ' : ' + str (losses))
               ts = time.time()
               st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
               logger.info (st)

    
    # save model to output directory
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta['name'] = new_model_name  # rename model
        nlp.to_disk(output_dir)
        logger.info("Saved model to" + str(output_dir))

# To train invoice
def train_invoice():

    data = train_data.INVOICE_TRAIN_DATA
    label = train_data.INVOICE_LABEL
    model_name = train_data.invoice_model
    output_dir = train_data.invoice_model_path
    
    train_model (model='en', new_model_name = model_name, output_dir  =output_dir, LABEL = label, TRAIN_DATA = data, n_iter=20)

# To train approver
def train_approver():

    data = train_data.APPROVER_DATA
    label = train_data.APPROVER_LABEL
    model_name = train_data.approver_model
    output_dir = train_data.approver_model_path
    
    train_model (model='en', new_model_name = model_name, output_dir  =output_dir, LABEL = label, TRAIN_DATA = data, n_iter=20)




