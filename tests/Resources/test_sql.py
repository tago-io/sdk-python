import os

from requests_mock.mocker import Mocker

from tagoio_sdk.modules.Resources.Resources import Resources


os.environ["T_ANALYSIS_TOKEN"] = "your_token_value"

QUERY_ROW = {
    "id": "sql-id-123",
    "name": "Latest temperature",
    "tags": [{"key": "audience", "value": "dashboard"}],
    "session_context": True,
    "created_at": "2026-07-01T12:00:00.000Z",
    "updated_at": "2026-07-02T12:00:00.000Z",
}

EXECUTE_RESULT = {
    "columns": [
        {"name": "variable", "type": "string"},
        {"name": "value", "type": "number"},
    ],
    "rows": [{"variable": "temperature", "value": 41.2}],
    "row_count": 1,
    "execution_ms": 12,
    "served_from_cache": False,
}


def testSqlMethodList(requests_mock: Mocker) -> None:
    requests_mock.get(
        "https://api.tago.io/sql", json={"status": True, "result": [QUERY_ROW]}
    )

    resources = Resources({"token": "your_token_value"})
    result = resources.sql.list(
        {"page": 1, "fields": ["id", "name", "tags"], "amount": 20}
    )

    assert isinstance(result, list)
    assert result[0]["id"] == "sql-id-123"
    assert result[0]["session_context"] is True


def testSqlMethodCreate(requests_mock: Mocker) -> None:
    requests_mock.post(
        "https://api.tago.io/sql", json={"status": True, "result": QUERY_ROW}
    )

    resources = Resources({"token": "your_token_value"})
    result = resources.sql.create(
        {
            "name": "Latest temperature",
            "query": "SELECT variable, value FROM device($1) AS d LIMIT 10",
            "params": [{"key": "$1", "value": "my-device-id"}],
        }
    )

    assert result["id"] == "sql-id-123"


def testSqlMethodInfo(requests_mock: Mocker) -> None:
    requests_mock.get(
        "https://api.tago.io/sql/sql-id-123", json={"status": True, "result": QUERY_ROW}
    )

    resources = Resources({"token": "your_token_value"})
    result = resources.sql.info("sql-id-123")

    assert result["name"] == "Latest temperature"
    assert result["session_context"] is True


def testSqlMethodEdit(requests_mock: Mocker) -> None:
    requests_mock.put(
        "https://api.tago.io/sql/sql-id-123", json={"status": True, "result": QUERY_ROW}
    )

    resources = Resources({"token": "your_token_value"})
    result = resources.sql.edit("sql-id-123", {"name": "Latest temperature"})

    assert result["id"] == "sql-id-123"


def testSqlMethodDelete(requests_mock: Mocker) -> None:
    requests_mock.delete(
        "https://api.tago.io/sql/sql-id-123",
        json={"status": True, "result": {"id": "sql-id-123"}},
    )

    resources = Resources({"token": "your_token_value"})
    result = resources.sql.delete("sql-id-123")

    assert result == {"id": "sql-id-123"}


def testSqlMethodGetVersion(requests_mock: Mocker) -> None:
    requests_mock.get(
        "https://api.tago.io/sql/sql-id-123/version/1",
        json={
            "status": True,
            "result": {
                "query": "SELECT 1",
                "params": [],
                "created_at": "2026-07-01T12:00:00.000Z",
            },
        },
    )

    resources = Resources({"token": "your_token_value"})
    result = resources.sql.getVersion("sql-id-123", 1)

    assert result["query"] == "SELECT 1"


def testSqlMethodExecute(requests_mock: Mocker) -> None:
    requests_mock.post(
        "https://api.tago.io/sql/sql-id-123/execute",
        json={"status": True, "result": EXECUTE_RESULT},
    )

    resources = Resources({"token": "your_token_value"})
    result = resources.sql.execute(
        "sql-id-123", {"params": [{"key": "$1", "value": "my-device-id"}]}
    )

    assert result["row_count"] == 1
    assert result["served_from_cache"] is False


def testSqlMethodTables(requests_mock: Mocker) -> None:
    requests_mock.get(
        "https://api.tago.io/sql/tables",
        json={
            "status": True,
            "result": {
                "tables": [
                    {"function": "device", "label": "Device Data", "columns": []}
                ],
                "resources": {"devices": [], "entities": []},
                "functions": [
                    {
                        "name": "count",
                        "kind": "aggregate",
                        "args": ["column"],
                        "description": "Row count",
                    },
                    {
                        "name": "session_user_tag",
                        "kind": "session",
                        "args": ["key"],
                        "description": "The executing user's value for a tag key, filled by the server",
                        "example": "COALESCE(session_user_tag('key'), '...')",
                    },
                ],
            },
        },
    )

    resources = Resources({"token": "your_token_value"})
    result = resources.sql.tables({"filter": "sensor"})

    assert result["tables"][0]["function"] == "device"
    assert result["functions"][0]["name"] == "count"
    assert result["functions"][1]["kind"] == "session"
    assert "COALESCE" in result["functions"][1]["example"]
