curl -X POST http://localhost:5000/execute_bash \
  -H 'Content-Type: application/json' \
  -d '{"command": "ls -l"}'