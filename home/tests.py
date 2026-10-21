from django.test import SimpleTestCase

from home.forms import SettingsForm
from home.models import Settings


class SettingsFormTests(SimpleTestCase):
    def test_settings_form_allows_submission_without_hidden_today_field(self):
        form = SettingsForm(
            data={
                "current_AI": "local",
                "AI_name": "openai/gpt-oss-20b",
                "AI_Status": 1,
                "memoryLimit": 6,
                "updateSummary": 12,
                "ANNOUNCEMENT_VERSION": "1.0.0",
                "ANNOUNCEMENT_TEXT": "hello",
                "API_KEY": "",
                "nonrp_system_prompt": "prompt",
                "rp_system_prompt": "prompt",
            },
            instance=Settings(),
        )

        self.assertTrue(form.is_valid(), form.errors.as_json())


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
