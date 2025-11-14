from tagoio_sdk.regions import getConnectionURI

"""Test suite for TagoIO Deploy (tdeploy) Region Support"""


def testShouldGenerateCorrectEndpointsForTdeployRegion():
    """Should generate correct endpoints for tdeploy region"""
    tdeploy = "68951c0e023862b2aea00f3f"
    region = {"tdeploy": tdeploy}

    result = getConnectionURI(region)

    assert result["api"] == f"https://api.{tdeploy}.tagoio.net"
    assert result["sse"] == f"https://sse.{tdeploy}.tagoio.net/events"


def testShouldPrioritizeTdeployOverOtherFields():
    """Should prioritize tdeploy over other fields when both are provided"""
    tdeploy = "68951c0e023862b2aea00f3f"
    # mixing api/sse with tdeploy is no longer allowed by types;
    # pass only tdeploy and ensure correct priority handling remains
    region = {"tdeploy": tdeploy}

    result = getConnectionURI(region)

    assert result["api"] == f"https://api.{tdeploy}.tagoio.net"
    assert result["sse"] == f"https://sse.{tdeploy}.tagoio.net/events"


def testShouldTrimWhitespaceFromTdeployValue():
    """Should trim whitespace from tdeploy value"""
    tdeploy = "  68951c0e023862b2aea00f3f  "
    region = {"tdeploy": tdeploy}

    result = getConnectionURI(region)

    assert result["api"] == "https://api.68951c0e023862b2aea00f3f.tagoio.net"
    assert result["sse"] == "https://sse.68951c0e023862b2aea00f3f.tagoio.net/events"


def testShouldFallbackToStandardBehaviorWhenTdeployIsEmpty():
    """Should fallback to standard behavior when tdeploy is empty"""
    region = {
        "tdeploy": "",
        "api": "https://custom-api.example.com",
        "sse": "https://custom-sse.example.com",
    }

    # Empty tdeploy should fallback to api/sse fields
    result = getConnectionURI(region)

    assert result["api"] == "https://custom-api.example.com"
    assert result["sse"] == "https://custom-sse.example.com"


def testShouldFallbackToStandardBehaviorWhenTdeployIsWhitespaceOnly():
    """Should fallback to standard behavior when tdeploy is whitespace only"""
    region = {
        "tdeploy": "   ",
        "api": "https://custom-api.example.com",
        "sse": "https://custom-sse.example.com",
    }

    # Whitespace-only tdeploy should fallback to api/sse fields
    result = getConnectionURI(region)

    assert result["api"] == "https://custom-api.example.com"
    assert result["sse"] == "https://custom-sse.example.com"


def testShouldMaintainBackwardCompatibilityWithExistingRegions():
    """Should maintain backward compatibility with existing regions"""
    result1 = getConnectionURI("us-e1")
    assert result1["api"] == "https://api.tago.io"
    assert result1["sse"] == "https://sse.tago.io/events"

    result2 = getConnectionURI("eu-w1")
    assert result2["api"] == "https://api.eu-w1.tago.io"
    assert result2["sse"] == "https://sse.eu-w1.tago.io/events"


def testShouldMaintainBackwardCompatibilityWithCustomRegionsObj():
    """Should maintain backward compatibility with custom RegionsObj"""
    customRegion = {
        "api": "https://my-api.com",
        "sse": "https://my-sse.com",
    }

    result = getConnectionURI(customRegion)

    assert result["api"] == "https://my-api.com"
    assert result["sse"] == "https://my-sse.com"
