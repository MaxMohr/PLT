from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query, Request, Form
from sqlmodel import Field, Session, SQLModel, create_engine, select

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
import random
from emails import send_mail


class LoveTest(SQLModel, table=True):
    test_id: int | None = Field(default=None, primary_key=True)
    name_one: Annotated[str, Query(min_length=2, max_length=69)] = Field(index=True)
    name_two: Annotated[str, Query(min_length=2, max_length=69)] = Field(index=True)
    mail: str | None = Field(index=True)
    percentage: int = Field(index=True)


sqlite_file_name = "lovetest.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("home.html.jinja2", context=context)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/", response_class=HTMLResponse)
async def panda_percentage(
    request: Request,
    name_one: Annotated[str, Form()],
    name_two: Annotated[str, Form()],
    mail: Annotated[str, Form()],
    session: SessionDep,
):
    percentage = random.randint(0, 100)

    send_mail(name_one, name_two, mail, percentage)
    save_test(name_one, name_two, percentage, mail, session)

    return str(percentage)


@app.post("/test", response_class=HTMLResponse)
async def test_route(request: Request):
    return str(random.randint(68, 70))


def save_test(
    name_one: str,
    name_two: str,
    percentage: int,
    mail: str,
    session: SessionDep,
):
    result = LoveTest(name_one=name_one, name_two=name_two, percentage=percentage, mail=mail)
    session.add(result)
    session.commit()
    session.refresh(result)
    print(name_one, name_two, percentage, mail, result)
    print("Test gespeichert")
