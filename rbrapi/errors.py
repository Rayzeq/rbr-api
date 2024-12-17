class APIError(Exception):
    code: int
    message: str

    def __init__(self, code: int, message: str) -> None:
        super().__init__(code, message)
        self.code = code
        self.message = message

    def __str__(self) -> str:
        return self.message


class AuthenticationError(APIError):
    """Exception raised for errors in the authentication process."""


class SignUpError(APIError):
    """Exception raised for errors during the sign-up process."""


class CollectTimedBonusError(APIError):
    """Exception raised for errors in collecting the timed bonus."""


class FriendRequestError(APIError):
    """Exception raised for errors in sending a friend request."""


class LootBoxError(APIError):
    """Exception raised for errors in purchasing a loot box."""


class UnknownUserError(APIError):
    """Exception raised for errors in sending a query to find a user."""
