#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from slackbot_helper.bp import NormalizeIncomingEvent
from slackbot_helper.dto import SlackIds
from slackbot_helper import normalize_event


d_incoming = {
    "blocks": [
        {
            "block_id": "vz+U",
            "elements": [
                {
                    "elements": [
                        {
                            "type": "user",
                            "user_id": "U045HCSMG8K"
                        },
                        {
                            "text": " dead ahead!",
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
    "text": "<@U045HCSMG8K> dead ahead!",
    "ts": 1665195085.499959,
    "type": "app_mention",
    "user": "U04674UNRBJ"
}

d_normalized_expected = {
    "analysis": {
        "commands": [

        ],
        "meta_mode": "human2bot",
        "meta_type": "H2B_SINGLE",
        "text_1": "@U045HCSMG8K dead ahead!",
        "text_2": "dead ahead!",
        "user_all": [
            "U045HCSMG8K"
        ],
        "user_source": "U04674UNRBJ",
        "user_target": "U045HCSMG8K"
    },
    "event": {
        "blocks": [
            {
                "block_id": "vz+U",
                "elements": [
                    {
                            "elements": [
                                {
                                    "type": "user",
                                    "user_id": "U045HCSMG8K"
                                },
                                {
                                    "text": " dead ahead!",
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
        "text": "<@U045HCSMG8K> dead ahead!",
        "ts": 1665195085.499959,
        "type": "app_mention",
        "user": "U04674UNRBJ"
    },
    "membership": "85e8d1eb_46c2_11ed_97a0_4c1d96716627"
}


def slack_ids() -> SlackIds:
    return ['U045HCSMG8K']


def test_orchestrator():

    bp = NormalizeIncomingEvent(bot_ids=slack_ids())
    assert bp

    d_normalized = bp.process(d_incoming)

    # the 'membership' value is dynamically generated
    # so we can't test as-is ...
    assert 'membership' in d_normalized
    d_normalized['membership'] = '85e8d1eb_46c2_11ed_97a0_4c1d96716627'

    # same with 'timestamp' ...
    # can't test a dynamically generated value
    assert 'ts' in d_normalized['event']
    d_normalized['event']['ts'] = 1665195085.499959

    assert d_normalized == d_normalized_expected


def test_root_init():

    d_normalized = normalize_event(d_event=d_incoming, bot_ids=slack_ids())

    # the 'membership' value is dynamically generated
    # so we can't test as-is ...
    assert 'membership' in d_normalized
    d_normalized['membership'] = '85e8d1eb_46c2_11ed_97a0_4c1d96716627'

    # same with 'timestamp' ...
    # can't test a dynamically generated value
    assert 'ts' in d_normalized['event']
    d_normalized['event']['ts'] = 1665195085.499959

    assert d_normalized == d_normalized_expected


def main():
    test_orchestrator()
    test_root_init()


if __name__ == "__main__":
    main()
