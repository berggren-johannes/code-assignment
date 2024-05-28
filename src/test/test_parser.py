import src.utils.FileParser as FileParser
import pytest
from unittest.mock import patch

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

    def test_replace_words_normal_case(self):
        text = "one two two three"
        parser = FileParser.FileParser(text)
        assert parser.replace_words() == "one footwobar footwobar three"

    def test_replace_words_empty_text(self):
        text = ""
        parser = FileParser.FileParser(text)
        with pytest.raises(ValueError):
            parser.replace_words()

    @patch.object(FileParser.FileParser, 'get_most_common_word', return_value=[])
    def test_replace_words_empty_words(self, mock_get_most_common_word):
        text = "one two two three"
        parser = FileParser.FileParser(text)
        with pytest.raises(ValueError):
            parser.replace_words()
            
    def test_replace_words_contains_word(self):
        text = "one two two three onetwothree"
        parser = FileParser.FileParser(text)
        assert parser.replace_words() == "one footwobar footwobar three onetwothree"

    def test_get_parsed_normal_case(self):
        text = "one two two three"
        parser = FileParser.FileParser(text)
        assert parser.get_parsed() == "one footwobar footwobar three"
