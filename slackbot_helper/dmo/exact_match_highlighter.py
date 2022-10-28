#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Highlight the Portion of the Output Text that corresponds to the User Input Text """


from typing import Optional

from baseblock import BaseObject, TextUtils
from fast_sentence_tokenize import tokenize_text


class ExactMatchHighlighter(BaseObject):
    """ Highlight the Portion of the Output Text that corresponds to the User Input Text """

    def __init__(self):
        """ Change Log

        Created:
            28-Oct-2022
            craigtrim@gmail.com
            *   refactored out of 'highlight-output-text'
        """
        BaseObject.__init__(self, __name__)

    def process(self,
                text_1: str,
                text_2: str) -> Optional[str]:
        """ Entry Point

        Args:
            text_1 (str): the baseline text string
            text_2 (str): the text string to modify (highlight)

        Returns:
            Optional[str]: a highlighted string (if any)
        """

        tokens_1 = tokenize_text(text_1.lower())
        tokens_2 = tokenize_text(text_2.lower())

        common_tokens = TextUtils.longest_common_phrase(
            tokens_1=tokens_1,
            tokens_2=tokens_2)

        if not common_tokens:
            return None

        common_phrase = ' '.join(common_tokens).strip().lower()
        text_2_lower = text_2.lower()

        if common_phrase not in text_2_lower:
            if self.isEnabledForWarning:
                self.logger.warning('\n'.join([
                    f"Common Phrase Not Found in Text 2",
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
