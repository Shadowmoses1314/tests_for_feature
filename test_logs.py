import pytest
import httpx

from logs_func import logs

@pytest.mark.asyncio
async def test_logs():
    cont = '92b52be58081'
    name = 'docker_back'

    # Create mock data
    mock_content = [b'log 1\n', b'log 2\n', b'log 3\n']

    # Create mock response
    mock_response = httpx.Response(200, content=mock_content)

    # Setup mock transport
    mock_transport = httpx.MockTransport(responses=[mock_response])

    # Start function
    async with httpx.AsyncClient(transport=mock_transport) as client:
        await logs(cont, name, client)

    # Check request
    request = mock_transport.await_request()
    assert request.url == f'http://xx/containers/{cont}/logs?follow=1&stdout=1'

    # Check content iteration
    assert mock_response.iter_raw.call_count == 3
    mock_response.iter_raw.assert_called_with(decode_content=False)
