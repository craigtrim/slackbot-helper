#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Define Strict Types for the Project """


from typing import Any
from typing import AnyStr
from typing import List
from typing import Dict
from typing import Tuple
from typing import TypedDict


class NormalizedEvent(TypedDict):
    event: Dict
    analysis: Dict
    membership: AnyStr


class IncomingEvent(TypedDict):
    blocks: List
    channel: AnyStr
    team: AnyStr
    text: AnyStr
    ts: AnyStr
    type: AnyStr
    user: AnyStr
