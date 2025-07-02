from fastapi import FastAPI, HTTPException

leave_api = FastAPI()

@leave_api.get("/leave-balance")
def get_leave_balance(user_id: str):
    return {"user_id": user_id, "leave_balance": "5 days"}

@leave_api.post("/apply-leave")
def apply_leave(user_id: str, days: int):
    if days > 5:
        raise HTTPException(status_code=400, detail="Insufficient leave balance")
    return {"status": "success", "message": f"{days} days leave applied for {user_id}"}