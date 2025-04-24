import os
import re
from datetime import datetime

import requests
from PySide2.QtCore import QThread, Signal
from config import proxies

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}


class DownloadThread(QThread):
    log = Signal(str)
    finish = Signal(str)
    progress = Signal(int, int)

    def __init__(self, book_url, download_dir, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.book_url = book_url
        self.download_dir = download_dir

    def run(self):
        self.log.emit("任务开始")
        self.download_smartedu_content()

    def download_smartedu_content(self):
        content_id_match = re.search(r'contentId=([^&]+)', self.book_url)
        if not content_id_match:
            self.log.emit("链接上未获取到contentId，请输入正确的链接")
            return
        self.log.emit("链接解析成功")

        # 获得content_id
        content_id = content_id_match.group(1)
        title_url = f"https://s-file-2.ykt.cbern.com.cn/zxx/ndrv2/resources/tch_material/details/{content_id}.json"
        resp = requests.get(url=title_url, headers=headers, proxies=proxies)

        # 获得教材名称
        title_match = re.search(r'"title"\s*:\s*"([^"]+)"', resp.text)
        if not title_match:
            self.log.emit("解析失败，未获取到教材名称")
            return

        title_obj = title_match.group(1)
        if title_obj:
            title = title_obj.strip()
        else:
            title = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

        # 创建目录
        os.makedirs(self.download_dir, exist_ok=True)
        file_path = os.path.join(self.download_dir, title + ".pdf")

        # 开始下载
        download_url = f"https://r2-ndr.ykt.cbern.com.cn/edu_product/esp/assets/{content_id}.pkg/pdf.pdf"
        self.download_file(download_url, file_path, title)

    def download_file(self, download_url, file_path, title):
        self.log.emit(f"开始下载：{title}.pdf")

        with requests.get(download_url, stream=True, proxies=proxies) as r:
            total_size = int(r.headers.get('content-length', 0))
            with open(file_path, 'wb') as file:
                downloaded = 0
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        # 写入文件
                        file.write(chunk)
                        # 更新进度条
                        downloaded += len(chunk)
                        self.progress.emit(downloaded, total_size)

        # 下载完成
        self.finish.emit(f"下载完成：{title}.pdf")
