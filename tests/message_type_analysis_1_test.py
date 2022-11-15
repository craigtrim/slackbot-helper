#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from pprint import pprint

from slackbot_helper.core.dmo import MessageTypeAnalysis


def test_component():

    dmo = MessageTypeAnalysis(
        user_ids=[],
        bot_ids=["U045HCSMG8K", "U046G4FURQT"],
        message_text="How do fish ladders help mitigate the effects of dams on fish populations?")

    assert dmo

    d_result = dmo.process()
    pprint(d_result)
    assert d_result


def main():
    test_component()


if __name__ == "__main__":
    main()
