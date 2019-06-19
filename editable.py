import os
import platform


def editabledate(pathToFile):
    if platform.system() == 'Windows':
        return os.path.getmtime(pathToFile)
    else:
        stat = os.stat(pathToFile)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime
