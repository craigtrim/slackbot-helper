#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from pprint import pprint

from slackbot_helper.core.dmo import UserIdExtract

d_event = {
    'blocks': [
        {
            'block_id': '0qH',
            'text': {
                'text': "I'm unmotivated. <@U045HCSMG8K> What kind of damage does strip mining cause to the environment?",
                'type': 'mrkdwn',
                'verbatim': False
            },
            'type': 'section'
        }
    ],
    'channel': 'C04M19F0JSG',
    'text': "I'm unmotivated. <@U045HCSMG8K> What kind of damage does strip mining cause to the environment?",
    'thread_ts': 1676258041.705079,
    'ts': 1676258044.110549,
    'type': 'app_mention',
    'user': 'U046G4FURQT'
}


def test_component():

    dmo = UserIdExtract()
    assert dmo

    print(dmo.process(d_event))


def main():
    test_component()


if __name__ == '__main__':
    main()
