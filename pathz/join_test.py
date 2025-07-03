# import os
from os import path

# inspiration:
# repo_dir = os.path.expanduser(os.path.join("~/repos", host_name, parsed["repo_path"]))

def test_joiner_no_tilde_expands_like_normal():
    joined = path.join("path", "to", "file.txt")
    assert "path/to/file.txt" == joined

def test_joiner_tilde_leading_expands_to_home_dir():
    joined = path.join("~/path", "to", "file.txt")
    assert "/Users/wesdemos/path/to/file.txt" == joined  # Change to your HOME dir
    # assert (os.getenv("HOME") or "") + "/path/to/file.txt" == joined  # OR, use this one that looks up HOME dir
