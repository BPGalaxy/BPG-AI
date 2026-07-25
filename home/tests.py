from django.test import SimpleTestCase

from home.views import _build_base_text


class BuildBaseTextTests(SimpleTestCase):
    def test_build_base_text_uses_summary_and_conversation_context(self):
        system_instructions = "SYSTEM"
        messages_before = [
            ("user message", "hello"),
            ("ai message", "hi"),
        ]

        base_text = _build_base_text(system_instructions, messages_before, "conversation summary", 1)

        self.assertIn("SYSTEM", base_text)
        self.assertIn("conversation summary", base_text)
        self.assertIn("hello", base_text)
        self.assertIn("hi", base_text)
