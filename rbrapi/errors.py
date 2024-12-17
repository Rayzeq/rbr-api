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
    """The provided password was too short."""

    code = 3


class InvalidCredentialsError(APIError):
    """A wrong email/password combo was entered."""

    code = 16
