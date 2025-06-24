import httpx

from fetcher.v1 import get_investments

PORTFOLIO_ID_1 = "45b89fe9-1a17-4318-98e0-5792897c2ed4"

if __name__ == "__main__":
    import asyncio


    async def main():
        try:
            investments = await get_investments(is_open=False, portfolio_id=PORTFOLIO_ID_1)
            print(investments)
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


    asyncio.run(main())
