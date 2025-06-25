```sh
./test_cases.sh > expected_test_cases_output
git diff # see if any changes to versioned output file (checked in copy is correct per my wesdemos user)

# double check expected matches what's in test_cases.sh
icdiff test_cases.sh expected_test_cases_output
# then look for commmented out paths to line up (obviously not the full script)
```
