#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from pprint import pprint

from slackbot_helper.core.dmo import MessageTypeAnalysis
from slackbot_helper.core.dto import MessageType

# FOR REFERENCE ONLY ... not used in test
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
    'text': '<@U045HCSMG8K> How long can particulate pollution remain airborne?',
    'ts': 1665724403.461959,
    'type': 'app_mention',
    'user': 'U046G4FURQT'
}


def test_component_1():

    # 20221013; this is what actually happened

    dmo = MessageTypeAnalysis(
        user_ids=['U045HCSMG8K'],
        bot_ids=[],
        message_text='<@U045HCSMG8K> How long can particulate pollution remain airborne')

    assert dmo

    d_result = dmo.process()
    pprint(d_result)

    # the outcome of 'MessageType.H2H_SINGLE' seems reasonable
    # as no bot-ids are provided ...

    assert d_result == {
        'commands': [],
        'message_text': 'How long can particulate pollution remain airborne.',
        'message_type': MessageType.H2H_SINGLE,
        'persist_events': False
    }


def test_component_2():

    # 20221013; what if we populate 'bot_ids=[]' with both iceberg and student?

    dmo = MessageTypeAnalysis(
        user_ids=['U045HCSMG8K'],
        bot_ids=['U046G4FURQT', 'U045HCSMG8K'],
        message_text='<@U045HCSMG8K> How long can particulate pollution remain airborne')

    assert dmo

    d_result = dmo.process()
    pprint(d_result)

    # the outcome of 'MessageType.H2B_SINGLE' seems reasonable
    # if we assume that bot_ids represents the target bots

    # TODO: but what if the 'user_ids=[...]' has a bot_id?  is this B2H or B2B?  This needs more work ...

    assert d_result == {
        'commands': [],
        'message_text': 'How long can particulate pollution remain airborne.',
        'message_type': MessageType.H2B_SINGLE,
        'persist_events': False
    }


def main():
    test_component_1()
    test_component_2()


if __name__ == '__main__':
    main()
