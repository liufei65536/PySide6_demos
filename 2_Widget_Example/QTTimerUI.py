from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QProgressBar, QPushButton, QVBoxLayout, QLabel)
from PySide6.QtCore import QTimer, Qt, Slot
import sys

# -------------------------- 主窗口类（定时器+UI+任务逻辑一体化）--------------------------
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init_timer()  # 初始化定时器

    def initUI(self):
        self.setWindowTitle("定时器实现后台更新 UI 示例")
        self.resize(400, 200)

        # UI 控件（和原线程版完全一致）
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)  # 进度条范围 0-100
        self.status_label = QLabel("就绪状态")
        self.start_btn = QPushButton("启动后台任务")
        self.start_btn.clicked.connect(self.start_task)  # 绑定按钮点击事件

        # 布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.status_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.start_btn)

    def init_timer(self):
        # 创建定时器（核心组件）
        self.task_timer = QTimer(self)
        # 设置定时器触发间隔：50ms（和原线程版 time.sleep(0.05) 一致）
        self.task_timer.setInterval(50)
        # 定时器触发时，执行任务的一小步
        self.task_timer.timeout.connect(self.do_task_step)
        # 初始化进度计数器（记录当前进度）
        self.current_progress = 0

    def start_task(self):
        # 1. 重置状态（进度、UI、定时器）
        self.current_progress = 0
        self.progress_bar.setValue(0)
        self.status_label.setText("任务执行中...")
        self.start_btn.setEnabled(False)  # 禁用按钮，防止重复启动

        # 2. 启动定时器（开始“分段执行”任务）
        self.task_timer.start()

    @Slot()
    def do_task_step(self):
        """定时器每次触发时执行的“任务小步”（运行在主线程，但不阻塞UI）"""
        # 1. 执行当前步任务（原线程版的耗时操作，这里拆成101步，每步50ms）
        # （如果是真实耗时任务，这里写单次计算/单次网络请求等小粒度操作）

        # 2. 进度推进
        self.current_progress += 1

        # 3. 更新UI（直接更新，因为定时器回调本身就在主线程）
        self.progress_bar.setValue(self.current_progress)
        self.status_label.setText(f"进度：{self.current_progress}%")

        # 4. 任务完成判断（进度达到100%时停止定时器）
        if self.current_progress >= 100:
            self.task_timer.stop()  # 停止定时器，结束任务
            self.status_label.setText("后台任务执行完成！")
            self.start_btn.setEnabled(True)  # 恢复按钮可用

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())