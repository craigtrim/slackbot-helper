#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from pprint import pprint

from slackbot_helper import normalize_event
from slackbot_helper.core.bp import NormalizeIncomingEvent
from slackbot_helper.core.dto import SlackIds

d_incoming = {
    'blocks': [
        {
            'block_id': '2YJR',
            'text': {
                'emoji': True,
                'text': 'Note my conduct.',
                'type': 'plain_text'
            },
            'type': 'section'
        },
        {
            'block_id': 'u31',
            'type': 'divider'
        },
        {
            'block_id': 'Ts06',
            'elements': [
                {
                    'text': '<@U04HLMTUDSR> Show me images of spaceships.',
                    'type': 'mrkdwn',
                    'verbatim': False
                }
            ],
            'type': 'context'
        }
    ],
    'channel': 'C04LPA56H8C',
    'team': 'T045AR44M70',
    'text': "This content can't be displayed.",
    'ts': 1675049179.061859,
    'type': 'app_mention',
    'user': 'U04LRAW3G0K'
}

d_normalized_expected = {
    'analysis': {
        'commands': [

        ],
        'meta_mode': 'human2bot',
        'meta_type': 'H2B_SINGLE',
        'text_1': 'Note my conduct.',
        'text_2': 'Note my conduct.',
        'user_all': [
            'U04HLMTUDSR'
        ],
        'user_source': 'U04LRAW3G0K',
        'user_target': 'U04HLMTUDSR'
    },
    'event': {
        'blocks': [
            {
                'block_id': '2YJR',
                'text': {
                    'emoji': True,
                    'text': 'Note my conduct.',
                    'type': 'plain_text'
                },
                'type': 'section'
            },
            {
                'block_id': 'u31',
                'type': 'divider'
            },
            {
                'block_id': 'Ts06',
                'elements': [
                    {
                        'text': '<@U04HLMTUDSR> Show me images of spaceships.',
                        'type': 'mrkdwn',
                        'verbatim': False
                    }
                ],
                'type': 'context'
            }
        ],
        'channel': 'C04LPA56H8C',
        'team': 'T045AR44M70',
        'text': "This content can't be displayed.",
        'ts': 1665195085.499959,
        'type': 'app_mention',
        'user': 'U04LRAW3G0K'
    },
    'membership': '85e8d1eb_46c2_11ed_97a0_4c1d96716627'
}


def slack_ids() -> SlackIds:
    return ['U04HLMTUDSR', 'U04LRAW3G0K']


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


if __name__ == '__main__':
    main()
