import src.utils.FileParser as FileParser

class TestFileParser:
    def test_get_most_common_word_normal_case(self):
        text = "one one two three"
        parser = FileParser.FileParser(text)
        assert parser.get_most_common_word() == "one"