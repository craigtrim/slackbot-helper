#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from pprint import pprint

from slackbot_helper.core.dmo import UserIdExtract

d_event = {
    'blocks': [

        {
            'block_id': 'af1',
            'text': {
                'text': '<@U046G4FURQT> *The capacity is low because* water must be pumped up a hill, requiring a large reservoir of water and, of course, a hill.',
                'type': 'mrkdwn',
                'verbatim': False
            },
            'type': 'section'
        },

        {
            'block_id': 'b0W/O', 'type': 'divider'
        },

        {
            'block_id': 'Hph',
            'text': {
                'text': ':ledger: *avoid-climate-disaster* Chapter 4:',
                'type': 'mrkdwn',
                'verbatim': False
            },
            'type': 'section'
        },

        {
            'block_id': 'RyE',
            'elements': [
                {
                    'action_id': '61+q',
                    'text': {
                        'emoji': True,
                        'text': 'Results Page Only',
                        'type': 'plain_text'},
                    'type': 'button',
                    'url': 'book/avoid-climate-disaster/page/CH04-PG29.jpg'
                },
                {
                    'action_id': 'Z470',
                    'text': {
                        'emoji': True,
                        'text': 'Entire Chapter',
                        'type': 'plain_text'},
                    'type': 'button',
                    'url': 'book/avoid-climate-disaster/chapter/CH04.pdf'
                }
            ],
            'type': 'actions'
        }
    ],
    'channel': 'C04BRFKKSNL',
    'text': "This content can't be displayed.",
    'ts': 1668625025.508569,
    'type': 'app_mention',
    'user': 'U045HCSMG8K'
}


def test_component():

    dmo = UserIdExtract()
    assert dmo

    assert dmo.process(d_event) == ['U046G4FURQT']


def main():
    test_component()


if __name__ == '__main__':
    main()
