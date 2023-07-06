import asyncio
from unittest.mock import MagicMock, patch
import pytest
import aiohttp
from logs import logs

@pytest.mark.asyncio
async def test_logs():
    cont = "container_name"
    name = "container_name"

    # Создаем фейковый объект ответа от сервера
    fake_response = MagicMock()
    fake_response.content = [b"Log line 1\n", b"Log line 2\n"]

    # Создаем фейковый объект сессии
    fake_session = MagicMock()

    # Мокаем класс ClientSession и переопределяем методы
    with patch('logs.aiohttp.ClientSession', return_value=fake_session):
        # Запускаем функцию logs
        await logs(cont, name)

        # Проверяем, что функция ClientSession создана с правильными параметрами
        fake_session.assert_called_once_with(connector=aiohttp.UnixConnector(path="/var/run/docker.sock"))

        # Проверяем, что функция get вызвана с правильным URL
        fake_session.return_value.get.assert_called_once_with(f"http://xx/containers/{cont}/logs?follow=1&stdout=1")

        # Проверяем, что функция print была вызвана с ожидаемыми аргументами
        expected_print_calls = [
            call(name, b"Log line 1\n"),
            call(name, b"Log line 2\n")
        ]
        assert print.call_args_list == expected_print_calls
