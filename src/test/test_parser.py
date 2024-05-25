import src.utils.FileParser as FileParser
import pytest

class TestFileParser:
    def test_get_most_common_word_normal_case(self):
        text = "one two two three"
        parser = FileParser.FileParser(text)
        assert parser.get_most_common_word() == ["two"]

    def test_get_most_common_word_empty_text(self):
        text = ""
        parser = FileParser.FileParser(text)
        with pytest.raises(ValueError):
            parser.get_most_common_word()

    def test_get_most_common_word_single_word(self):
        text = "one"
        parser = FileParser.FileParser(text)
        assert parser.get_most_common_word() == ["one"]

    def test_get_most_common_word_multiple_words(self):
        text = "one two three"
        parser = FileParser.FileParser(text)
        assert parser.get_most_common_word() == ["one", "two", "three"]

    def test_get_most_common_word_multiple_most_common(self):
        text = "one one two two three"
        parser = FileParser.FileParser(text)
        assert parser.get_most_common_word() == ["one", "two"]

    def test_sandwich_word_normal_case(self):
        text = "one two two three"
        parser = FileParser.FileParser(text)
        assert parser.sandwich_word(text, ["two"]) == "one footwobar footwobar three"

    def test_sandwich_word_empty_text(self):
        text = ""
        parser = FileParser.FileParser(text)
        with pytest.raises(ValueError):
            parser.sandwich_word("", ["two"])

    def test_sandwich_word_empty_words(self):
        text = "one two two three"
        parser = FileParser.FileParser(text)
        with pytest.raises(ValueError):
            parser.sandwich_word(text, [])