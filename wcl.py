import argparse
import os
import re
import subprocess
from urllib.parse import urlparse

# constants for subprocess.run for readability
IGNORE_FAILURE = False
STOP_ON_FAILURE = True

parser = argparse.ArgumentParser(description="(w)es (cl)one", prog="wcl")
parser.add_argument("url", type=str, help="repository clone url")
parser.add_argument("--dry-run", action="store_true", help="preview changes")
parser.add_argument("--path-only", action="store_true", help="return path (do not clone)")
args = parser.parse_args()

url: str = args.url
dry_run: bool = args.dry_run
path_only: bool = args.path_only

url = url.strip()

# strip .git
if url.endswith(".git"):
    url = url[:-4]

parsed: dict | None = None

if url.startswith("git@"):  # SSH URL
    # git@host:path/to/repo.git
    ssh_pattern = r"git@([^:]+):(.+)"
    match = re.match(ssh_pattern, url)
    if match:
        host, path = match.groups()
        parsed = {"domain": host, "repo_path": path}
    # else => None (invalid git@ url)
elif url.startswith("https://"):  # HTTPS or similar
    url_parsed = urlparse(url)
    path = url_parsed.path.lstrip("/")  # Remove leading '/'
    path = path.rstrip("/")  # Remove trailing '/' => wcl https://github.com/Hammerspoon/Spoons/

    # org/repo/blob/branch/path/to/file, strip blob+ (must have org/repo before blob)
    # PRN if it happens to be that a repo is named blob/tree then we have issues!
    if re.search(r"[^/]+/[^/]+/(blob|tree)/", path):
        path = re.sub(r"/(blob|tee).*", "", path)

    parsed = {"domain": url_parsed.netloc, "repo_path": path}
elif not re.search(r"\/", url):
    # url = "g0t4"
    #   => github.com:g0t4/{url}
    parsed = {"domain": "github.com", "repo_path": "g0t4/" + url}
elif re.search(r"\/", url):
    # url = "g0t4/dotfiles"
    #   => github.com:g0t4/dotfiles
    # 2+ levels (obviously github only has two: org/repo)
    parsed = {"domain": "github.com", "repo_path": url}

if not parsed:
    print("unable to parse repository url", url, "\n")
    exit(1)

host_name = parsed["domain"]
if host_name == "github.com":
    host_name = "github"
elif host_name == "gitlab.com":
    host_name = "gitlab"
elif host_name == "bitbucket.org":
    host_name = "bitbucket"

repo_dir = os.path.expanduser(os.path.join("~/repos", host_name, parsed["repo_path"]))
org_dir = os.path.dirname(repo_dir)

if path_only:
    print(repo_dir)
    exit()

# ensure org dir exists, including parents
# - can also let git clone create parents
if dry_run:
    print("mkdir -p", org_dir, "\n")
else:
    os.makedirs(org_dir, exist_ok=True)

if os.name != "nt":
    which_zsh = subprocess.run(f"which zsh", shell=True, check=IGNORE_FAILURE, stdout=subprocess.DEVNULL)
    if which_zsh.returncode == 0:
        # - zsh's z allows dir to be added before it is created
        # - adding ahead of creating (during clone) means I can _cd_ to it while its cloning
        # - or if dir already exists, then add to the stats count for it
        z_add_zsh = f"z --add '{repo_dir}'"
        if dry_run:
            print("# zsh z add:")
            print(z_add_zsh, "\n")
        else:
            # zsh -i => interactive, otherwise z command won't be available
            subprocess.run(["zsh", "-il", "-c", z_add_zsh], check=IGNORE_FAILURE)

if os.path.isdir(repo_dir):
    print("repo_dir found, attempt pull latest", "\n")
    pull = ["git", "-C", repo_dir, "pull"]
    if dry_run:
        print(pull, "\n")
    else:
        subprocess.run(pull, check=IGNORE_FAILURE)
else:
    always_use_https = parsed["domain"] in ["gitlab.gnome.org", "sourceware.org", "git.kernel.org", "huggingface.co", "git.sr.ht"]
    if always_use_https:
        clone_from = f"https://{parsed["domain"]}/{parsed["repo_path"]}"
    else:
        # prefer ssh for git repos (simple, standard, supports ssh auth)
        clone_from = f"git@{parsed["domain"]}:{parsed["repo_path"]}"
    print(f"# cloning {clone_from}...")

    clone = ["git", "clone", "--recurse-submodules", clone_from, repo_dir]
    if dry_run:
        print(clone, "\n")
    else:
        subprocess.run(clone, check=STOP_ON_FAILURE)

is_windows = os.name == "nt"
if is_windows:
    # - dir must exist before calling z
    # - FYI current pwsh z caches the db, so this only works for z calls in a new pwsh instance
    z_add_pwsh = f"z '{repo_dir}'"
    if dry_run:
        print("# pwsh z add:")
        print(z_add_pwsh, "\n")
    else:
        subprocess.run(["pwsh", "-NoProfile", "-Command", z_add_pwsh], check=IGNORE_FAILURE)

if os.name != "nt":
    which_fish = subprocess.run(f"which fish", shell=True, check=IGNORE_FAILURE, stdout=subprocess.DEVNULL)
    if which_fish.returncode == 0:
        # - dir must exist before calling __z_add
        # - __z_add does not take an argument, instead it uses $PWD (hence set cwd)
        # - FYI I had issues w/ auto-venv (calling deactivate) in fish (but, not zsh)
        #   so, don't launch an interactive shell (which would then use auto-venv)
        # - fish doesn't need interactive for z to be loaded (b/c its installed in functions dir)
        z_add_fish = ["fish", "-c", "__z_add"]
        if dry_run:
            print("# fish z add:")
            print(z_add_fish, f"cwd={repo_dir}", "\n")
        else:
            subprocess.run(z_add_fish, cwd=repo_dir, check=IGNORE_FAILURE)
