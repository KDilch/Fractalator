import appdirs
from logging import Formatter

APP_NAME = "Fractalator"
AUTHOR = "Klaudia Dilcher <klaudia.dilcher@gmail.com>"
VERSION = "0.1"
LICENCE = "GNU"

APP_DIRS = appdirs.AppDirs(APP_NAME, AUTHOR)
LOG_FILE_NAME = 'Fractalator.log'
LOG_FORMATTER = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', '%H:%M:%S')
