# GitBook-auto-summary

Automatically update SUMMARY.md of a GitBook repo

自动输出 GitBook 目录的 SUMMARY.md 文件.

By [Frank-the-Obscure @ GitHub](https://github.com/Frank-the-Obscure)

Tested with Python 3.4.3 in Windows 7 and OS 10.10


# Usage

1. `$ python gitbook-auto-summary.py GitBook_repo_root`
2. The auto summary file `SUMMARY-GitBook-auto-summary.md` will be created under the same directory.
  - Markdown links of `[filename](file link)` will be created by default.
  - Files is sorted from files a-z, then folders a-z
3. Advanced: using parameters
  - Use `-a` or `--append` to append new markdown files. **Link name in former SUMMARY.md will not be changed**. This is very useful when appending new file to an existing summary.
  - Use `-o` or `--overwrite` to overwrite on SUMMARY.md. You MUST take care before overwriting!

---

1. 运行`$ python gitbook-auto-summary.py GitBook_repo_root`
2. 脚本将自动在同一个目录生成 `SUMMARY-GitBook-auto-summary.md` 
  - 默认 link 为 `[filename](file link)` 
  - 排序方式为按文件名 a-z, 随后是文件夹名 a-z, 只有含有 markdown 文件的文件夹会被输出
3. 高级用法: 使用参数
  - `-a` or `--append` 添加新文件. **已有的文件链接名称不会被修改**. 这一参数在你修改过某些链接名称后, 只想添加新文件时十分有效.
    - 链接地址会被正确更新
    - 链接排序也会被更新: 如果对排序有特殊要求, 可考虑运行后 copy 想要的链接到目前的 SUMMARY.md 中.
  - `-o` or `--overwrite` 直接修改 SUMMARY.md. 由于 SUMMARY.md 会被修改, 请务必小心使用这个功能!

# Examples

### Basic:

eg1. folder tree:

```
eg1.
├── README.md
├── SUMMARY.md
├── concept-and-definition.md
├── language-secret.md
├── preface.md
├── rationality.md
├── study-under-uncertainty.md
├── twisted.png
└── wheel-of-python.png
```

`python gitbook-auto-summary.py eg1`


output SUMMARY-GitBook-auto-summary.md:

```
# Summary

- [concept-and-definition](./concept-and-definition.md)
- [language-secret](./language-secret.md)
- [preface](./preface.md)
- [rationality](./rationality.md)
- [README](./README.md)
- [study-under-uncertainty](./study-under-uncertainty.md)

```

Note:

- only .md file converted to link
- SUMMARY.md in input directory is ignored

eg2. folder tree:

```
eg2.
├── README.md
├── SUMMARY-GitBook-auto-summary.md
├── SUMMARY.md
├── for-myself-at-16
│   ├── README.md
│   ├── SUMMARY.md
│   ├── twisted.png
│   └── wheel-of-python.png
├── nomd
│   └── Untitled.ipynb
└── python-1-to-n
    ├── README.md
    ├── SUMMARY.md
    ├── chaos-to-telegram
    │   └── telegram.md
    ├── gitbook-auto-summary
    │   ├── argparse.md
    │   ├── gitbook-auto-summary.md
    │   └── os-and-os-path.md
    └── mahjong
        ├── chaos-to-bottle.md
        ├── chaos-to-sae.md
        └── mahjong.md
```

`python gitbook-auto-summary.py eg2`

output SUMMARY-GitBook-auto-summary.md:

```
# Summary

- [README](./README.md)
- for-myself-at-16
  - [README](for-myself-at-16/README.md)
  - [SUMMARY](for-myself-at-16/SUMMARY.md)
- python-1-to-n
  - chaos-to-telegram
    - [telegram](python-1-to-n/chaos-to-telegram/telegram.md)
  - gitbook-auto-summary
    - [argparse](python-1-to-n/gitbook-auto-summary/argparse.md)
    - [gitbook-auto-summary](python-1-to-n/gitbook-auto-summary/gitbook-auto-summary.md)
    - [os-and-os-path](python-1-to-n/gitbook-auto-summary/os-and-os-path.md)
  - mahjong
    - [chaos-to-bottle](python-1-to-n/mahjong/chaos-to-bottle.md)
    - [chaos-to-sae](python-1-to-n/mahjong/chaos-to-sae.md)
    - [mahjong](python-1-to-n/mahjong/mahjong.md)
  - [README](python-1-to-n/README.md)
  - [SUMMARY](python-1-to-n/SUMMARY.md)

```

Note: 

- SUMMARY.md in subdirectories is not ignored.
- Directories with no .md file are ignored.

### -a, --append

eg3. folder tree:

```
eg3.
├── README.md
├── SUMMARY.md
├── concept-and-definition.md
├── language-secret.md

former SUMMARY.md in eg3:

# Summary

- [语言的诡计](./language-secret.md)
- [README](./README.md)

```

`python gitbook-auto-summary.py -a eg3`


output SUMMARY-GitBook-auto-summary.md:

```
# Summary

- [concept-and-definition](./concept-and-definition.md)
- [语言的诡计](./language-secret.md)
- [README](./README.md)

```

Note:

- Former link name of language-secret.md (语言的诡计) is preserved.

### -o, --overwrite

Output file is the same, while script overwrite SUMMARY.md.

DO take care before overwrite!
