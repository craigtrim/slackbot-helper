#!/usr/bin/env python
# -*- coding: UTF-8 -*-

""" Transform an Incoming Mention Event """


from typing import Optional
from pprint import pformat

from baseblock import BaseObject, Enforcer

from slackbot_helper.core.dto import IncomingEvent, NormalizedEvent


class TransformIncomingEvent(BaseObject):
    """ Transform an Incoming Mention Event

    TODO: this is a candidate for a slackbot-toolkit MSS
    """

    def __init__(self) -> None:
        """ Change Log

        Created:
            2-May-2022
            craigtrim@gmail.com
            *   refactored out of 'text-bot-orchestrator' in pursuit of
                https://github.com/grafflr/graffl-core/issues/333
        Updated:
            6-Oct-2022
            craigtrim@gmail.com
            *   refactored into 'climate-bot'
        Updated:
            7-Oct-2022
            craigtrim@gmail.com
            *   refactored into 'slackbot-helper'
        Updated:
            12-Feb-2023
            craigtrim@gmail.com
            *   capture thread-ts in normalized event
                https://github.com/craigtrim/slackbot-helper/issues/11
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                d_event: IncomingEvent) -> NormalizedEvent:
        """ Transform and Validate Incoming Event

        Reference:
            https://github.com/grafflr/graffl-core/issues/277#issuecomment-1094148847

        Args:
            d_event (dict): an incoming slack event

        Returns:
            dict: validated slack event
        """

        # # slackbot-helper/issues/11
        def get_thread_ts() -> Optional[float]:
            if 'thread_ts' in d_event:
                return float(d_event['thread_ts'])

        d = {
            'type': d_event['type'],
            'text': d_event['text'],
            'user': d_event['user'],
            'ts': float(d_event['ts']),
            'thread_ts': get_thread_ts(),
            'team': d_event['team'],
            'channel': d_event['channel'],
        }

        # b2b communication does not have 'blocks'
        if 'blocks' in d_event:
            d['blocks'] = d_event['blocks']

        if self.isEnabledForDebug:
            Enforcer.is_str(d['type'])
            Enforcer.is_str(d['text'])
            Enforcer.is_str(d['user'])
            Enforcer.is_float(d['ts'])
            Enforcer.is_optional_float(d['thread_ts'])
            Enforcer.is_str(d['team'])
            Enforcer.is_str(d['channel'])
            if 'blocks' in d:
                Enforcer.is_list(d['blocks'])

        if self.isEnabledForInfo:
            self.logger.info(f'Service Event\n{pformat(d)}')

        return d
