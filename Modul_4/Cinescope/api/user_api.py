# from Modul_4.Cinescope.custom_requester.custom_requester import CustomRequester
# from Modul_4.Cinescope.constants import LOGIN_ENDPOINT, REGISTER_ENDPOINT
#
# class UserAPI(CustomRequester):
#     """
#     Класс для работы с API пользователей.
#     """
#
#     def __init__(self, session):
#         super().__init__(base_url=session.base_url)
#         self.session = session
#
#     def get_user_info(self, user_id, expected_status=200):
#         """
#         Получение информации о пользователе.
#         :param user_id: ID пользователя.
#         :param expected_status: Ожидаемый статус-код.
#         """
#         return self.send_request(
#             method="GET",
#             endpoint=f"/users/{user_id}",
#             expected_status=expected_status
#         )
#
#     def delete_user(self, user_id, expected_status=204):
#         """
#         Удаление пользователя.
#         :param user_id: ID пользователя.
#         :param expected_status: Ожидаемый статус-код.
#         """
#         return self.send_request(
#             method="DELETE",
#             endpoint=f"/users/{user_id}",
#             expected_status=expected_status
#         )
