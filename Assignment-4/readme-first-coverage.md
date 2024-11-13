# Running Tests and Viewing Reports

## Prerequisites

1. Make sure the app is running on localhost by following the instructions in `Assignment-2/readme-first.md`.

## Running Tests

1. Set the `PYTHONPATH` and run tests:
   ```bash
   PYTHONPATH=$(pwd)/app coverage run -m pytest app/test_app.py
   ```

## Viewing Coverage

1. Check the report using:
   ```bash
   coverage report -m
   ```