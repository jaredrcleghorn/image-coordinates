#!/bin/bash

curl localhost:5000 \
	-X POST \
	-H "Content-Type: application/json" \
	-d '{"dimensions": [10, 12], "corners": [[1.5, 1.5], [4.0, 1.5], [1.5, 8.0], [4.0, 8.0]]}' \
	-s | json_pp
