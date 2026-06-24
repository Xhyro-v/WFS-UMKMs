from sqlalchemy.exc import OperationalError
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI()

@app.exception_handler(OperationalError)
async def database_error_handler(
      request: Request,
      exc : OperationalError
):
      return JSONResponse(
          status_code=503,
          content={"detail":"Database bermasalah/Belum aktif"}
      )

@app.exception_handler(RequestValidationError)
async def validation_error_handler(
      request: Request,
      exc : RequestValidationError
  ):
        message=("Validation errors")
        for error in exc.errors():
            message += f"\nField: {error['loc']}, Error: {error['msg']}"
        return PlainTextResponse(message, status_code=400)
