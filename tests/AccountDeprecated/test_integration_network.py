from requests_mock.mocker import Mocker

from src.tagoio_sdk.modules.Resources.IntegrationNetwork import Networks
from tests.conftest import mockListNetwork, mockNetworkInfo


def testNetworksMethodListNetworks(
    requests_mock: Mocker, mockListNetwork: mockListNetwork
):
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    :param mockListNetwork is a fixture to return list of NetworkInfo.
    """

    requests_mock.get("https://api.tago.io/integration/network", json=mockListNetwork)

    tokenFake = {"token": "fake_token"}
    response = Networks(params=tokenFake).listNetwork(queryObj={"amount": 100})

    assert response == mockListNetwork["result"]
    assert isinstance(response, list)
    assert isinstance(response[0], dict)


def testNetworksMethodInfo(requests_mock: Mocker, mockNetworkInfo: mockNetworkInfo):
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    :param mockNetworkInfo is a fixture to return the object NetworkInfo.
    """
    networkID = "fake_network_id"
    requests_mock.get(
        f"https://api.tago.io/integration/network/{networkID}", json=mockNetworkInfo
    )

    tokenFake = {"token": "fake_token"}
    response = Networks(params=tokenFake).info(networkID=networkID)

    assert response == mockNetworkInfo["result"]
    assert isinstance(response, dict)
