#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from logging.handlers import DEFAULT_TCP_LOGGING_PORT
from pprint import pprint

from slackbot_helper import normalize_event

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

d_event_expected = {
    "analysis": {
        "commands": [

        ],
        "meta_mode": "bot2bot",
        "meta_type": "H2H_SINGLE",
        "text_1": "@U046G4FURQT please ask @U045HCSMG8K a random question",
        "text_2": "please ask a random question.",
        "user_all": [
            "U046G4FURQT",
            "U045HCSMG8K"
        ],
        "user_source": "U04674UNRBJ",
        "user_target": "U046G4FURQT"
    },
    "event": {
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
        "team": "T045AR44M70",
        "text": "<@U046G4FURQT> please ask <@U045HCSMG8K> a random question",
        "ts": 1665723755.778069,
        "type": "app_mention",
        "user": "U04674UNRBJ"
    },
    "membership": "5859e84f_4b7e_11ed_b2be_4c1d96716627"
}


def test_root_init():

    d_normalized = normalize_event(d_event=d_event_incoming, bot_ids=[])
    pprint(d_normalized)

    assert 'membership' in d_normalized
    d_normalized['membership'] = "5859e84f_4b7e_11ed_b2be_4c1d96716627"

    assert 'ts' in d_normalized['event']
    d_normalized['event']['ts'] = 1665723755.778069

    assert d_normalized == d_event_expected


def main():
    test_root_init()


if __name__ == "__main__":
    main()
