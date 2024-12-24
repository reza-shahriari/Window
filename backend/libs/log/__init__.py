import logging
import sys

log = logging.getLogger(name="AUTORENT")
log.setLevel(level=logging.DEBUG)

datefmt = "%Y-%m-%dT%H:%M:%S%z"  # ISO 8601
fmt = logging.Formatter(
    fmt='%(asctime)s:%(name)s:%(levelname)s:%(message)s',
    datefmt=datefmt,
)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(fmt=fmt)
log.addHandler(hdlr=handler)
