#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from pprint import pprint

from slackbot_helper import normalize_event
from slackbot_helper.core.bp import NormalizeIncomingEvent
from slackbot_helper.core.dto import SlackIds

d_incoming = {
    'blocks': [
        {
            'block_id': 'HR0',
            'text': {
                'emoji': True,
                'text': 'Keep an eye on my moves.',
                'type': 'plain_text'
            },
            'type': 'section'
        },
        {
            'block_id': 'cWmZy',
            'type': 'divider'
        },
        {
            'block_id': 'PSs',
            'elements': [
                {
                    'text': '<@U04HLMTUDSR> Show me everything with sun in it.',
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
    'ts': 1675053514.430099,
    'type': 'app_mention',
    'user': 'U04LRAW3G0K'
}

d_normalized_expected = {
    'analysis': {
        'commands': [

        ],
        'meta_mode': 'human2bot',
        'meta_type': 'H2B_SINGLE',
        'text_1': 'Keep an eye on my moves. <@U04HLMTUDSR> Show me everything with sun in it.',
        'text_2': 'Keep an eye on my moves. Show me everything with sun in it.',
        'user_all': [
            'U04HLMTUDSR'
        ],
        'user_source': 'U04LRAW3G0K',
        'user_target': 'U04HLMTUDSR'
    },
    'event': {
        'blocks': [
            {
                'block_id': 'HR0',
                'text': {
                    'emoji': True,
                    'text': 'Keep an eye on my moves.',
                    'type': 'plain_text'
                },
                'type': 'section'
            },
            {
                'block_id': 'cWmZy',
                'type': 'divider'
            },
            {
                'block_id': 'PSs',
                'elements': [
                    {
                        'text': '<@U04HLMTUDSR> Show me everything with sun in it.',
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
        'thread_ts': None,
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

    pprint(d_normalized)

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
