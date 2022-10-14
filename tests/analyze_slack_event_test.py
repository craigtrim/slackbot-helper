#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from pprint import pprint

from slackbot_helper.svc import AnalyzeSlackEvent

d_event_incoming = {
    "blocks": [
        {
            "block_id": "m5kF",
            "elements": [
                {
                    "elements": [
                        {
                            "type": "user",
                            "user_id": "U046G4FURQT"
                        },
                        {
                            "text": " please ask ",
                            "type": "text"
                        },
                        {
                            "type": "user",
                            "user_id": "U045HCSMG8K"
                        },
                        {
                            "text": " a random question",
                            "type": "text"
                        }
                    ],
                    "type": "rich_text_section"
                }
            ],
            "type": "rich_text"
        }
    ],
    "channel": "C046DB9TLEL",
    "client_msg_id": "bd324672-9e87-4629-af81-aaa4d701082b",
    "event_ts": "1665723755.778069",
    "team": "T045AR44M70",
    "text": "<@U046G4FURQT> please ask <@U045HCSMG8K> a random question",
    "ts": "1665723755.778069",
    "type": "app_mention",
    "user": "U04674UNRBJ"
}


def test_service():

    # U046G4FURQT; student
    # U045HCSMG8K; iceberg

    d_result_1 = AnalyzeSlackEvent(
        bot_ids=['U046G4FURQT']).process(d_event_incoming)

    d_result_2 = AnalyzeSlackEvent(
        bot_ids=['U045HCSMG8K']).process(d_event_incoming)

    assert d_result_1 == d_result_2

    # user source is U04674UNRBJ (craig) who said: '@U046G4FURQT (student) please ask @U045HCSMG8K (iceberg) a random question'
    # so the user_source and user_target are true for this current event
    # but they are not meant to be used for the 'next event'
    # there has been confusion on this point
    # the next event will need a new user source and user target

    assert d_result_1 == {
        'commands': [],
        'meta_mode': 'bot2bot',
        'meta_type': 'OTHER',
        'text_1': '@U046G4FURQT please ask @U045HCSMG8K a random question',
        'text_2': 'please ask a random question.',
        'user_all': ['U046G4FURQT', 'U045HCSMG8K'],
        'user_source': 'U04674UNRBJ',
        'user_target': 'U046G4FURQT'
    }


def main():
    test_service()


if __name__ == "__main__":
    main()
