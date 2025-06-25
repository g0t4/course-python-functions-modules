#!/usr/bin/env bash

# FYI this does not check for:
# - Normalized clone url for some hosts (uses_https check)

uv run wcl.py --path-only https://github.com/torvalds/linux
# /Users/wesdemos/repos/github/torvalds/linux

uv run wcl.py --path-only git@github.com:g0t4/ask-openai.nvim
# /Users/wesdemos/repos/github/g0t4/ask-openai.nvim

# not covered in original tests, used hhttps instead
# uv run wcl.py --path-only git://gcc.gnu.org/git/gcc.git
uv run wcl.py --path-only https://gcc.gnu.org/git/gcc.git
# /Users/wesdemos/repos/gcc.gnu.org/git/gcc

# .git suffix on https
uv run wcl.py --path-only https://gitlab.com/g0t4/dotfiles.git
# /Users/wesdemos/repos/gitlab/g0t4/dotfiles

uv run wcl.py --path-only SeeGit
# /Users/wesdemos/repos/github/g0t4/SeeGit

uv run wcl.py --path-only python/cpython
# /Users/wesdemos/repos/github/python/cpython

# contains other parts of URI path, strip those
uv run wcl.py --path-only "https://github.com/jackMort/ChatGPT.nvim?tab=readme-ov-file#configuration"
# /Users/wesdemos/repos/github/jackMort/ChatGPT.nvim

# 3 level repo_path
uv run wcl.py --path-only https://huggingface.co/datasets/PleIAs/common_corpus
# /Users/wesdemos/repos/huggingface.co/datasets/PleIAs/common_corpus

# ignore tree/... (don't treat as part of repo_path)
uv run wcl.py --path-only https://huggingface.co/datasets/PleIAs/common_corpus/tree/main
# /Users/wesdemos/repos/huggingface.co/datasets/PleIAs/common_corpus

# ignore blob/ too
uv run wcl.py --path-only https://huggingface.co/datasets/PleIAs/common_corpus/blob/main/README.md
# /Users/wesdemos/repos/huggingface.co/datasets/PleIAs/common_corpus

uv run wcl.py --path-only https://huggingface.co/microsoft/speecht5_tts
# /Users/wesdemos/repos/huggingface.co/microsoft/speecht5_tts
