import carbonsh
import asyncio
def carbonImg(code):

    config = carbonsh.Config(language=carbonsh.languages.PYTHON,drop_shadow=False,)

    # returns >>> 'https://carbon.now.sh/?bg=rgba(...'
    carbon_url = carbonsh.code_to_url(code, config)

    loop = asyncio.get_event_loop()

    # saves the image as carbon.png where expected
    loop.run_until_complete(carbonsh.url_to_file(carbon_url, '/home/diamond/Documents/MyProjects/PythonData/pythonPractice/telagramBot/'))


# carbonImg("Aadesh lokhande")