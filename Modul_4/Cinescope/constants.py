import os

BASE_URL = "https://auth.dev-cinescope.store"
USER_BASE_URL = "https://users.dev-cinescope.store"

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

LOGIN_ENDPOINT = "/login"
REGISTER_ENDPOINT = "/register"
USER_INFO_ENDPOINT = "/users/{user_id}"
DELETE_USER_ENDPOINT = "/users/{user_id}"