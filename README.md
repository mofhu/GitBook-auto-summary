# GitBook-auto-summary

Automatically update SUMMARY.md of a GitBook repo

自动输出 GitBook 目录的 SUMMARY.md 文件.

By [Frank-the-Obscure @ GitHub](https://github.com/Frank-the-Obscure)

# usage

1. `$ python gitbook-auto-summary.py`
  - use argument `-o` to overwrite SUMMARY.md without checking.
2. input directory(it should be the *root* directory of a GitBook repo)
3. the auto summary file `SUMMARY.md` will be under the same directory.

Tested with Python 3.4.3 in Windows 7 and OS 10.10

# examples

```
folder tree:
.
├── README.md
├── SUMMARY.md
├── md
│   └── SUMMARY.md
├── nomd
└── os-and-os-path.md
```

output SUMMARY.md:

```
# Summary

- [os-and-os-path](./os-and-os-path.md)
- [README](./README.md)
- md
  - [SUMMARY](md/SUMMARY.md)

```
