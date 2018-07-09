# sierraDynamicWallpaper
sierra仿majave动态壁纸

### [使用python脚本实现自动切换壁纸](https://github.com/welljun06/sierraDynamicWallpaper.git)

步骤

1. 下载majave.py文件

2. 下载mojave_dynamic.zip图片在电脑本地解压

3. 将majave.py文件的localpath变量改为放置图片的路径

4. 设置定时任务, 每隔一个钟自动执行python脚本任务

   - 这里使用的是`crontab`指令，先通过`sudo crontab -e`进入设置界面
   - 键入i进入编辑模式，输入下面代码，其中前面`0 */1 * * *`代表时间设置，python后面的路径为本地存放majave.py的路径，可以先在终端输入`python /Users/welljun06/script/majove.py`查看是否执行脚本。

   ```shell
   0 */1 * * * python /Users/welljun06/script/majove.py
   ```

   - 设置好之后通过`sudo crontab -l`来查看设置内容

5. 设置成功

```python
import datetime
import subprocess

cmd = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

ISOTIMEFORMAT = '%H'
theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
print theTime

if int(theTime) < 8 and int(theTime) >= 6:
    index = 0
elif int(theTime) >=0 and int(theTime) < 6:
    index = 16
else:
    index = int(theTime) - 7

localpath = "/Users/welljun06/Pictures/mojave_dynamic/mojave_dynamic_{0}.jpeg".format(index)
try:
    subprocess.Popen(cmd%localpath, shell=True)
#    subprocess.call(["killall Dock"], shell=True)
except KeyboardInterrupt:
    print "The Computer says NO!"
```

### todo:

- 设置根据地理信息来进行调整图片
- 可以考虑增加更多图片