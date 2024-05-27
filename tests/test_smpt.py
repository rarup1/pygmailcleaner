import os
import sys
import pytest # type: ignore
from unittest.mock import Mock, patch

sys.path.append("./")
from pygmailcleaner.utils import SMPTClient

TRASH_FOLDER = os.getenv("TRASH_FOLDER", '"[Google Mail]/Trash"')

# Sample test data
SERVER = "smtp.gmail.com"
PORT = 993
USER = "test@gmail.com"
PASSWORD = "testpassword"


@pytest.fixture
def smpt_client():
    return SMPTClient(SERVER, PORT, USER, PASSWORD)


@pytest.fixture
def imaplib_mock():
    with patch("imaplib.IMAP4_SSL") as mock:
        yield mock


class TestSMPTClient:

    def test_connect(self, smpt_client, imaplib_mock):
        smpt_client.connect()
        imaplib_mock.assert_called_once_with(SERVER, PORT)
        imaplib_mock.return_value.login.assert_called_once_with(USER, PASSWORD)
        imaplib_mock.return_value.select.assert_called_once()

    def test_close(self, smpt_client):
        smpt_client.imap = Mock()
        smpt_client.close()
        smpt_client.imap.close.assert_called_once()
        smpt_client.imap.logout.assert_called_once()

    def test_get_msg_ids(self, smpt_client):
        smpt_client.imap = Mock()
        smpt_client.imap.search.return_value = ("OK", [b"1 2 3 4"])
        method = "delete_unread"
        date_until = "2023-01-01"
        msg_ids = smpt_client.get_msg_ids(method, date_until)
        assert msg_ids == "1,2,3,4"

    def test_count_msgs(self, smpt_client):
        assert smpt_client.count_msgs("1,2,3,4") == 4
        assert smpt_client.count_msgs("") == 0

    def test_delete_msgs(self, smpt_client):
        smpt_client.imap = Mock()
        smpt_client.imap.expunge.return_value = ("OK",)
        smpt_client.delete_msgs("1,2,3,4")
        assert smpt_client.imap.store.call_count == 2
        smpt_client.imap.select.assert_called_with(TRASH_FOLDER)
        smpt_client.imap.expunge.assert_called_once()
