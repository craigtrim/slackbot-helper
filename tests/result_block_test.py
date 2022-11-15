#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Standardized API for Dealing with Slack Blocks """


from slackbot_helper import ResultBlock


def test_text_block():

    bp = ResultBlock()
    assert bp

    bp.text_block(
        output_text=None,
        slack_channel_id=None,
        slack_thread_ts=None)

    bp.text_block(
        output_text='Output Text',
        slack_channel_id=None,
        slack_thread_ts=None)

    bp.text_block(
        output_text='Output Text',
        slack_channel_id='ID',
        slack_thread_ts='TS')


def test_book_only():

    bp = ResultBlock()
    assert bp

    bp.book_only(
        primary_text=None,
        secondary_text=None,
        book_url=None,
        book_name='Book Name',
        book_button_text=None,
        slack_channel_id=None,
        slack_thread_ts=None)

    bp.book_only(
        primary_text=None,
        secondary_text='Secondary Text',
        book_url=None,
        book_name='Book Name',
        book_button_text=None,
        slack_channel_id=None,
        slack_thread_ts=None)

    bp.book_only(
        primary_text='Primary Text',
        secondary_text=None,
        book_url=None,
        book_name='Book Name',
        book_button_text=None,
        slack_channel_id=None,
        slack_thread_ts=None)

    bp.book_only(
        primary_text=None,
        secondary_text='Secondary Text',
        book_url=None,
        book_name='Book Name',
        book_button_text=None,
        slack_channel_id=None,
        slack_thread_ts=None)

    bp.book_only(
        primary_text='Primary Text',
        secondary_text='Secondary Text',
        book_url='Book URL',
        book_name='Book Name',
        book_button_text='Book Button Text',
        slack_channel_id='ID',
        slack_thread_ts='TS')


def test_chapter_and_page_block():

    bp = ResultBlock()
    assert bp

    bp.chapter_and_page_block(
        primary_text=None,
        secondary_text=None,
        page_url=None,
        chapter_url=None,
        chapter_number=None,
        book_name='Test Book Name',
        slack_channel_id=None,
        slack_thread_ts=None)

    bp.chapter_and_page_block(
        primary_text=None,
        secondary_text='Secondary Text',
        page_url=None,
        chapter_url=None,
        chapter_number=None,
        book_name='Test Book Name',
        slack_channel_id=None,
        slack_thread_ts=None)

    bp.chapter_and_page_block(
        primary_text='Primary Text',
        secondary_text='Secondary Text',
        page_url=None,
        chapter_url=None,
        chapter_number=None,
        book_name='Test Book Name',
        slack_channel_id=None,
        slack_thread_ts=None)

    bp.chapter_and_page_block(
        primary_text='Primary Text',
        secondary_text=None,
        page_url=None,
        chapter_url=None,
        chapter_number=None,
        book_name='Test Book Name',
        slack_channel_id=None,
        slack_thread_ts=None)

    bp.chapter_and_page_block(
        primary_text='Primary Text',
        secondary_text='Secondary Text',
        page_url='Page URL',
        chapter_url='Chapter URL',
        chapter_number=0,
        book_name='Test Book Name',
        slack_channel_id='ID',
        slack_thread_ts='TS')


def main():
    test_text_block()
    test_book_only()
    test_chapter_and_page_block()


if __name__ == "__main__":
    main()
