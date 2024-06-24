import logging
from enum import Enum


class LogType(Enum):
    ERROR = "[ERROR]"
    INFO = "[INFO]"
    WARNING = "[WARNING]"


def console_logs(info_text: str, log_type: LogType):
    logger = logging.getLogger(__name__)
    output = f"{log_type.value} {info_text}"
    if log_type == LogType.INFO:
        logger.info(output)
    elif log_type == LogType.ERROR:
        logger.error(output)

