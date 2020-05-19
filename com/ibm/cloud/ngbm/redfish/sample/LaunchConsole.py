from com.ibm.cloud.ngbm.redfish.manage.Power import Power
from com.ibm.cloud.ngbm.redfish.manage.Console import Console
import com.ibm.cloud.ngbm.redfish as rf
from PyQt5 import QtCore, QtWidgets, QtNetwork, QtWebEngineWidgets


def set_ssl_protocol():
    default_config = QtNetwork.QSslConfiguration.defaultConfiguration()
    default_config.setProtocol(QtNetwork.QSsl.TlsV1_2)
    QtNetwork.QSslConfiguration.setDefaultConfiguration(default_config)


class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
    def certificateError(self, certificateError):
        return True

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.webView = QtWebEngineWidgets.QWebEngineView()
        self.setCentralWidget(self.webView)
        page = WebEnginePage(self)
        self.webView.setPage(page)
        page.load(QtCore.QUrl(url))
        self.setFixedSize(1200, 1200)



if __name__ == "__main__":
    import sys

    print("WAITING FOR SERVER TO POWERON##################################")
    power: Power = Power()
    power.connectRedfish()
    while power.isPowerOn() != True:
        print("Waiting for power to turn on.")
    power.disconnectRedfish()
    print("SERVER IS POWERED ON##################################\n")

    print("CONNECTING REDFISH VIRTUAL MEDIA CLIENT##################################")
    console: Console = Console()
    console.connectRedfish()
    print("CONNECTED: " + str(console.isConnectedRedfish()))

    print("GETTING CONSOLE###########################")
    url = rf.target+console.getConsoleURI()

    print("Connecting to: "+url)
    app = QtWidgets.QApplication(sys.argv)
    set_ssl_protocol()
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
