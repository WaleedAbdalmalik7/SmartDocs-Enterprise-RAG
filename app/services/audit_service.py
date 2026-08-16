"""Simple audit/event logging for actions."""
import logging

logger = logging.getLogger("smartdocs.audit")


def log_event(event: str, **data):
    logger.info("%s %s", event, data)
