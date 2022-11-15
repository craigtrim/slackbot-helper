#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Display Book Results with both a Chapter and Page in Slack """


from typing import List, Optional

from baseblock import BaseObject


class ChapterAndPageBlock(BaseObject):
    """ Display Book Results with both a Chapter and Page in Slack

    View Sample Output:
        https://github.com/craigtrim/climate-bot/issues/8#issue-1406861717
    """

    def __init__(self):
        """ Change Log

        Created:
            12-Oct-2022
            craigtrim@gmail.com
            *   refactored out of 'app-mention-orchestrator' in pursuit of
                https://github.com/craigtrim/climate-bot/issues/6
        Created:
            20-Oct-2022
            craigtrim@gmail.com
            *   refactored out of 'climate-bot'
        Created:
            15-Nov-2022
            craigtrim@gmail.com
            *   further refactoring in pursuit of
                https://github.com/craigtrim/slackbot-helper/issues/2

        Args:
            web_client (WebClient): an instantiation of the slack client
        """
        BaseObject.__init__(self, __name__)

    def _book_name_text(self,
                        chapter_number: int,
                        book_name: str) -> str:
        """ Format the Provenance Description

        Args:
            chapter_number (int): the chapter number
            book_name (str): the name of the book (label form)

        Returns:
            str: the provenance output
            Sample Output:
                :book: How to Avoid a Climate Disaster Chapter 3:
        """

        # don't want text that says "Chapter 0"
        # the '0' chapter is always the book's Introduction
        if chapter_number == 0:
            return ':book: *#BOOKNAME* Introduction:'.replace(
                "#BOOKNAME", book_name)

        # Use chapter numbers as usual
        return ':book: *#BOOKNAME* Chapter #CHAPTER:'.replace(
            "#BOOKNAME", book_name).replace('#CHAPTER', str(chapter_number))

    @staticmethod
    def _primary_text_only(primary_text: str,
                           book_name_text: str,
                           page_url: str,
                           chapter_url: str) -> list:
        return [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": primary_text
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": book_name_text
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Results Page Only"
                        },
                        "url": page_url
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Entire Chapter"
                        },
                        "url": chapter_url
                    }
                ]
            }
        ]

    @staticmethod
    def _secondary_text(primary_text: str,
                        secondary_text: List[str],
                        page_url: str,
                        chapter_url: str,
                        book_name_text: str) -> str:
        return [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": primary_text
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": secondary_text
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": book_name_text
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Results Page Only"
                        },
                        "url": page_url
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Entire Chapter"
                        },
                        "url": chapter_url
                    }
                ]
            }
        ]

    def process(self,
                primary_text: str,
                secondary_text: Optional[List[str]],
                page_url: str,
                chapter_url: str,
                chapter_number: int,
                book_name: str,
                slack_channel_id: str,
                slack_thread_ts: Optional[str] = None) -> dict:
        """ Entry Point

        Args:
            primary_text (str): the primary output text to display to the user
            secondary_text (Optional[List[str]]): the secondary output text for the user
            page_url (str): the S3 Page URL
            chapter_url (str): the S3 Chapter URL
            chapter_number (int): the chapter number
            book_name (str): the name of the book (label form)
            slack_channel_id (str): the Slack Channel ID
            slack_thread_ts (Optional[str], optional): the Slack Thread timestamp. Defaults to None.

        Returns:
            dict: the display block
        """

        book_name_text = self._book_name_text(
            book_name=book_name,
            chapter_number=chapter_number)

        def decide() -> list:
            if secondary_text and len(secondary_text):
                return self._secondary_text(
                    page_url=page_url,
                    chapter_url=chapter_url,
                    book_name_text=book_name_text,
                    output_text=primary_text,
                    output_text_secondary=secondary_text)

            return self._primary_text_only(
                page_url=page_url,
                chapter_url=chapter_url,
                output_text=primary_text,
                book_name_text=book_name_text)

        blocks = decide()

        d_event_outgoing = {
            'blocks': blocks,
            'channel': slack_channel_id,
            'thread_ts': slack_thread_ts,
        }

        return d_event_outgoing