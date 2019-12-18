**CURRENT**
```
向特定的窗口发送鼠标点击消息。

模仿实现类似任务管理器功能，可以查找到目标游戏程序。
```

**TODO**
```
后续日志记录功能可考虑替换使用LOG4CPP。

日志除输出到文件外也可输出到控制台窗口。

程序启动隐藏，非完美隐藏。
```

# 游戏辅助程序开发。

## MH 

## 开发日志记录 （倒序） 

**2019-12-16**
1. 转换到使用 VS 2010 。
- 方便低配置电脑也可编辑运行工程。
2. 保留 .sln 文件。
- 开发中可能会集不少调试性的工程。

**2019-12-16**
1. 可通过窗口标题来查找匹配的窗口，获取取句柄。
- FindWindow 的 lpWindowName 来指定窗口的标题文体(title) 。
2. Tool 中实现简化获取 Windows 函数执行后的 Last Error。 以字符串返回，同时返回错误码 支持ASNI 和 UNICODE 。
3. 在项目属性中配置引用的头文件的所在目录位置： 配置属性 > C/C++ > 常规 > 附加包含目录 。以简化 #include 语句的编写。

**2019-12-14**
1. 实现程序启动隐藏。
- **搜索： VC windows 窗口隐藏**
  + [VC窗口启动时隐藏](https://blog.csdn.net/jonathanlin2008/article/details/4237657)
- **搜索：  高仿QQ新闻右下角弹窗效果图**
  + [高仿QQ右下角新闻弹窗之MFC版](http://www.voidcn.com/article/p-tfhwakkh-ep.html)
    - [fusijie/Win32-MFC_Popup_Window](https://github.com/fusijie/Win32-MFC_Popup_Window)
- 已经有一个演示系统托盘的工程。
  + **搜索： CSystemTray**
    - 该工程来自 [Adding Icons to the System Tray](https://www.codeguru.com/cpp/com-tech/shell/icons/article.php/c1335/Adding-Icons-to-the-System-Tray.htm)
    - 其他可参考：
      + 好像是同一个人的 codeproject 上的升级版 [Adding Icons to the System Tray](https://www.codeproject.com/articles/74/adding-icons-to-the-system-tray)
  + **搜索： SystemTray SystemTrayDemo**
    - [DEMO: Windows System Tray Icons](https://community.microfocus.com/t5/Net-Express-Server-Express/DEMO-Windows-System-Tray-Icons/ta-p/1743059)
- 创建非模态对话框，可自由控制显示、隐藏。
  + 完善程序退出前的窗口销毁及删除窗口C++对象。
  + 有一个闪烁现象，且目前实现无法再显示窗口，后续也就没有办法交互了。
  + 任务管理器中可见。
- **搜索： PostNcDestroy **
  + [DestroyWindow](https://www.cnblogs.com/findumars/p/5870466.html)
    - 假设自己通过new创建了一个窗口对象pWnd，然后pWnd->Create。则销毁窗口的调用次序：
      + 手工调用pWnd->DestroyWindow()；
      + DestroyWindow会发送WM_DESTROY；
      + WM_DESTROY对应的消息处理函数是OnDestroy()；
      + DestroyWindow会发送WM_NCDESTROY；
      + WM_NCDESTROY对应的消息处理函数是OnNcDestroy；
      + OnNcDestroy最后会调用PostNcDestroy；
      + PostNcDestroy经常被用户重载以提供释放内存操作。例如可以使用delete this（delete this 时再调用析构函数）；
    - 通过这种方式，窗口对象对应的窗口和窗口对象本身都被释放了。
2. 构建一个命令行脚本 删除不需要归档的文件。
 
**2019-12-11**
1. 集成日志记录功能，便于进行调试分析。
- 先使用自己创建的日志工具TOOL。同时在使用中方便改进该工具。
- LOG4CPP 可丰产品较为成熟时或者想学习 LOG4CPP 时考虑使用。
- 先只考虑输出内容到文件。输出到控制台窗口后续再完善。



