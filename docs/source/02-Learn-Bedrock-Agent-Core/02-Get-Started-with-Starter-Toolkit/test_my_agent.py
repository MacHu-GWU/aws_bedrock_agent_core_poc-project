# -*- coding: utf-8 -*-

"""
.. code-block:: bash

    ❯ curl -X POST http://localhost:8080/invocations \
      -H "Content-Type: application/json" \
      -d '{"prompt": "Hello!"}'
    {"result": {"role": "assistant", "content": [{"text": "Hello! It's nice to meet you. How are you doing today?"}]}}%
"""

import requests
from rich import print as rprint

res = requests.post(
    "http://localhost:8080/invocations",
    headers={"Content-Type": "application/json"},
    json={"prompt": "Hello!"}
)
rprint(res.json())
