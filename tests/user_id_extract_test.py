#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from pprint import pprint

from slackbot_helper.dmo import UserIdExtract

d_event_incoming = {
    "blocks": [
        {
            "block_id": "4rdo",
            "text": {
                "text": "<@U045HCSMG8K> How long can particulate pollution remain airborne?",
                "type": "mrkdwn",
                "verbatim": False
            },
            "type": "section"
        }
    ],
    "channel": "C046DB9TLEL",
    "team": "T045AR44M70",
    "text": "<@U045HCSMG8K> How long can particulate pollution remain airborne?",
    "ts": 1665724403.461959,
    "type": "app_mention",
    "user": "U046G4FURQT"
}


def test_component():

    dmo = UserIdExtract()
    assert dmo

    assert dmo.process(d_event_incoming) == ['U045HCSMG8K']


def main():
    test_component()


if __name__ == "__main__":
    main()
