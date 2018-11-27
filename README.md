# 前言
一个最近重写的TestDll工具，用于测试Dll劫持。不过某人疯狂（@王小明）打脸说有一个更好的工具rattler，确实更方便更省事，不过在实战测试一些软件的时候，发现自己写的这个工具还是可以作为辅助的。

dll劫持虽然老，但是感觉还可以用于很多地方的，比如用于绕杀毒软件、用于启动项、用于提权，可以看下面的实战。

rattler:https://github.com/sensepost/rattler
TestDll:https://github.com/lufeirider/TestDll

# 用法
将收集到的dll名填入到info.txt中，格式不限定，下面这种也是可以的，因为会通过正则提取正则名。
```c
[*] EXECUTABLE TEST VULNERABLE DLL-> C:\Windows\system32\CRYPTBASE.dll
[*] EXECUTABLE TEST VULNERABLE DLL-> C:\Windows\system32\dbghelp.dll
[*] EXECUTABLE TEST VULNERABLE DLL-> C:\Windows\system32\profapi.dll
[*] EXECUTABLE TEST VULNERABLE DLL-> C:\Windows\system32\dwmapi.dll
```
`python TestDll.py`

然后会分别在test32、test64中生成对应的32位dll，64位dll，这些dll目的就会是会弹窗，比如test32/credssp.dll这个dll当被加载的时候，会弹出credssp.dll。

rattler测出来的dll有的不一定有效，有的能够劫持，但是严重损害了正常功能，所以还需要拿TestDll生成的dll去手动测试下。

# 实战
## 绕杀毒
以迅雷为列，首先使用rattler进行测试迅雷存在劫持的dll，`Rattler_32.exe "C:\Program Files\Thunder Network\Thunder\Program\Thunder.exe" 1`

![](http://image.lufe1.cn/TestDll/1.png)

使用TestDLL生成测试dll，这个用于检测是否能够完好利用，因为有些dll用于比较关键，你提供一个恶意的dll，甚至连主界面都进不去，而有些dll不太重要，影响的功能也不重要。

测试：CRYPTBASE.dll，将放入`C:\Program Files\Thunder Network\Thunder\Program`中，启动迅雷，发现卡在启动界面，主界面进不去。

![](http://image.lufe1.cn/TestDll/2.png)

测试：cscapi.dll，顺利弹窗。
![](http://image.lufe1.cn/TestDll/3.png)

劫持了迅雷有什么用，这个也可以用作于启动项，不过不太通用，不过迅雷的软件证书很有用，是杀软的白名单，拿腾讯管家试一试。

![](http://image.lufe1.cn/TestDll/4.gif)


## 启动项
跟上面的测试步骤一样，不过这次测试的是explorer.exe资源管理器，开机是必定启动它的，所以测试一下是否存在dll劫持用于作为启动项。apphelp.dll可以用于劫持的。

不过有点遗憾的是，大概是2016年测试的很完美，现在再测试的时候，发现某款杀软开始杀了。现在又发现win10平台也不存在劫持了。不过可以找下windows其他的软件。

![](http://image.lufe1.cn/TestDll/5.gif)


## 提权
只要文件权限没有做好，就可以看下服务器上有哪些软件，然后测试一下是否存在dll劫持（检测dll劫持很方便），然后丢个dll，就可以守株待兔了。

## 总结
dll劫持宝刀未老。dll劫持还有什么好玩的思路？
