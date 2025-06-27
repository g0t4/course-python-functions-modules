## Setup .venv w/ dependencies

```sh
# use uv for dependencies
uv sync

# OR, use venv/pip manually
python3 -m venv .venv
source .venv/bin/activate[.fish]
pip3 install .

```

## Running wcl

```sh
# always make sure your venv is activated
source .venv/bin/activate[.fish]

# then pick one:
python3 wcl.py
python3 -m wcl
```

## Testing

```sh
./test_cases.sh > expected_test_cases_output
git diff # see if any changes to versioned output file (checked in copy is correct per my wesdemos user)

# double check expected matches what's in test_cases.sh
icdiff test_cases.sh expected_test_cases_output
# then look for commmented out paths to line up (obviously not the full script)
```
