import pytest
from unittest.mock import MagicMock, patch
import binascii
import sample  # sample.py をテスト対象とする

# Type3Tagのモック
class MockType3Tag:
    TYPE = "Type3Tag"
    idm = b"\x01\x23\x45\x67\x89\xab\xcd\xef"  # サンプルIDm

# Type4Tagのモック
class MockType4Tag:
    TYPE = "Type4Tag"
    identifier = b"\xde\xad\xbe\xef"  # サンプルUID

@pytest.fixture
def mock_contactless_frontend():
    """nfc.ContactlessFrontend をモック化"""
    with patch("nfc.ContactlessFrontend") as mock_clf:
        yield mock_clf

def test_on_connect_type3tag(capsys):
    """Type3Tag のIDmを正しく取得できるかテスト"""
    tag = MockType3Tag()
    sample.on_connect(tag)
    captured = capsys.readouterr()
    assert "IDm (Type3Tag): 0123456789abcdef" in captured.out

def test_on_connect_type4tag(capsys):
    """Type4Tag のUIDを正しく取得できるかテスト"""
    tag = MockType4Tag()
    sample.on_connect(tag)
    captured = capsys.readouterr()
    assert "UID (Type4Tag): deadbeef" in captured.out

def test_main(mock_contactless_frontend, capsys):
    """main関数の動作をテスト"""
    # MockType3Tag を接続時の動作に設定
    mock_clf_instance = mock_contactless_frontend.return_value
    mock_clf_instance.connect.return_value = MockType3Tag()

    # main関数の実行
    sample.main()

    # 標準出力を検証
    captured = capsys.readouterr()
    assert "リーダーを待機中..." in captured.out
    assert "IDm (Type3Tag): 0123456789abcdef" in captured.out
