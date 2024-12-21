from __future__ import annotations

from typing import Any, ClassVar


class APIError(Exception):
    code: ClassVar[int]
    CODES: ClassVar[dict[int, type[APIError]]] = {}

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        APIError.CODES[cls.code] = cls

    @classmethod
    def from_code(cls, code: int, message: str) -> APIError:
        if klass := cls.CODES.get(code):
            return klass(message)

        print(f"NEW ERROR CODE: {code} {message}")
        return cls(message)

    message: str

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return self.message


class PasswordTooShortError(APIError):
    """The password was too short.

    The message can be:
      - Password must be at least 8 characters long.
    """

    code = 3


class BonusNotUnlockedError(APIError):
    """The bonus is not available yet.

    The message can be:
      - Bonus is not unlocked yet.
      - [client_version] 69 < 70
    """

    code = 13


class AuthenticationError(APIError):
    """There was an error while authenticating.

    The message can be:
      - Invalid credentials.
      - Auth token invalid
    """

    code = 16
