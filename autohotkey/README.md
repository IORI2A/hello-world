**搜索： **


**2020-02-15 P1**
1. autohotkey 研究告一段落
2. 归档辅助研究时下载的一些文档资料。

**2020-02-15 P1**
1. [python OpenCV 图片相似度 5种算法](https://blog.csdn.net/enter89/article/details/90293971)
2. pip install requests


**2020-02-13 P1**
1. [Python代码中执行另外一个.py文件](https://blog.csdn.net/sunshinezhihuo/article/details/80942993)


**2020-02-11 P1**
1. [在windows下pywin32模拟鼠标及键盘动作](https://blog.csdn.net/qq_33371343/article/details/78916751)
2. [sup817ch/AutoOnmyoji](https://github.com/sup817ch/AutoOnmyoji/blob/master/game_ctl.py)


**2020-02-10 P1**
1. 基于[基于计算机视觉的梦幻西游辅助脚本（只用于开发学习技术）](https://blog.csdn.net/silent_gods/article/details/89955166)安装相关组件。
- pip install pywin32
  + 网速问题使用迅雷下载安装文件进行安装
  + pip install pywin32-227-cp38-cp38-win32.whl
- pip install Pillow
  + pip install Pillow-7.0.0-cp38-cp38-win32.whl
- pip install pyinstaller
  + 网速问题，且暂不使用该组件。
2. **搜索： opencv python 游戏辅助**
- [python + opencv 实现色弱測試游戏 自动点击游戏外挂](https://blog.csdn.net/u014017080/article/details/76216125)
- [OpenCV图像识别初探-50行代码教机器玩2D游戏](https://blog.csdn.net/devcloud/article/details/94169912)
3. **搜索： opencv python 截屏**
- [python opencv 截图](https://blog.csdn.net/smilife_/article/details/89210638)
  + [使用Python和OpenCV检测图像中的物体并将物体裁剪下来](https://blog.csdn.net/liqiancao/article/details/55670749)
4. **搜索： python log**
- [Python日志库logging总结-可能是目前为止将logging库总结的最好的一篇文章](https://cloud.tencent.com/developer/article/1354396)


**2020-02-09 P2**
1. **搜索： opencv python**
[ex2tron/OpenCV-Python-Tutorial](https://github.com/ex2tron/OpenCV-Python-Tutorial)


**2020-02-09 P1**
1. 总结安装 opencv-python 。
- 安装 python-3.8.1.exe 。
- 通过 pip install 安装相关组件。
  + pip install numpy
  + pip install matplotlib
  + pip install opencv-python
    - 第三方基于官方编译的 opencv-python 模块。
    - opencv_python-4.1.2.30-cp38-cp38-win32.whl
    - 网络不好，太慢，下载安装失败。
    - 单独下载 opencv_python-4.1.2.30-cp38-cp38-win32.whl
    - pip install opencv_python-4.1.2.30-cp38-cp38-win32.whl
2. 验证安装是否成功。
- 验证 python 安装。
  + >python
  + Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
- 验证 numpy 安装。
  + >>> import numpy
  + >>> #print(numpy.__version__)
  + 1.18.1
- 验证 matplotlib 安装。
  + >>> import matplotlib
  + >>> #print(matplotlib.__version__)
  + 3.1.2
- 验证 opencv-python 安装。
  + >>> import cv2
  + >>> #print(cv2.__version__)
  + 4.1.2


**2020-01-14 P1**
1. **搜索： cv2.cp38-win_amd64.pyd**
- [opencv-python · PyPI](https://pypi.org/project/opencv-python/)
  + opencv-python 4.1.2.30
  + pip install opencv-python
    - opencv_python-4.1.2.30-cp38-cp38-win32.whl (24.2MB)
2. [基于计算机视觉的梦幻西游辅助脚本（只用于开发学习技术）](https://blog.csdn.net/silent_gods/article/details/89955166)
- [haungwanjun/mhxy_fz](https://github.com/haungwanjun/mhxy_fz)
- **搜索： python PIL**
  + [PIL - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/897692888725344/966759628285152)
    - PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。
  + [python PIL 图像处理 - 简书](https://www.jianshu.com/p/e8d058767dfa)
    - python里面自带一个PIL（python images library), 但这个库现在已经停止更新了，所以使用Pillow, 它是由PIL发展而来的。
  + [python之PIL库(Image模块) - 噼里巴啦 - 博客园](https://www.cnblogs.com/xiaozx/p/10698852.html)
    - PIL(Python Image Library)是python的第三方图像处理库，PIL的功能非常的强大，几乎被认定是Python的官方图像处理库了。
    - 由于PIL仅支持到python2.7于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，支持最新的python3，而且扩容了很多特性，所以在python3我们可以直接安装Pillow。
    - 我们可以去官网查看它的资料：http://effbot.org/。
- **搜索： python PIL opencv**
  + [图像处理库PIL与OpenCV](https://blog.csdn.net/LYKXHTP/article/details/81837951)
    - Python Imaging Library ，或者叫PIL，简略来说， 是Python图像操作的核心库。不幸的是，它的开发陷入了停滞，最后一次更新是2009年。
      + 幸运的是，存在一个活跃的PIL开发分支，叫做 Pillow 它很容易安装，运行在各个操作系统上，而且支持Python3。
    - OpenCv 是一个在图像操作与处理上比PIL更先进的库。它可以在很多语言上被执行并被广泛使用。
  + [Python-Opencv和PIL读取图像文件的差别](https://oldpan.me/archives/python-opencv-pil-dif)
    - 之前在进行深度学习训练的时候，偶然发现使用PIL读取图片训练的效果要比使用python-opencv读取出来训练的效果稍好一些，也就是训练更容易收敛。
      + 可能的原因是两者读取出来的数据转化为pytorch中Tensor变量稍有不同
- **搜索： pywin32**
  + [Windows平台Python编程必会模块之pywin32](https://www.cnblogs.com/achillis/p/10462585.html)
    - pip install pywin32
  + [mhammond/pywin32](https://github.com/mhammond/pywin32)
  + [pywin32 · PyPI](https://pypi.org/project/pywin32/)
    - pip install pywin32
- **搜索： tkinter**  
  + [Python GUI 编程(Tkinter) | 菜鸟教程](https://www.runoob.com/python/python-gui-tkinter.html)
  + [tkinter — Python interface to Tcl/Tk](https://docs.python.org/3/library/tkinter.html)
  + python 3.8.1 已经自带。
- **搜索： pyinstaller**
  + [PyInstaller Quickstart](http://www.pyinstaller.org/)
- **搜索： from PIL import ImageGrab, Image**
  + [关于from PIL import Image问题](https://blog.csdn.net/qq_33485434/article/details/80422374)
    - [Pillow 7.0.0](https://pypi.org/project/Pillow/)
      + pip install Pillow
    - 如何安装whl文件:
      + 如果将D:\Python27\Scripts目录添加到path中，可以直接在whl文件所在目录用管理员打开一个cmd窗口，直接执行下面的语句。
        - pip install Pillow-4.1.0-cp27-cp27m-win_amd64.whl
      + 否则的话，需要在D:\Python27\Scripts目录下用管理员打开cmd，运行pip命令，文件名应该写全路径）
        - pip install C:\Users\xxx\Downloads\Pillow-4.1.0-cp27-cp27m-win_amd64.whl


**2020-01-13 P1**
1. pip install matplotlib
- 多次安装 Successfully installed cycler-0.10.0 kiwisolver-1.1.0 matplotlib-3.1.2 pyparsing-2.4.6 python-dateutil-2.8.1 six-1.13.0
2. 验证安装是否成功。
- >>> import numpy
- >>> print (numpy.__version__)
- 1.18.1
- >>> import matplotlib
- >>> print (matplotlib.__version__)
- 3.1.2
3. 安装 opencv 到 python 。
- Install OpenCV-Python in Windows
  + Goto opencv/build/python/2.7 folder.
  + Copy cv2.pyd to C:/Python27/lib/site-packages.
- 通过 OpenCV 4.2.0 的文档无法成功执行 import cv2 。
4. **搜索： PyTorch**
- [强推！《PyTorch中文手册》来了](https://baijiahao.baidu.com/s?id=1625418330981941428&wfr=spider&for=pc)
  + PyTorch 是一个深度学习框架，旨在实现简单灵活的实验。
  + PyTorch 现在是 GitHub 上增长速度第二快的开源项目。
  + PyTorch 1.0 增加了一系列强大的新功能，大有赶超深度学习框架老大哥 TensorFlow 之势。


**2020-01-12 P4**
1. 安装配置 OpenCV-Python 环境。
- [Install OpenCV-Python in Windows](https://docs.opencv.org/master/d5/de5/tutorial_py_setup_in_windows.html)
  + [下载 python](https://www.python.org/downloads/)
    - python-3.8.1.exe
	- cmd > python 验证安装。
  + **搜索： Numpy**
    - [NumPy中文网](https://www.numpy.org.cn/)
  + **搜索： Matplotlib**
    - [Matplotlib 中文](https://www.matplotlib.org.cn/)
  + **搜索： pip install**
    - [Python pip 安装与使用 | 菜鸟教程](https://www.runoob.com/w3cnote/python-pip-install-usage.html)
	  + pip 是 Python 包管理工具，该工具提供了对Python 包的查找、下载、安装、卸载的功能。
	  + Python 2.7.9 + 或 Python 3.4+ 以上版本都自带 pip 工具。
	  + pip install numpy
	    - Successfully installed numpy-1.18.1
	  + python -m pip install --upgrade pip
	    - Successfully installed pip-19.3.1
	  + pip install matplotlib
	    - 安装失败。
2. python 学习。
- [A Byte of Python](https://swaroop-c-h.gitbook.io/byte-of-python/)
  + [简明 Python 教程](https://bop.mol.uno/)
  + 在本书撰写的时点，最新版本为 Python 3.5.1
  + 在 Windows 下运行 Python 命令提示符
    - cmd > python
  + 出现了 >>> 。这个被称作 Python 解释器提示符（Python Interpreter Prompt） 。
  + Windows 中按下 [ctrl + z] 组合键并敲击 [enter] 键来退出。
  + 编辑器。
    - 如果你对应从哪开始还没有概念，我推荐你使用 PyCharm 教育版 软件
  + 运行 .py 文件。
    - python xxx.py
  + 要注意 Python 是区分大小写的
  + 需要确保每一行的第一个字符前面都没有任何空格或制表格
  + help('len') 命令——这将显示出有关 len 函数的帮助
  + 变量只需被赋予某一值。不需要声明或定义数据类型。
  + 如果你希望在一行物理行中指定多行逻辑行，那么你必须通过使用分号(;)来明确表明逻辑行或语句的结束。
    - 强烈建议你对于每一行物理行最多只写入一行逻辑行。
  + 如果你有一行非常长的代码，你可以通过使用反斜杠将其拆分成多个物理行。这被称作显式行连接（Explicit Line Joining）
  + 逻辑行以括号开始，它可以是方括号或花括号，但不能是右括号。这被称作 隐式行连接（Implicit Line Joining）。
  + 在逻辑行的开头留下空白区（使用空格或制表符）用以确定各逻辑行的缩进级别，而后者又可用于确定语句的分组。
  + 这意味着放置在一起的语句必须拥有相同的缩进。每一组这样的语句被称为 块（block）。
    - 错误的缩进可能会导致错误。
  + 函数可以通过关键字 def 来定义。
  + 文档字符串（Documentation Strings），在称呼它时通常会使用另一个短一些的名字docstrings。
 

**2020-01-12 P3**
1. **搜索： OpenCV**
- [OpenCV](https://opencv.org/)
2. **搜索： 梦幻西游外挂编程**
- [基于计算机视觉的梦幻西游辅助脚本（只用于开发学习技术）](https://blog.csdn.net/silent_gods/article/details/89955166)
3. **GITHUB 搜索： opencv**
- [opencv/opencv](https://github.com/opencv/opencv)
- [spmallick/learnopencv](https://github.com/spmallick/learnopencv)
4. **搜索： 图片中对象标记**
- [使用tensorflow训练模式识别图片中的对象（object-detection）](https://www.codercto.com/a/26761.html)
  + [tzutalin/labelImg](https://github.com/tzutalin/labelImg)
5. **GITHUB 搜索： opencv label object**
- [peterborkuti/haarselector](https://github.com/peterborkuti/haarselector)
- [kabrau/PyImageRoi](https://github.com/kabrau/PyImageRoi)


**2020-01-12 P2**
1. 推荐使用全屏坐标系。
- 使用窗口坐标系，进行任务点击无效果。
- 可设计一个窗口目标坐标转全屏坐标的转换。
2. AutoHotkey 脚本可不通过热键来触发，而可以直接运行执行。
- ahk 转换为 exe 。如果 ahk 内容是通过热键触发，那么 exe 内容也需要通过热键触发。
- 可以将各种小操作保存主一个个小的 EXE 。后续由逻辑代码来调用执行。
3. 到目前为止算是解决了模拟鼠标输入的问题。


**2020-01-12 P1**
1. MHXY 可使用 Macro Creator 来实现移动点击效果。
- mhxy_mouse_move_click.pmc
2. 将 mhxy_mouse_move_click.pmc 转为 ahk 。通过 ahk 也可以成功运行产生效果。
- mhxy_mouse_move_click.ahk
3. 问题：人物自身坐标确定？点击目标的坐标确定？
- 通过图像搜索获取人物坐标。
4. **搜索： 截屏工具**
- [好用的截图工具有哪些？](https://www.zhihu.com/question/19593742)
5. **搜索： 截屏工具 开源**
- [开源的截图工具](https://www.cnblogs.com/jiftle/p/6654100.html)
- [优秀开源截图工具 Snipaste 2.2.4 + x64 绿色中文版](http://www.dayanzai.me/snipaste.html)
- [开源截屏工具——share X史上最强"开源软件"，11年来一直 ...](http://www.xihahou.net/2019/10/14/c98da4d4f6/)
6. **GITHUB 搜索： Snipaste**
- [Snipaste](https://github.com/Snipaste)
- 未开源源码。
7. **GITHUB 搜索： share x**
- [ShareX/ShareX](https://github.com/ShareX/ShareX)
- C# 实现。
8. **GITHUB 搜索： snipping  tool**
- [pinebit/reverscreen](https://github.com/pinebit/reverscreen)
9. 按键精灵就有截图功能。


**2020-01-11 P1**
1. 使用 Macro Creator 录制一个时间同步的记录。
- 默认是 F9 启动、停止录制，F3 播放录制。
- F9 按下后右下角都会有提示当前情况。注意多次重复按 F9 导致仿佛无操作一般。
2. 将 pmc 转为 ahk 可成功运行。


**2020-01-08 P1**
1. [Pulover's Macro Creator 官网](https://www.macrocreator.com/)
- [Pulover/PuloversMacroCreator](https://github.com/Pulover/PuloversMacroCreator)
- 是基于 AutoHotkey 来实现的。用到 AutoHotkey 来写脚本实现？


**2020-01-06 P1**
1. [AutoHotkey 官网](https://www.autohotkey.com/)
- 下载安装 AutoHotkey_1.1.32.00_setup.exe
2. [AutoHotkey 中文帮助文档](https://wyagd001.github.io/zh-cn/docs/AutoHotkey.htm)
3. 学习 AutoHotkey 的一些辅助。
- [【工具】宏录制和自动化脚本创建](https://zhuanlan.zhihu.com/p/19772251)
  + AutoScriptWriter
  + Pulover's Macro Creator
  + SciTE4AutoHotkey 
- [【工具】Macro Creator 学习资源](https://zhuanlan.zhihu.com/p/19772667)


