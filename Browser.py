from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QToolBar, QToolButton, QAction, QTabWidget, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtCore import QUrl


class Browser(QMainWindow):
    def __init__(self, start):
        super().__init__()

        if start == "":
            self.home = "http://www.google.com"
        else:
            self.home = start
        self.setWindowTitle("Browser")
        self.setGeometry(300, 200, 800, 600)

        self.browser = QWebEngineView()

        self.showMaximized()

        self.setCentralWidget(self.browser)

        """tabs = QTabWidget()
        tab1 = QWidget()
        tab2 = QWidget()
        tabs.addTab(tab1, "Tab 1")
        tabs.addTab(tab2, "Tab 2")
        self.layout().addWidget(tabs)"""


        navBar = QToolBar()
        navBar.setMovable(False)
        self.addToolBar(navBar)

        backBtn = QAction('Back', self)
        backBtn.triggered.connect(self.browser.back)
        navBar.addAction(backBtn)

        forwardBtn = QAction('Forward', self)
        forwardBtn.triggered.connect(self.browser.forward)
        navBar.addAction(forwardBtn)

        homeBtn = QAction('Home', self)
        homeBtn.triggered.connect(self.goHome)
        navBar.addAction(homeBtn)

        self.urlBar = QLineEdit()
        self.urlBar.returnPressed.connect(self.loadUrl)
        self.urlBar.mousePressEvent = self.selectAllText
        navBar.addWidget(self.urlBar)

        reloadBtn = QAction('Reload', self)
        reloadBtn.triggered.connect(self.browser.reload)
        navBar.addAction(reloadBtn)

        self.goHome()
        self.browser.urlChanged.connect(self.updateUrl)

    def loadUrl(self):
        input = self.urlBar.text().strip()
        if not input:
            self.browser.setUrl(QUrl("http://www.google.com"))
            return
        if "." in input or input.startswith(("http://", "https://")):
            if not input.startswith(("http://", "https://")):
                input = "http://" + input
            url = QUrl(input)
        else:
            url = QUrl("http://www.google.com/search?q=" + input)
        if url.isValid():
            self.browser.setUrl(url)

    def updateUrl(self, url):
        self.urlBar.setText(url.toString())

    def selectAllText(self, event):
        self.urlBar.selectAll()

    def goHome(self):
        self.browser.setUrl(QUrl(self.home))
