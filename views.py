import fastapi
from fastapi.templating import Jinja2Templates
from fastapi import Request, Form
from starlette.requests import Request
from utilities import CpiData


templates = Jinja2Templates('templates')

router = fastapi.APIRouter()

cpi_data = CpiData()

@router.get("/")
def form_get(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})

@router.post("/")
def form_post(request: Request, country: str = Form(...)):
    result = str(country).upper()
    if result in cpi_data.countries:
        try:
            ticker = cpi_data.countries[result]
            cpi = cpi_data.get_cpi_all(ticker)
            return templates.TemplateResponse('index.html', context={'request': request, 'cpi': cpi, 'result': result})
        except ConnectionError:
            msg = 'Sorry, there was a problem with your request. Please try again later'
            return templates.TemplateResponse('index.html', context={'request': request, 'msg': msg})
    else:
        msg = 'PLEASE TRY A DIFFERENT COUNTRY!'
        return templates.TemplateResponse('index.html', context={'request': request, 'msg': msg})

@router.get("/about")
def about(request: Request):
    return templates.TemplateResponse("about.html", {'request': request})

@router.get("/countries")
def countries(request: Request):
    return templates.TemplateResponse("countries.html", {'request': request})

@router.get("/g5")
def g5_get(request: Request):
    cpi = cpi_data.get_cpi_g5()
    nums = range(5)
    msg = 'Connection error. Please try again.'
    try:
        return templates.TemplateResponse('g5.html', context={'request': request, 'cpi': cpi, 'nums': nums})
    except:
        len(cpi) < 5
        return templates.TemplateResponse("countries.html", {'request': request, 'msg': msg})
        


    
