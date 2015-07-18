# GitBook-auto-summary

Automatically update Summary.md of a GitBook repo

v1.0 

tested in Windows

# usage

1. `$ python gitbook-auto-summary.py`
2. input directory(it should be the *root* directory of GitBook repo), enter
3. the auto summary file `SUMMARY.md` will be under the same directory.

# examples

```
folder tree:
.
│  git-cheat-sheet.png
│  gitbook.md
│  introduction.md
│  SUMMARY.md
│  
├─child1
│      environment.md
│      git-basics.md
│      
└─child2
    │  mailing-list.md
    │  markdown-basics.md
    │  opening.md
    │  
    ├─child233
    │      mailing-list.md
    │      markdown-basics.md
    │      opening.md
    │      
    └─child233 - copy
            mailing-list.md
            markdown-basics.md
            opening.md

output SUMMARY.md:

# Summary

- child1
  - [environment](child1\environment.md)
  - [git-basics](child1\git-basics.md)
- child2
  - child233
    - [mailing-list](child2\child233\mailing-list.md)
    - [markdown-basics](child2\child233\markdown-basics.md)
    - [opening](child2\child233\opening.md)
  - child233 - copy
    - [mailing-list](child2\child233 - copy\mailing-list.md)
    - [markdown-basics](child2\child233 - copy\markdown-basics.md)
    - [opening](child2\child233 - copy\opening.md)
  - [mailing-list](child2\mailing-list.md)
  - [markdown-basics](child2\markdown-basics.md)
  - [opening](child2\opening.md)
- [gitbook](.\gitbook.md)
- [introduction](.\introduction.md)

```
