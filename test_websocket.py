import pytest
import websocket
import ssl

ENDPOINT = "ws://127.0.0.1:8080/websocket"

@pytest.fixture
def websocket_client():
    if "wss" in ENDPOINT.lower():
        ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
    else:
        ws = websocket.WebSocket()
    ws.connect(ENDPOINT)  # WebSocket server address
    yield ws
    ws.close()

@pytest.mark.repeat(10)  # Run the test 10 times
def test_send_message(websocket_client):
    for num in range(1000):
        message = 'ping' + str(num)
        websocket_client.send(message)  # Send message to WebSocket server
        response = websocket_client.recv()          # Receive response from WebSocket server
        assert response == 'ping' + str(num)  # Verify response