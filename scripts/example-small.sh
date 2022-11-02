#!/bin/bash

curl localhost:5000 \
	-X POST \
	-H "Content-Type: application/json" \
	-d '{"dimensions": [3, 3], "corners": [[1, 1], [3, 1], [1, 3], [3, 3]]}' \
	-s | json_pp
