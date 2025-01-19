import pytest
from src import code_mock

# モック化したい関数
def get_json_data_mock(id):
    # モックの戻り値を設定
    return {'name': '宮内　太郎'}

# テスト対象の関数をモンキーパッチでモック化
def test_get_user_name(monkeypatch):
    # モンキーパッチを使ってrequests.getの戻り値をモック化
    monkeypatch.setattr(
        code_mock, 'get_json_data', get_json_data_mock)
    # テスト対象の関数を実行
    result = code_mock.get_user_name([1, 2, 3])
    # テスト結果の検証
    assert result == {1: '宮内　太郎', 2: '宮内　太郎', 3: '宮内　太郎'}

def test_user_name_validation():
    # テスト対象の関数を実行
    # 例外の型を引数に指定して、例外のメッセージを検証
    with pytest.raises(ValueError) as e:
        code_mock.user_name_validation(None)
    assert str(e.value) == '名前が設定されていません'