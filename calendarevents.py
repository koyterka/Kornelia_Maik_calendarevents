from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import json
import EndOfEvent


def main():
    scopes = 'https://www.googleapis.com/auth/calendar'     # set OAuth scope
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', scopes)
        creds = tools.run_flow(flow, store)
    gcal = discovery.build('calendar', 'v3', http=creds.authorize(Http()))

    with open('data.txt') as json_file:
        data = json.load(json_file)
        for event in data['events']:        # iterate over all events in the json file
            end = EndOfEvent.endOfEvent(event['start'], event['duration'])      # calculate the end of event
            gmt_off = event['gmt']

            # prepare the proper event body for google calendar API
            EVENT = {
                'summary': event['summary'],
                'start': {'dateTime': event['start']+"%s" % gmt_off},
                'end': {'dateTime': end+"%s" % gmt_off},
                'description': event['description'],
                'location': event['location'],
                'reminders': {
                    'useDefault': False,
                    'overrides': [
                        {'method': 'email', 'minutes': event['reminders']['email']},
                        {'method': 'popup', 'minutes': event['reminders']['popup']},
                    ],
                },
            }

            # create the event
            e = gcal.events().insert(calendarId='primary', body=EVENT).execute()

            # print the event just to make sure it worked
            print('''%r event added:
                Start: %s
                End:   %s''' % (e['summary'].encode('utf-8'),
                                e['start']['dateTime'], e['end']['dateTime']))


main()
