import os
from requests_mock.mocker import Mocker

from tagoio_sdk.modules.Resources.Resources import Resources
from tagoio_sdk.modules.Resources.Dictionaries_Types import DictionaryInfo, LanguageData

os.environ["T_ANALYSIS_TOKEN"] = "your_token_value"


def mockDictionaryList() -> list[DictionaryInfo]:
    return {
        "status": True,
        "result": [
            {
                "id": "dictionary_id_1",
                "name": "Dictionary 1",
                "slug": "DICT1",
                "fallback": "en-US",
                "languages": [
                    {"code": "en-US", "active": True},
                    {"code": "pt-BR", "active": True},
                ],
                "created_at": "2023-02-21T15:17:35.759Z",
                "updated_at": "2023-02-21T15:17:35.759Z",
            },
            {
                "id": "dictionary_id_2",
                "name": "Dictionary 2",
                "slug": "DICT2",
                "fallback": "en-US",
                "languages": [{"code": "en-US", "active": True}],
                "created_at": "2023-02-21T16:17:35.759Z",
                "updated_at": "2023-02-21T16:17:35.759Z",
            },
        ],
    }


def mockDictionaryInfo() -> DictionaryInfo:
    return {
        "status": True,
        "result": {
            "id": "dictionary_id_1",
            "name": "Dictionary 1",
            "slug": "DICT1",
            "fallback": "en-US",
            "languages": [
                {"code": "en-US", "active": True},
                {"code": "pt-BR", "active": True},
            ],
            "created_at": "2023-02-21T15:17:35.759Z",
            "updated_at": "2023-02-21T15:17:35.759Z",
        },
    }


def mockLanguageInfo() -> LanguageData:
    return {
        "status": True,
        "result": {
            "HELLO": "Hello",
            "GOODBYE": "Goodbye",
            "WELCOME": "Welcome $0",
        },
    }


def mockCreateDictionary() -> dict:
    return {
        "status": True,
        "result": {"dictionary": "dictionary_id_new"},
    }


