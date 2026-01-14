from contextlib import contextmanager
from typing import Generator, Any, Dict
import json
from flask import request, abort

from src.database import get_session


def get_json_or_400() -> Dict[str, Any]:
    # try normal JSON parsing (respects Content-Type)
    data = None
    try:
        data = request.get_json(silent=True)
    except Exception:
        data = None

    # if not parsed, try to parse raw body (handles missing/wrong Content-Type)
    if data is None:
        raw = request.get_data(as_text=True)
        if raw:
            try:
                data = json.loads(raw)
            except Exception:
                abort(400, description="JSON inválido ou ausente")
        else:
            abort(400, description="JSON inválido ou ausente")

    return data


@contextmanager
def session_scope():
    session = get_session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
