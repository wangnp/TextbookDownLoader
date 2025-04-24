import base64
import json
import traceback

import requests
from PySide2.QtCore import Qt, QUrl
from PySide2.QtGui import QGuiApplication, QDesktopServices, QPixmap, QIcon
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, \
    QPushButton, QFileDialog, QVBoxLayout, QTextEdit, QHBoxLayout

from threads import DownloadThread
from window import Ui_MainWindow
from config import *


class DisclaimerDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("免责声明")
        self.setFixedSize(400, 300)  # 增加高度，以容纳更多内容
        # 禁用右上角关闭按钮
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        # 始终保持在顶部
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        # 创建界面
        layout = QVBoxLayout()

        # 添加协议文本，使用 QTextEdit
        self.text_edit = QTextEdit(self)
        self.text_edit.setText(privacy_policy)
        self.text_edit.setReadOnly(True)  # 设置为只读
        self.text_edit.setAlignment(Qt.AlignTop)  # 文本从顶部开始显示
        layout.addWidget(self.text_edit)

        # 创建按钮
        button_layout = QHBoxLayout()

        # "同意"按钮
        agree_button = QPushButton("同意")
        agree_button.clicked.connect(self.accept)
        button_layout.addWidget(agree_button)

        # "拒绝"按钮
        decline_button = QPushButton("拒绝")
        decline_button.clicked.connect(self.reject)
        button_layout.addWidget(decline_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.setModal(True)  # 设置为模态对话框

    def closeEvent(self, event):
        # 禁止关闭窗口的事件，必须通过按钮来关闭
        event.ignore()


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 添加点击信号
        self.text_log.anchorClicked.connect(lambda url: QDesktopServices.openUrl(url))

        # 绑定事件
        self.btn_select_dir.clicked.connect(self.event_click_select_dir)
        self.btn_download.clicked.connect(self.event_click_download)
        self.action_mianze.triggered.connect(self.show_disclaimer)

        # 设置全局异常钩子
        sys.excepthook = self.global_exception_handler
        self.comment_thread = None

        # 显示主窗口
        self.show()
        # 弹出免责声明
        configData = getUserConfig(user_config_file)
        if not configData.get("agreed"):
            self.show_disclaimer()

        # 初始化ui
        self.init_ui()

    def init_ui(self):
        # 加载图标
        icon_data = base64.b64decode(image_data["fav.ico"])
        pixmap = QPixmap()
        pixmap.loadFromData(icon_data)
        icon = QIcon(pixmap)
        self.setWindowIcon(icon)

        # 加载默认路径
        self.text_download_dir.setText(f"{base_path}\\下载")

        # 获取公告
        # applicationInfo = getApplicationInfo()
        # if applicationInfo:
        #     applicationData = applicationInfo["data"]
        #     announcement = applicationData["announcement"]
        #     version = float(applicationData["version"])
        #     status = applicationData["status"]
        #
        #     self.text_log.append(announcement)
        #
        #     if not status:
        #         QMessageBox.warning(self, "错误", "应用已关闭")
        #         sys.exit(0)
        #
        #     if version > curr_version:
        #         QMessageBox.warning(self, "请更新版本", f"发现新版本{version}，请前往【公众号：程序员王哪跑】进行更新...")
        # else:
            # 携带默认的
        self.text_log.append("""
        <b>更多原创软件，请关注公众号：程序员王哪跑</b><br>""")
        self.text_log.append("----------------------------------------------------")

    def global_exception_handler(self, exc_type, exc_value, exc_traceback):
        error_message = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        self.text_log.append(f"出现异常，请反馈给作者: {error_message}")
        self.btn_start_comment.setEnabled(True)
        self.btn_start_comment.setText("开始")

    def mouse_press(self, event):
        """自定义鼠标点击事件处理"""
        if event.button() == Qt.LeftButton:
            # 获取点击位置的锚点（链接）
            anchor = self.text_log.anchorAt(event.pos())
            if anchor:
                QDesktopServices.openUrl(QUrl(anchor))
                return

        # 如果不是点击链接，调用原始的鼠标事件处理
        QTextEdit.mousePressEvent(self.text_log, event)

    def show_disclaimer(self):
        # 创建并显示免责声明对话框
        self.disclaimer_dialog = DisclaimerDialog()
        if self.disclaimer_dialog.exec() == QDialog.Rejected:
            saveUserConfig(user_config_file, {"privacy_policy": privacy_policy, "agreed": False})
            QMessageBox.warning(None, "提示", "您必须接受条款才能使用本软件。")
            sys.exit(0)
        # 同意结果：存入用户目录
        saveUserConfig(user_config_file, {"privacy_policy": privacy_policy, "agreed": True})

    def event_click_download(self):
        book_url = self.text_book_url.text()
        download_dir = self.text_download_dir.text()

        if not book_url:
            QMessageBox.warning(self, "警告", "请输入教材链接")
            return

        if not download_dir:
            QMessageBox.warning(self, "警告", "请选择下载目录")
            return

        if "basic.smartedu.cn" not in book_url:  # 判断是否为第二种下载链接
            QMessageBox.warning(self, "警告", "请输入正确的链接地址")
            return

        thread = DownloadThread(book_url, download_dir, self)
        thread.log.connect(self.log_callback)
        thread.finish.connect(self.finish_callback)
        thread.progress.connect(self.progress_callback)
        thread.start()

    def progress_callback(self, downloaded, total_size):
        if total_size > 0:
            progress = (downloaded / total_size) * 100
            self.progressBar.setValue(progress)
            size_mb = downloaded / (1024 * 1024)
            total_mb = total_size / (1024 * 1024)
            self.label_progress.setText(f"下载中: {size_mb:.2f}MB / {total_mb:.2f}MB ({progress:.1f}%)")

    def log_callback(self, msg):
        self.text_log.append(msg)

    def finish_callback(self, msg):
        self.text_log.append(msg)
        self.label_progress.setText("下载完成")
        self.text_log.append("---------------------------------------")

    def event_click_select_dir(self):
        """
        选择文件
        :return:
        """
        # 打开文件夹选择对话框
        dir_path = QFileDialog.getExistingDirectory(self, '选择路径')

        # 如果选择了文件夹，将其路径显示在标签中
        if dir_path:
            self.text_download_dir.setText(dir_path)


def saveUserConfig(file_path, data: dict):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def getUserConfig(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    return {}


def getApplicationInfo():
    try:
        resp = requests.get(f"{api_url}/app/info?appid={app_id}", timeout=10, proxies=proxies)
        return resp.json()
    except:
        pass
    return None


if __name__ == '__main__':
    QGuiApplication.setAttribute(Qt.AA_EnableHighDpiScaling) # 启用高DPI缩放（适配Qt 5）
    QGuiApplication.setAttribute(Qt.AA_UseHighDpiPixmaps) # 使用高DPI图像资源

    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())

    # nuitka main.py --output-filename=电子课本下载器.exe --mingw64 --onefile --standalone --windows-disable-console --plugin-enable=pyside2 --windows-icon-from-ico=logo.png

    # pyinstaller -w -F main.py -n 电子课本下载器 -i logo.png
