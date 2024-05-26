import pytest
from unittest.mock import patch
import sys

sys.path.append("./")
from pygmailcleaner.utils import YesNoQuestionHandler, DateQuestionHandler


@pytest.fixture
def yes_no_handler():
    return YesNoQuestionHandler(
        [{"description": "Test question 1"}, {"description": "Test question 2"}]
    )


@pytest.fixture
def date_handler():
    return DateQuestionHandler("Please enter a date:")


@patch("builtins.input")
class TestQuestionHandlers:

    def test_yes_no_question_handler_with_yes(self, mocked_input, yes_no_handler):
        mocked_input.side_effect = ["y", "n"]
        yes_no_handler.run()
        assert yes_no_handler.values == ["y", "n"]

    def test_date_question_handler_valid_date(self, mocked_input, date_handler):
        mocked_input.side_effect = ["2023-01-01"]
        date_handler.run()
        assert date_handler.values == "2023-01-01"

    def test_validate_date_format_valid(self, mocked_input):
        assert DateQuestionHandler.validate_date_format("2023-01-01") is True

    def test_validate_date_format_invalid(self, mocked_input):
        assert DateQuestionHandler.validate_date_format("2023-01-0122") is False
