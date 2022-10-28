#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Highlight the Portion of the Output Text that generally corresponds to the User Input Text """


from typing import List, Optional, Text

from baseblock import BaseObject, TextUtils
from fast_sentence_tokenize import tokenize_text


class FuzzyMatchHighlighter(BaseObject):
    """ Highlight the Portion of the Output Text that generally corresponds to the User Input Text """

    def __init__(self):
        """ Change Log

        Created:
            28-Oct-2022
            craigtrim@gmail.com
            *   refactored out of 'highlight-output-text'
        """
        BaseObject.__init__(self, __name__)

    @staticmethod
    # TODO: baseblock >= 0.1.34
    def most_similar_phrase(tokens_1: List[str],
                            tokens_2: List[str],
                            window_size: int,
                            score_threshold: float,
                            debug: bool = False) -> dict:
        """ Find the Most Similar Phrase in Tokens-2 relative to Tokens-1

        Implementation Note:
            How is this different from 'longest-common-phrase'?

            In the example below, there are no common sequences between tokens-1 and tokens-2
            This function will find "nearly similar" sequences and return the most similar

        Args:
            tokens_1 (list): the first tokenized list
                ['where', 'is', 'the', 'library', '?']
            tokens_2 (list): the second tokenized list
                ['I', 'understand', 'you', 'want', 'to', 'know', 'where', 'the', 'library', 'is', '.']
            window_size (int, Optional): n-Gram window size for comparison.
            score_threshold (float): when threshold is met, return the results (if any)
            debug (bool, Optional): When True, print results to console. default is False.

        Returns:
            the most similar span (list) with similarity score
        """

        tokens_1 = [x.lower().strip() for x in tokens_1]
        tokens_2 = [x.lower().strip() for x in tokens_2]

        t1 = TextUtils.sliding_window(
            tokens_1,
            window_size=window_size)

        t2 = TextUtils.sliding_window(
            tokens_2,
            window_size=window_size)

        d_results = {}

        for item_1 in [' '.join(x) for x in t1]:
            for item_2 in [' '.join(x) for x in t2]:

                if item_1 == item_2:
                    return {100: {"tokens_1": item_1, "tokens_2": item_2}}

                score = TextUtils.jaccard_similarity(item_1, item_2)
                if debug:
                    print(f"({item_1}) vs. ({item_2}) = {score}")

                if score >= score_threshold:
                    d_results[score] = {"tokens_1": item_1, "tokens_2": item_2}

        return d_results

    def _most_similar_phrase(self,
                             tokens_1: List[str],
                             tokens_2: List[str]) -> Optional[dict]:

        def high_score(some_d_results: dict) -> dict:
            score = max(list(some_d_results.keys()))
            return some_d_results[score]

        i = 5
        while i >= 3:

            results = FuzzyMatchHighlighter.most_similar_phrase(
                tokens_1=tokens_1,
                tokens_2=tokens_2,
                window_size=i,
                score_threshold=0.75,
                debug=False)

            if results and len(results):
                return high_score(results)

            i -= 1

    def process(self,
                tokens_1: List[str],
                tokens_2: List[str],
                text_2: str) -> Optional[str]:
        """ Entry Point

        Args:
            tokens_1 (str): the tokenized form of text-1
            tokens_2 (str): the tokenized form of text-2
            text_2 (str): the text string to modify (highlight)

        Returns:
            Optional[str]: a highlighted string (if any)
        """

        d_similar = self._most_similar_phrase(
            tokens_1=tokens_1,
            tokens_2=tokens_2)

        if not d_similar or not len(d_similar):
            return None

        common_phrase = ' '.join(d_similar['tokens_2']).strip().lower()
        text_2_lower = text_2.lower()

        if common_phrase not in text_2_lower:
            if self.isEnabledForWarning:
                self.logger.warning('\n'.join([
                    "Common Phrase Not Found in Text 2",
                    f"\tCommon Phrase: {common_phrase}",
                    f"\tText 2: {text_2_lower}"]))
            return None

        x = text_2_lower.index(common_phrase)
        y = x + len(common_phrase)

        start = text_2[:x]
        mid = f"*{text_2[x:y]}*"
        end = text_2[y:]

        final = f"{start} {mid} {end}"
        while '  ' in final:
            final = final.replace('  ', ' ').strip()

        return final
