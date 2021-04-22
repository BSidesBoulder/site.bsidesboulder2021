#!/usr/bin/python3

import requests
import json
from jinja2 import Template
import base64

SPEAKER_API = 'https://sessionize.com/api/v2/yrggtml6/view/Speakers'
SESSION_API = 'https://sessionize.com/api/v2/yrggtml6/view/Sessions'

# get the speakers
speaker_req = requests.get(SPEAKER_API)
speakers = json.loads(speaker_req.content.decode())

session_req = requests.get(SESSION_API)
sessions = json.loads(session_req.content.decode())

template = None

with open('helperscripts/speaker.html','r') as speaker_template:
    data = ''.join(speaker_template.readlines())
    template = Template(data)

for speaker in speakers:
    output = template.render(speaker)
    message = {}
    message['id'] = speaker['id']
    message['fromfieldFriendly'] = speaker['fullName']
    message['fromfield'] = 'no-reply@bsidesboulder.org'
    message['shortdate'] = "Fri Apr 24"
    message['longdate'] = 'Friday April 24, 2021 12:00:01 AM'
    message['date'] = '2021-04-24 00:00:01.000000'
    message['subject'] = speaker['sessions'][0]['name']
    message['message'] = base64.encodestring(output.encode('utf8')).decode()

    with open(f'./data/speaker/{speaker["id"]}.json', 'w') as jsondata:
        jsondata.write(json.dumps(message))