def testDictionariesMethodList(requests_mock: Mocker) -> None:
    """Test list method of Dictionaries class."""
    mock_response = mockDictionaryList()
    requests_mock.get("https://api.tago.io/dictionary", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    query = {
        "page": 1,
        "fields": ["id", "name", "slug", "languages"],
        "amount": 20,
        "orderBy": ["name", "asc"],
    }

    result = resources.dictionaries.list(query)

    # Check if the result is a list
    assert isinstance(result, list)
    # Check if the result has the expected items
    assert len(result) == 2
    # Check if items have expected properties
    assert result[0]["id"] == "dictionary_id_1"
    assert result[1]["id"] == "dictionary_id_2"
    assert result[0]["slug"] == "DICT1"
    assert result[1]["slug"] == "DICT2"
    assert len(result[0]["languages"]) == 2
    assert len(result[1]["languages"]) == 1


def testDictionariesMethodCreate(requests_mock: Mocker) -> None:
    """Test create method of Dictionaries class."""
    mock_response = mockCreateDictionary()
    requests_mock.post("https://api.tago.io/dictionary", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    dictionary_data = {
        "name": "New Dictionary",
        "slug": "NEWDICT",
        "fallback": "en-US",
    }

    result = resources.dictionaries.create(dictionary_data)

    # Check if result has expected structure
    assert result["dictionary"] == "dictionary_id_new"


def testDictionariesMethodEdit(requests_mock: Mocker) -> None:
    """Test edit method of Dictionaries class."""
    mock_response = {
        "status": True,
        "result": "Successfully Updated",
    }

    requests_mock.put("https://api.tago.io/dictionary/dictionary_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    dictionary_data = {
        "name": "Updated Dictionary Name",
    }

    result = resources.dictionaries.edit("dictionary_id_1", dictionary_data)

    # Check if result has expected message
    assert result == "Successfully Updated"


def testDictionariesMethodDelete(requests_mock: Mocker) -> None:
    """Test delete method of Dictionaries class."""
    mock_response = {
        "status": True,
        "result": "Successfully Removed",
    }

    requests_mock.delete("https://api.tago.io/dictionary/dictionary_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.dictionaries.delete("dictionary_id_1")

    # Check if result has expected message
    assert result == "Successfully Removed"


def testDictionariesMethodInfo(requests_mock: Mocker) -> None:
    """Test info method of Dictionaries class."""
    mock_response = mockDictionaryInfo()
    requests_mock.get("https://api.tago.io/dictionary/dictionary_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.dictionaries.info("dictionary_id_1")

    # Check if result has expected properties
    assert result["id"] == "dictionary_id_1"
    assert result["name"] == "Dictionary 1"
    assert result["slug"] == "DICT1"
    assert len(result["languages"]) == 2
    assert result["languages"][0]["code"] == "en-US"
    assert result["languages"][1]["code"] == "pt-BR"


def testDictionariesMethodLanguageEdit(requests_mock: Mocker) -> None:
    """Test languageEdit method of Dictionaries class."""
    mock_response = {
        "status": True,
        "result": "Dictionary language Successfully Updated",
    }

    requests_mock.put("https://api.tago.io/dictionary/dictionary_id_1/en-US", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    language_data = {
        "dictionary": {"HELLO": "Hello", "GOODBYE": "Goodbye"},
        "active": True,
    }

    result = resources.dictionaries.languageEdit("dictionary_id_1", "en-US", language_data)

    # Check if result has expected message
    assert result == "Dictionary language Successfully Updated"


def testDictionariesMethodLanguageDelete(requests_mock: Mocker) -> None:
    """Test languageDelete method of Dictionaries class."""
    mock_response = {
        "status": True,
        "result": "Successfully Removed",
    }

    requests_mock.delete("https://api.tago.io/dictionary/dictionary_id_1/pt-BR", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.dictionaries.languageDelete("dictionary_id_1", "pt-BR")

    # Check if result has expected message
    assert result == "Successfully Removed"


def testDictionariesMethodLanguageInfo(requests_mock: Mocker) -> None:
    """Test languageInfo method of Dictionaries class."""
    mock_response = mockLanguageInfo()
    requests_mock.get("https://api.tago.io/dictionary/dictionary_id_1/en-US?fallback=False", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.dictionaries.languageInfo("dictionary_id_1", "en-US")

    # Check if result has expected properties
    assert "HELLO" in result
    assert "GOODBYE" in result
    assert "WELCOME" in result
    assert result["HELLO"] == "Hello"
    assert result["WELCOME"] == "Welcome $0"


def testDictionariesMethodLanguageInfoWithFallback(requests_mock: Mocker) -> None:
    """Test languageInfo method of Dictionaries class with fallback parameter."""
    mock_response = mockLanguageInfo()
    requests_mock.get("https://api.tago.io/dictionary/dictionary_id_1/en-US?fallback=True", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.dictionaries.languageInfo("dictionary_id_1", "en-US", {"fallback": True})

    # Check if result has expected properties
    assert "HELLO" in result
    assert "GOODBYE" in result
    assert result["HELLO"] == "Hello"


def testDictionariesMethodLanguageInfoBySlug(requests_mock: Mocker) -> None:
    """Test languageInfoBySlug method of Dictionaries class."""
    mock_response = mockLanguageInfo()
    requests_mock.get("https://api.tago.io/dictionary/DICT1/en-US?fallback=True", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.dictionaries.languageInfoBySlug("DICT1", "en-US")

    # Check if result has expected properties
    assert "HELLO" in result
    assert "GOODBYE" in result
    assert result["HELLO"] == "Hello"


def testDictionariesMethodLanguageInfoBySlugWithoutFallback(requests_mock: Mocker) -> None:
    """Test languageInfoBySlug method of Dictionaries class without fallback."""
    mock_response = mockLanguageInfo()
    requests_mock.get("https://api.tago.io/dictionary/DICT1/en-US?fallback=False", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.dictionaries.languageInfoBySlug("DICT1", "en-US", {"fallback": False})

    # Check if result has expected properties
    assert "HELLO" in result
    assert "GOODBYE" in result
    assert result["HELLO"] == "Hello"
