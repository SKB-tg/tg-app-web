
from fastapi import APIRouter, Request, Response, FastAPI, Depends
from fastapi.responses import Response
#from auth.api import router as auth
router = APIRouter()
#router.include_router(auth)


from googletrans import Translator


def text_translator(text='Hello friend', src='en', dest='ru'):
    # try:
    translator = Translator()
    translation = translator.translate(text=text, src=src, dest=dest)
    print(translation.text)
    return translation.text

@router.post("/mes_for_translator/")#, response_model=UserResponse)
async def answer_translator_handler1(request: Request):
    data = await request.json()
    text = data['text']
    ru_en = data['lang']
    if ru_en == False:
        src='ru'
        dest='en'
        text_translator1 = text_translator(text=text, src=src, dest=dest)
        print(0, str(text_translator1), text, ru_en)
    else:
        text_translator1 = text_translator(text=text)
        print(str(text_translator1))
    return {'messages': str(text_translator1)}


import json
import base64
import webptools
import openai
#from aiohttp.web import RouteTableDef, AbstractRouteDef
from pathlib import Path
#from aiohttp.web_fileresponse import FileResponse
# from aiohttp.web_request import Request
# from aiohttp.web_response import json_response, Response
#from aiohttp import web
import time

#routes = RouteTableDef()

STATIC_PATH = str(Path('main.py').parent.resolve()) + '/public'
STATIC_PATH_IMG =str(STATIC_PATH) + '/static/img/openai_img/'
openai.api_key = "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" #os.getenv("OPENAI_API_KEY")

def convertsu():
    from PIL import Image
    f1=[STATIC_PATH_IMG + 'input/for_sharg_m.png', STATIC_PATH_IMG + 'input/uy.png']
    for f in f1:
        png = Image.open(f)
        png.load() # required for png.split()

        background = png.convert("RGBA")
        #background.paste(png, mask=png.split()[3]) # 3 is the alpha channel

        background.save(f, quality=100)



@router.post("/mes_for_gpt/")#, response_model=UserResponse)
async def answer_openai_handler(request: Request):
    #convertsu()
    data = await request.json()
    text = data['text']
    response = openai.Image.create(#create( # create_edit # create_variation
      #image=open(STATIC_PATH_IMG + 'input/The_theme_is_a_0.png', "rb"),
      #mask = open(STATIC_PATH_IMG + 'input/for_sharg_m2.png', "rb"),#@photo_2023-03-14_02-55-34.png',
      prompt=text,
      n=4,
      size="512x512",
      response_format="b64_json",
    )
    fileName=[]
    fileName_web=[]
    for i in range(0,4):
        image_64_encode = json.loads(str(response))["data"][i]["b64_json"]
        image_64_decode = base64.b64decode(image_64_encode)
        fileName.append(STATIC_PATH_IMG + "out/" + text.replace(' ', '_')[0:15] + str(i))
        image_result = open(fileName[i].replace("\n", "_") + '.png', 'wb') # create a writable image and write the decoding result
        image_result.write(image_64_decode)
        print(fileName, STATIC_PATH_IMG)
        fileName_web.append('/static/img/openai_img/out/' +text.replace(' ', '_')[0:15] + str(i)+ ".webp")
        webptools.cwebp(input_image=fileName[i] + '.png', output_image=fileName[i] + ".webp",
            option="-q 80", logging="-v")
        i=+1
#############################################
    #image_url1 = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-EQt3NJBh1f6cmj6JOuDmAJsQ/user-eGXGrjzztnbHzrGC73a2YMAX/img-MZiADtV8zTp7n5h5Kt5AJ88t.png?st=2023-02-09T08%3A04%3A51Z&se=2023-02-09T10%3A04%3A51Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-02-08T22%3A00%3A16Z&ske=2023-02-09T22%3A00%3A16Z&sks=b&skv=2021-08-06&sig=9DObDHHuE8IqPRDW%2BdE6nkytdpVEi%2BOjlzlNqL9rnZU%3D"
    # image_url1 = response['data'][0]['url']
    # image_url2 = response['data'][1]['url']
    # image_url3 = response['data'][2]['url']
    # image_url4 = response['data'][3]['url']
    # image_url=[image_url1, image_url2, image_url3, image_url4]
#################################

    #answer='Ответ HelperGPT:\n' + response.choices[0].text+str(count)
    print(fileName_web)
    #f_download(image_url1)
    #time.sleep(5)
    return {'messages': fileName_web}

#   return {'css_stat': '/css-static/', 'src_stat': '/src-static/', 'img_stat': '/img-static/',}
# ["http://127.0.0.1:7800/img-static/openai_img/An_ultra_hd_det1.webp", "http://127.0.0.1:7800/img-static/openai_img/An_ultra_hd_det1.webp", "http://127.0.0.1:7800/img-static/openai_img/An_ultra_hd_det1.webp", "http://127.0.0.1:7800/img-static/openai_img/An_ultra_hd_det1.webp"]}
##########################################################################################
#Карикатурный отдыхающий , худой , в модных широких трусах, на берегу океана смотрит на закат большого солнца

###############################################################
async def answer_translator_handler(request):
    data = await request.json()
    text = 'перевести на английский язык:' + data['text']
    response = openai.Completion.create( 
        model="text-davinci-003", 
        prompt=text, 
        max_tokens=512, 
        temperature=0.9,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.2, 
        #stop=["\n"] 
    )
    # count=len(response.choices[0].text)
    answer=response.choices[0].text
    print(answer, text)
    return json_response(data={'messages': answer})


##############################################################
def f_download(image_url):

    import requests
    from requests import get
    import shutil
    import os
#   from bs4 import BeautifulSoup
    # img_tag = document.querySelector('img')
    # img_url = img_tag.src Authorization
    s = requests.Session()
    YOUR_API_KEY="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"
    params={
    "Authorization": f"Bearer {YOUR_API_KEY}",

    }
    headers = {
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Host": "oaidalleapiprodscus.blob.core.windows.net",
    #"Origin": "http://127.0.0.1:7800/",
    # "OpenAI-Organization": "org-EQt3NJBh1f6cmj6JOuDmAJsQ",
    # "OpenAI-User": "user-eGXGrjzztnbHzrGC73a2YMAX",
    "Referer": "http://127.0.0.1:7800/",
    "sec-ch-ua-platform": "Windows",
    "Sec-Fetch-Dest": "image",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    }
    try:
       respon = s.get(image_url, stream=True, params=params, headers=headers)
       print(68, respon.reason, respon)
    except Exception as e:
        print(err, e)
    file_name = os.path.basename("img_url")
    with open('./public/download/' + file_name, 'wb') as out_file: 
        shutil.copyfileobj(respon.raw, out_file)
    del respon
    print('File saved to', file_name)

    #return json_response({"ok": True}, status=200)
################################################################