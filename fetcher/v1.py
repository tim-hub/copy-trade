import os

import httpx
# dotenv
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.involio.com/v1_0"
ACCESS_KEY = os.environ.get("ACCESS_TOKEN", None)


async def get_investments(is_open=False, portfolio_id=None, page=1, page_size=10):
    """

    Example
    {
      "portfolioId": "45b89fe9-1a17-4318-98e0-5792897c2ed4",
      "isOpen": false,
      "params": {
        "page": 1,
        "size": 10
      }
    }
    :param is_open:
    :param portfolio_id:
    :param page:
    :param page_size:
    :return:
    """
    path = 'investments/get_investments'

    params = {
        "portfolioId": portfolio_id,
        "isOpen": is_open,
        "params": {
            "page": page,
            "size": page_size
        }
    }

    async with httpx.AsyncClient() as client:
        client.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(ACCESS_KEY)
        })
        response = await client.post(f"{BASE_URL}/{path}", json=params)
        response.raise_for_status()

    data = response.json()
    print(data)
    if not data.get("success", False):
        raise Exception(f"Error fetching investments: {data.get('message', 'Unknown error')}")

    return data.get("investmentsTicker", [])


if __name__ == "__main__":
    import asyncio


    async def main():
        try:
            investments = await get_investments(is_open=False, portfolio_id="45b89fe9-1a17-4318-98e0-5792897c2ed4")
            print(investments)
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


    asyncio.run(main())
