import sys
import time
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QSplashScreen, QMainWindow
from PySide2.QtCore import Qt


if __name__ == "__main__":
    app = QApplication(sys.argv)
    startup_splash = QSplashScreen()
    main_window = QMainWindow()
    main_window.setFixedSize(400, 600)
    startup_splash.setPixmap(QPixmap("./media/ava_splash.png"))
    startup_splash.show()
    app.processEvents()
    time.sleep(0.5)
    startup_splash.setPixmap(QPixmap("./media/ava_splash_1.png"))
    app.processEvents()
    time.sleep(0.5)
    startup_splash.setPixmap(QPixmap("./media/ava_splash_2.png"))
    app.processEvents()
    time.sleep(0.5)
    startup_splash.setPixmap(QPixmap("./media/ava_splash_3.png"))
    app.processEvents()
    time.sleep(2)
    main_window.show()
    startup_splash.finish(main_window)
    sys.exit(app.exec_())
