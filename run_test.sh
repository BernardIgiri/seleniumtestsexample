#!/bin/bash
set -e
# start application server
python3 -m http.server --directory webapp &
PID=$!
# wait for server to start
sleep 3
# run test
pytest test.py --verbose --capture=no
# kill server
kill $PID
echo 'Test completed!'
