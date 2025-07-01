
def open_in_ide():

    parser = argparse.ArgumentParser(description="(w)es (cl)one", prog="wcl")
    parser.add_argument("url", type=str, help="repository clone url")
    args = parser.parse_args()

    repo_dir, _ = parse_url(args.url)
    subprocess.run(f"code '{repo_dir}'", shell=True, check=IGNORE_FAILURE, stdout=subprocess.DEVNULL)


