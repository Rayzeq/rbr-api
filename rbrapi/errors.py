class AuthenticationError(Exception):
    """Exception raised for errors in the authentication process."""


class SignUpError(Exception):
    """Exception raised for errors during the sign-up process."""


class CollectTimedBonusError(Exception):
    """Exception raised for errors in collecting the timed bonus."""


class FriendRequestError(Exception):
    """Exception raised for errors in sending a friend request."""


class LootBoxError(Exception):
    """Exception raised for errors in purchasing a loot box."""


class userNotExistError(Exception):
    """Exception raised for errors in sending a query to find a user."""
