#!/usr/bin/env python3

# Copyright 2017 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START import_libraries]
import argparse
import uuid

import os
import json
import logging
import aiy.i18n

import dialogflow_v2 as dialogflow
# [END import_libraries]

logger = logging.getLogger("dialogflow")
credentials_file = os.path.expanduser('~/cloud_speech.json')
_detect_intent_texts = None

class _Detect_Intent_Texts(object):

    def __init__(self, credentials_file):

        self.language_code = aiy.i18n.get_language_code()
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_file
        self.project_id = format(json.load(open(credentials_file))['project_id'])

    # [START dialogflow_detect_intent_text]
    def recognize(self, session_id, texts):
        """Returns the result of detect intent with texts as inputs.
        Using the same `session_id` between requests allows continuation
        of the conversaion."""
        session_client = dialogflow.SessionsClient()

        session = session_client.session_path(self.project_id, session_id)
        logger.debug('Session path: {}'.format(session))

        text_input = dialogflow.types.TextInput(
            text=texts, language_code=self.language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        response = session_client.detect_intent(
            session=session, query_input=query_input)

        logger.info('Query text: {}'.format(response.query_result.query_text))
        logger.info('Detected intent: {} (confidence: {})'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
        logger.info('Fulfillment text: {}'.format(
            response.query_result.fulfillment_text))
        return response
    # [END dialogflow_detect_intent_text]

def get_recognizer():
    global _detect_intent_texts
    if not _detect_intent_texts:
        _detect_intent_texts = _Detect_Intent_Texts(credentials_file)
    return _detect_intent_texts
