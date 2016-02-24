from PyQt4.QtCore import QT_VERSION_STR
from PyQt4.pyqtconfig import Configuration
import matplotlib as mpl

print("Qt version:", QT_VERSION_STR)
cfg = Configuration()
print("SIP version:", cfg.sip_version_str)
print("PyQt version:", cfg.pyqt_version_str)
print("matplotlib version:", mpl.__version__)
