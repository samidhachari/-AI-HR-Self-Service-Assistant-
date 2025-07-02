from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
import grpc
import csv
from llm_parser import extract_intent
import hr_services_pb2
import hr_services_pb2_grpc

app = FastAPI()

class Settings(BaseModel):
    authjwt_secret_key: str = "supersecret"

@AuthJWT.load_config
def get_config():
    return Settings()

@app.post("/login")
def login(user: dict, Authorize: AuthJWT = Depends()):
    if user['username'] == "admin" and user['password'] == "admin":
        access_token = Authorize.create_access_token(subject=user['username'])
        return {"access_token": access_token}
    raise HTTPException(status_code=401, detail="Bad credentials")

@app.post("/process")
async def process_query(request: Request, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    data = await request.json()
    intent = extract_intent(data['query'])
    channel = grpc.insecure_channel('grpc-service:50051')
    stub = hr_services_pb2_grpc.LeaveServiceStub(channel)
    res = stub.GetLeaveBalance(hr_services_pb2.UserRequest(user_id=data['user_id']))
    return {"intent": intent, "response": res.message}

@app.get("/admin/tickets")
def admin_view_tickets(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    return [{"id": 1, "user": "user123", "issue": "VPN not working"}]

@app.get("/admin/tickets/export")
def export_tickets_csv(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    tickets = [{"id": 1, "user": "user123", "issue": "VPN not working"}]
    with open("tickets.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "user", "issue"])
        writer.writeheader()
        writer.writerows(tickets)
    return {"status": "exported", "file": "tickets.csv"}