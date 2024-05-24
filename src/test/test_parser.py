import src.utils.FileParser as FileParser
import pytest

class TestFileParser:
    def test_get_most_common_word_normal_case(self):
        text = "one one two three"
        parser = FileParser.FileParser(text)
        assert parser.get_most_common_word() == "one"

    def test_get_most_common_word_empty_text(self):
        text = ""
        parser = FileParser.FileParser(text)
        with pytest.raises(ValueError):
            parser.get_most_common_word()

    def test_get_most_common_word_single_word(self):
        text = "one"
        parser = FileParser.FileParser(text)
        assert parser.get_most_common_word() == "one"