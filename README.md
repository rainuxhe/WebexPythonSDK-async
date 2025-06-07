# WebexPythonSDK-async

Basic functionalities are derived from [WebexPythonSDK](https://github.com/WebexCommunity/WebexPythonSDK), but modified to use asynchronous HTTP calls.

## Examples

```python
from webexpythonsdk_async import AsyncWebexAPI
import asyncio

token = "YOUR_TOKEN"

api = AsyncWebexAPI(access_token=token)

async def main():
    async for webhook in api.webhooks.list():
        print(f"type: {type(webhook)}, {webhook}")

    resp = await api.messages.create(toPersonEmail="raihe@cisco.com", text="Hello World")
    print(f"type: {type(resp)}, {resp}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Installation

```bash
python -m pip install webexpythonsdk-async
```

## Todo

- [ ] Support synchronous calls.
- [ ] Add more examples.