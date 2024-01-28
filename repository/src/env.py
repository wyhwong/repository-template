import os


# For logger
LOGLEVEL = int(os.getenv("LOGLEVEL", "10"))
LOGFILE_PATH = os.getenv("LOGFILE_PATH", "../runtime.log")

TZ = os.getenv("TZ", "Asia/Hong_Kong")
