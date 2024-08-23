async with BitlyAPI(**credentials) as api:
    responses = await asyncio.gather(
        api.link.clicks(link='https://bit.ly/2EAh3Vo'),
        api.link.clicks(link='2A7lTGn'),
        )
        for response in responses:
            print(response.link_clicks) # output: <number of clicks>
        try:
            response = await api.link.clicks(link='bad_link')
        except APIException as err:
            print(err) # output: [404] NOT FOUND
