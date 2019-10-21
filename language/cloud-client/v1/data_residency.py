# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def data_residency():
    """Set a regional data endpoint using data residency"""
    # [START language_client_library]
    # [START language_data_residency]
    # Imports the Google Cloud client library
    from google.cloud import language

    client_options = {'api_endpoint': 'language.googleapis.com:443'}

    # Instantiates a client
    client = language.LanguageServiceClient(client_options=client_options)
    # [END language_data_residency]

    # The text to analyze
    document = language.types.Document(
        content='Hello, world!',
        type=language.enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
    # [END language_client_library]


if __name__ == '__main__':
    data_residency()
