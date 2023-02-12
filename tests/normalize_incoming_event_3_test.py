#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from logging.handlers import DEFAULT_TCP_LOGGING_PORT
from pprint import pprint

from slackbot_helper import normalize_event

d_event_incoming = {
    'blocks': [
        {
            'block_id': '4rdo',
            'text': {
                'text': '<@U045HCSMG8K> How long can particulate pollution remain airborne',
                'type': 'mrkdwn',
                'verbatim': False
            },
            'type': 'section'
        }
    ],
    'channel': 'C046DB9TLEL',
    'team': 'T045AR44M70',
    'text': '<@U045HCSMG8K> How long can particulate pollution remain airborne?',
    'ts': 1665724403.461959,
    'type': 'app_mention',
    'user': 'U046G4FURQT'
}

d_event_expected = {
    'analysis': {
        'commands': [],
        'meta_mode': 'bot2bot',
        'meta_type': 'H2H_SINGLE',
        'text_1': '<@U045HCSMG8K> How long can particulate pollution remain airborne',
        'text_2': 'How long can particulate pollution remain airborne.',
        'user_all': ['U045HCSMG8K'],
        'user_source': 'U046G4FURQT',
        'user_target': 'U045HCSMG8K'
    },
    'event': {
        'blocks': [
            {
                'block_id': '4rdo',
                'text': {
                    'text': '<@U045HCSMG8K> How long can particulate pollution remain airborne',
                    'type': 'mrkdwn',
                    'verbatim': False
                },
                'type': 'section'
            }
        ],
        'channel': 'C046DB9TLEL',
        'team': 'T045AR44M70',
        'text': '<@U045HCSMG8K> How long can particulate pollution remain airborne?',
        'ts': 1665724403.461959,
        'thread_ts': None,
        'type': 'app_mention',
        'user': 'U046G4FURQT'
    },
    'membership': '70e4c2dd_4b81_11ed_a836_4c1d96716627'
}


def test_root_init():

    d_normalized = normalize_event(d_event=d_event_incoming, bot_ids=[])
    pprint(d_normalized)

    assert 'membership' in d_normalized
    d_normalized['membership'] = '70e4c2dd_4b81_11ed_a836_4c1d96716627'

    assert 'ts' in d_normalized['event']
    d_normalized['event']['ts'] = 1665724403.461959

    assert d_normalized == d_event_expected


def main():
    test_root_init()


if __name__ == '__main__':
    main()
