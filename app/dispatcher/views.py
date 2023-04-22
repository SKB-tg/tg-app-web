import jinja2
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
from app.dispatcher import main_router
#router_views = APIRouter()
#router_views.include_router()
# создаем функцию, которая будет отдавать html-файл
templates = Jinja2Templates(directory="public")

@main_router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



# @aiohttp_jinja2.templates("index.html")
# async def index(request):
# 	data = await request.post()
# 	print(data)

	# response = openai.Completion.create(
	#    model="text-davinci-003",
	#    prompt=data,
	#    temperature=0.6,
	# )

	# result = request.args.get("result")
	# return render_template("index.html", result=result)

#@aiohttp_jinja2.template("index.html")
# async def answer_openai_handler(request):
# 	data = await request.post()
# 	parse_data = json.loads(data["my_data"])
# 	print(parse_data)
# #	return {'css_stat': '/css-static/', 'src_stat': '/src-static/', 'img_stat': '/img-static/',}

# @aiohttp_jinja2.template("css/style.css")
# async def get_handler_css(request):
# 	print('result')
