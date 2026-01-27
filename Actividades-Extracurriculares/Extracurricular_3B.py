import logging
import requests
from logging.handlers import RotatingFileHandler
from colorlog import ColoredFormatter

# =======================
# CONFIG TELEGRAM
# =======================
TELEGRAM_TOKEN = "TU_BOT_TOKEN"
CHAT_ID = "TU_CHAT_ID"

class TelegramHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": log_entry
        }
        try:
            requests.post(url, json=payload, timeout=5)
        except Exception:
            pass  # Evita que el logging rompa el programa

# =======================
# LOGGER PRINCIPAL
# =======================
logger = logging.getLogger("MiLogger")
logger.setLevel(logging.DEBUG)

# =======================
# FORMATO GENERAL
# =======================
log_format = (
    "%(asctime)s | %(levelname)-8s | "
    "%(filename)s:%(lineno)d | %(message)s"
)

date_format = "%Y-%m-%d %H:%M:%S"

# =======================
# HANDLER CONSOLA (COLORES)
# =======================
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

color_formatter = ColoredFormatter(
    "%(log_color)s" + log_format,
    datefmt=date_format,
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    }
)

console_handler.setFormatter(color_formatter)

# =======================
# HANDLER ARCHIVO
# =======================
file_handler = RotatingFileHandler(
    "app.log",
    maxBytes=1_000_000,
    backupCount=3,
    encoding="utf-8"
)
file_handler.setLevel(logging.INFO)

file_formatter = logging.Formatter(
    log_format,
    datefmt=date_format
)
file_handler.setFormatter(file_formatter)

# =======================
# HANDLER TELEGRAM
# =======================
telegram_handler = TelegramHandler()
telegram_handler.setLevel(logging.ERROR)
telegram_handler.setFormatter(file_formatter)

# =======================
# REGISTRAR HANDLERS
# =======================
logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.addHandler(telegram_handler)

# =======================
# PRUEBAS
# =======================
logger.debug("Mensaje de depuración")
logger.info("Aplicación iniciada correctamente")
logger.warning("Advertencia: uso elevado de memoria")
logger.error("Error crítico en el módulo de pagos")
logger.critical("FALLO TOTAL DEL SISTEMA")
