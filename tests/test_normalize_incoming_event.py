#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from pprint import pprint

from slackbot_helper.bp import NormalizeIncomingEvent


def test_orchestrator():

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

    d_normalized = NormalizeIncomingEvent().process(d_incoming)
    pprint(d_normalized)


def main():
    test_orchestrator()


if __name__ == "__main__":
    main()
