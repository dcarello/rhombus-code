import json
import requests

webhook_url = "https://hooks.slack.com/services/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"
slack_data = {'text': "My first Slack message yay"}
response = requests.post(
    webhook_url, data=  json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
)

if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
)