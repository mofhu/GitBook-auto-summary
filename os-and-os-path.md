# os/os.path for manipulation pathname
# 使用 os/os.path 操作文件路径

## outline

结合自己的需求, 在实际应用中学习 python 的 os/os.path 模块的一些功能.

在这里简述相关功能和应用实例

- 需求
- 实现思路
- 需要的技术和 Python 实现
  - 读取目录 `os.listdir()`
  - 遍历目录 `os.walk()`
  - 判断文件与路径 `os.path.isfile()`, `os.path.isdir()`
  - 合并路径 `os.path.join()`
  - 计算相对路径 `os.path.relpath()`
  - 正则表达式: 判断文件是否是 .md 文件
  - 其它也许有用的函数
- 小结

## 需求

GitBook 使用中, 需要不断更新 SUMMARY.md, GitBook 通过这个文件展示书籍索引.

问题: 不断增加书籍内容时, 经常反复更新 Summary 繁琐耗时, 且可能出错产生错误链接

需求: 能否把 `添加md文件内容和链接到 Summary` 这一过程自动化?

## 实现思路
MVP 版本中, 可实现为读取某个目录下全部 .md文件, 并输出为SUMMARY.md

1. 读取目录下全部文件
2. 逐个匹配是否是有效的 markdown 文件
3. 如是, 则按照 markdown 格式写入文件名和链接到SUMMARY.md

后续版本, 需要搜索目录下的全部子目录, 并正确处理子目录中的文件链接和缩进层次

1. 本质上每层都可以通过 MVP 实现. 问题转化为如何组织这些操作, 并处理缩进层次.
2. **递归**: 传递目录和递归深度, 即可正确实现.

## 需要的技术和 python 实现

### 读取目录 `os.listdir()`
Return a list containing the names of the entries in the directory given by path.  
[`os.listdir()`](https://docs.python.org/3/library/os.html#os.listdir)返回一个列表, 列表中有目录下信息.  
后续可通过遍历列表实现遍历目录

```python
for filename in os.listdir(dire):
    do sth here
```

### 遍历目录 `os.walk()`
Generate the file names in a directory tree by walking the tree either top-down or bottom-up. For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).  
[`os.walk()`](https://docs.python.org/3/library/os.html#os.walk)可用来遍历目录中的每一个子目录, 返回一个三元数组

```python
for root, dirs, files in os.walk(dire):
    do sth here
```

在当前应用中, 为了传递递归深度, 没有使用 os.walk().   
但这个函数对于很多应用比下文提到的手动实现遍历方法更方便.

### 判断文件与路径 `os.path.isdir()`, `os.path.isfile()`
遍历得到列表后, 我们需要判断列表中内容是文件还是目录, 从而决定后续操作.  
os.path 中有几个相关函数: [`os.path.isdir(path)`](https://docs.python.org/3/library/os.path.html#os.path.isdir), [`os.path.isfile(path)`](https://docs.python.org/3/library/os.path.html#os.path.isfile)  
满足条件时返回 True

```python
if os.path.isdir(path)):
    do sth here
```

### 合并路径 os.path.join()
得到列表后, 还需要把路径和文件名合并, 才能得到文件路径.   
在前面的实践(mascot-csv-process)中, 使用了手动添加反斜杠(backslash) '\' 的方法, 在windows下可用.   
但unix下使用的是 slash '/'. 兼容性会成为问题.   
好在 Python 提供了通用函数 [`os.path.join(path, *paths)`](https://docs.python.org/3/library/os.path.html#os.path.join)

```python
if os.path.isdir(os.path.join(dire, filename)):
    do sth here
```

### 传递递归深度
正确缩进要求我们传递递归深度. 把递归深度作为一个变量加入函数. 输出时, 用递归深度计算出缩进量即可.

实现的遍历方式: 
1. 读取全部文件/路径
2. 遍历, 如果是路径: 递归(子路径, 深度 + 1)

### 计算相对路径 `os.path.relpath()`
Summary 输出可用链接时, 需要计算文件和根目录的相对路径.  
[`os.path.relpath(path, start=os.curdir)`](https://docs.python.org/3/library/os.path.html#os.path.relpath) 可实现这一计算

绝对路径可用 [`os.path.realpath(path)`](https://docs.python.org/3/library/os.path.html#os.path.realpath)


### 判断文件是否是 .md 文件
正则 `$`用于从文件末尾匹配后缀, 用 slicing 输出文件名的前面部分.

```python
import re
if re.search('.md$', filename): 
    print(filename, filename[:-3], 'match')
```


### 其它也许有用的函数

[os.path.exists(path)](https://docs.python.org/3/library/os.path.html#os.path.exists)  
后续判断是否已有文件(防止覆盖已有的summary)时, 很可能会用到

[os.path.normpath(path)](https://docs.python.org/3/library/os.path.html#os.path.normpath)  
整理路径格式

[os.path.samefile(path1, path2)](https://docs.python.org/3/library/os.path.html#os.path.samefile)

[os.getcwd()](https://docs.python.org/3/library/os.html#os.getcwd)  
Return a string representing the current working directory. 返回当前工作目录

[os.chdir(path)](https://docs.python.org/3/library/os.html#os.chdir)  
改变工作目录

## 小结

这个可用的 MVP 脚本包括注释仅用不到50行代码.

Python 标准库的功能极其强大, 直接寻找合适的模块使用即可, 和本科时写C代码自己实现完全不同.

---

References

- [Python doc - os](https://docs.python.org/3/library/os.html)
- [Python doc - os.path](https://docs.python.org/3/library/os.path.html)
