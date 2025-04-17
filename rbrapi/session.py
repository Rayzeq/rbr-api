from __future__ import annotations

from datetime import UTC, datetime
from threading import local
from typing import Any

import requests

from .errors import APIError

# Session time-to-live in seconds
SESSION_TIME_TO_LIVE = 600

# Thread-local storage for session and creation time
thread_local = local()


def get_session(*, reset: bool = False) -> requests.session.Session:
    """Return or create a requests session, reset if expired."""
    if not hasattr(thread_local, "session") or reset:
        thread_local.session = requests.sessions.Session()
        thread_local.creation_time = datetime.now(UTC)

    if (
        SESSION_TIME_TO_LIVE
        and (datetime.now(UTC) - thread_local.creation_time).total_seconds()
        > SESSION_TIME_TO_LIVE
    ):
        thread_local.session = requests.sessions.Session()
        thread_local.creation_time = datetime.now(UTC)

    return thread_local.session


def make_request(
    url: str,
    headers: dict[str, str] | None = None,
    json: dict[str, Any] | None = None,
    data: str | None = None,
    timeout: int | None = None,
    method: str = "POST",
) -> dict[str, Any]:
    session = get_session()

    if method == "POST":
        response = session.post(
            url,
            timeout=timeout,
            headers=headers,
            json=json,
            data=data,
        )
    else:
        response = session.get(
            url,
            timeout=timeout,
            headers=headers,
            json=json,
            data=data,
        )

    try:
        if not response.ok:
            response = response.json()
            raise APIError.from_code(response["code"], response["message"])

        return response.json()
    except requests.exceptions.JSONDecodeError:
        raise APIError(response.text) from None
