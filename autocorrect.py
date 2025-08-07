import threading

import keyboard
from spellchecker import SpellChecker


class AutoCorrector:
    """Listen to keyboard events and autocorrect words on the fly."""

    def __init__(self) -> None:
        self.spell = SpellChecker(language="fr")
        self.buffer = []
        self.sending = False
        self.just_corrected = False
        self.skip_once = False
        keyboard.hook(self._handle_event)

    def _handle_event(self, event) -> None:
        if self.sending or event.event_type != "down":
            return
        key = event.name
        if key == "space":
            if self.skip_once:
                self.skip_once = False
                self.buffer = []
                return
            self._apply_correction()
            self.buffer = []
        elif key == "backspace":
            if self.just_corrected:
                self.skip_once = True
                self.just_corrected = False
            elif self.buffer:
                self.buffer.pop()
        elif len(key) == 1:
            self.buffer.append(key)

    def _apply_correction(self) -> None:
        word = "".join(self.buffer)
        if not word:
            return
        corrected = self.spell.correction(word)
        if corrected and corrected != word:
            self.sending = True
            for _ in range(len(word) + 1):  # remove word and trailing space
                keyboard.send("backspace")
            keyboard.write(corrected + " ")
            self.sending = False
            self.just_corrected = True
        else:
            self.just_corrected = False


if __name__ == '__main__':
    AutoCorrector()
    threading.Event().wait()
