#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Standardized API for Dealing with Slack Blocks """


from typing import List, Optional

from baseblock import BaseObject

from slackbot_helper.blocks.dmo import (BookOnlyBlock, ChapterAndPageBlock,
                                        StandardTextBlock)


class ResultBlock(BaseObject):
    """ Standardized API for Dealing with Slack Blocks """

    def __init__(self):
        """ Change Log

        Created:
            15-Nov-2022
            craigtrim@gmail.com
            *   created in pursuit of
                https://github.com/craigtrim/slackbot-helper/issues/2
        """
        BaseObject.__init__(self, __name__)
        self._book_only = BookOnlyBlock().process
        self._chapter_and_page_block = ChapterAndPageBlock().process
        self._standard_text_block = StandardTextBlock()

    def text_block(self,
                   output_text: str,
                   slack_channel_id: str,
                   slack_thread_ts: Optional[str] = None) -> dict:
        """ Create a Standard Text Block

        Args:
            output_text (str): the outgoing slack message
            slack_channel_id (str): the Slack Channel ID
            slack_thread_ts (Optional[str], optional): the Slack Thread timestamp. Defaults to None.

        Returns:
            dict: the display block
        """
        return self._standard_text_block(
            output_text=output_text,
            slack_channel_id=slack_channel_id,
            slack_thread_ts=slack_thread_ts)

    def book_only(self,
                  primary_text: str,
                  secondary_text: Optional[List[str]],
                  book_url: str,
                  book_name: str,
                  book_button_text: str,
                  slack_channel_id: str,
                  slack_thread_ts: Optional[str] = None) -> dict:
        """ Create a Slack Block with a Book Reference Only

        Args:
            primary_text (str): the primary output text to display to the user
            secondary_text (Optional[List[str]]): the secondary output text for the user
            book_url (str): the S3 Chapter URL
            book_name (str): the name of the book (label form)
            book_button_text (str): the name to display on the button
            slack_channel_id (str): the Slack Channel ID
            slack_thread_ts (Optional[str], optional): the Slack Thread timestamp. Defaults to None.

        Returns:
            dict: the display block
        """
        return self._book_only(
            primary_text=primary_text,
            secondary_text=secondary_text,
            book_url=book_url,
            book_name=book_name,
            book_button_text=book_button_text,
            slack_channel_id=slack_channel_id,
            slack_thread_ts=slack_thread_ts)

    def chapter_and_page_block(self,
                               primary_text: str,
                               secondary_text: Optional[List[str]],
                               page_url: str,
                               chapter_url: str,
                               chapter_number: int,
                               book_name: str,
                               slack_channel_id: str,
                               slack_thread_ts: Optional[str] = None) -> dict:
        """ Create a Slack Block with a Chapter and Page Reference

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
        return self._chapter_and_page_block(
            primary_text=primary_text,
            secondary_text=secondary_text,
            page_url=page_url,
            chapter_url=chapter_url,
            chapter_number=chapter_number,
            book_name=book_name,
            slack_channel_id=slack_channel_id,
            slack_thread_ts=slack_thread_ts)