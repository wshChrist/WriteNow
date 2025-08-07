import threading

import keyboard
import language_tool_python


class AutoCorrector:
    """Listen to keyboard events and autocorrect words on the fly."""

    def __init__(self) -> None:
        self.tool = language_tool_python.LanguageTool('fr')
        self.buffer = []
        self.sending = False
        keyboard.hook(self._handle_event)

    def _handle_event(self, event) -> None:
        if self.sending or event.event_type != 'down':
            return
        key = event.name
        if key == 'space' or key in {'.', ',', ';', '?', '!', 'enter'}:
            self.buffer.append(' ')
            self._apply_correction()
            self.buffer = []
        elif key == 'backspace':
            if self.buffer:
                self.buffer.pop()
        elif len(key) == 1:
            self.buffer.append(key)

    def _apply_correction(self) -> None:
        text = ''.join(self.buffer)
        matches = self.tool.check(text)
        corrected = language_tool_python.utils.correct(text, matches)
        if corrected != text:
            self.sending = True
            for _ in text:
                keyboard.send('backspace')
            keyboard.write(corrected)
            self.sending = False


if __name__ == '__main__':
    AutoCorrector()
    threading.Event().wait()
