import json
import requests
import logging
import os

class CustomRequester:
    """
    Кастомный реквестер для стандартизации и упрощения отправки HTTP-запросов.
    """

    base_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    def __init__(self, session: object, base_url: object) -> object:
        """
        Инициализация кастомного реквестера.
        :param session: Объект requests.Session.
        :param base_url: Базовый URL API.
        """
        self.base_url = base_url
        self.session = session #
        self.headers = self.base_headers.copy()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    def send_request(self, method, endpoint, data=None, params=None, headers=None, expected_status=None,
                     need_logging=True):
        """
        Универсальный метод для отправки запросов.
        :param method: HTTP метод (GET, POST, PUT, DELETE и т.д.).
        :param endpoint: Эндпоинт (например, "/login").
        :param data: Тело запроса (JSON-данные).
        :param params: Параметры запроса для методов типа GET.
        :param headers: Дополнительные заголовки.
        :param expected_status: Ожидаемые статус-коды (может быть числом или списком).
        :param need_logging: Флаг для логирования (по умолчанию True).
        :return: Объект ответа requests.Response.
        """
        url = f"{self.base_url}{endpoint}"
        request_headers = {**self.headers, **(headers or {})}

        response = requests.request(
            method=method,
            url=url,
            json=data,
            params=params,
            headers=request_headers
        )

        if need_logging:
            self.log_request_and_response(response)

        # Если expected_status не задан, используем стандартные успешные статусы
        if expected_status is None:
            expected_status = [200, 201, 204]

        # Если передан один код, превращаем его в список
        if isinstance(expected_status, int):
            expected_status = [expected_status]

        if response.status_code not in expected_status:
            raise ValueError(f"Unexpected status code: {response.status_code}. Expected one of: {expected_status}")

        return response

    def _update_session_headers(self, session, **kwargs):
        """
        Обновление заголовков сессии.
        :param session: Объект requests.Session, предоставленный API-классом.
        :param kwargs: Дополнительные заголовки.
        """
        self.headers.update(kwargs)  # Обновляем базовые заголовки
        session.headers.update(self.headers)  # Обновляем заголовки в текущей сессии


    def log_request_and_response(self, response):
        """
        Логирование запросов и ответов.
        :param response: Объект ответа requests.Response.
        """
        try:
            request = response.request
            GREEN = '\033[32m'
            RED = '\033[31m'
            RESET = '\033[0m'
            headers = " \\\n".join([f"-H '{header}: {value}'" for header, value in request.headers.items()])
            full_test_name = f"pytest {os.environ.get('PYTEST_CURRENT_TEST', '').replace(' (call)', '')}"

            body = ""
            if hasattr(request, 'body') and request.body is not None:
                if isinstance(request.body, bytes):
                    body = request.body.decode('utf-8')
                body = f"-d '{body}' \n" if body != '{}' else ''

            # Логируем запрос
            self.logger.info(f"\n{'=' * 40} REQUEST {'=' * 40}")
            self.logger.info(
                f"{GREEN}{full_test_name}{RESET}\n"
                f"curl -X {request.method} '{request.url}' \\\n"
                f"{headers} \\\n"
                f"{body}"
            )

            # Обрабатываем ответ
            response_status = response.status_code
            is_success = response.ok
            response_data = response.text

            # Попытка форматировать JSON
            try:
                response_data = json.dumps(json.loads(response.text), indent=4, ensure_ascii=False)
            except json.JSONDecodeError:
                pass  # Оставляем текст, если это не JSON

            # Логируем ответ
            self.logger.info(f"\n{'=' * 40} RESPONSE {'=' * 40}")
            if not is_success:
                self.logger.info(
                    f"\tSTATUS_CODE: {RED}{response_status}{RESET}\n"
                    f"\tDATA: {RED}{response_data}{RESET}"
                )
            else:
                self.logger.info(
                    f"\tSTATUS_CODE: {GREEN}{response_status}{RESET}\n"
                    f"\tDATA:\n{response_data}"
                )
            self.logger.info(f"{'=' * 80}\n")
        except Exception as e:
            self.logger.error(f"\nLogging failed: {type(e)} - {e}")