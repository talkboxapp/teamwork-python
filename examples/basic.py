import asyncio

from teamwork import AsyncClient


async def run():
    # create the async client
    client = AsyncClient("https://teamwork.app/api/v1", "API_TOKEN")

    # you can also use env variables for endpoint_url and api_token. Define the following env variables:
    # TEAMWORK_API_ENDPOINT = <your_teamwork_endpoint>
    # TEAMWORK_API_KEY = <your_api_key>
    #
    # After that, create the client without arguments:
    # client = AsyncClient()

    user = await client.user.by_id(1001)
    print(user)


if __name__ == "__main__":
    asyncio.run(run())
