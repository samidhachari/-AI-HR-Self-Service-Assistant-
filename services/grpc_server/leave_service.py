import grpc
from concurrent import futures
import hr_services_pb2
import hr_services_pb2_grpc
import requests

class LeaveService(hr_services_pb2_grpc.LeaveServiceServicer):
    def GetLeaveBalance(self, request, context):
        res = requests.get("http://leave-api:8000/leave-balance", params={"user_id": request.user_id})
        return hr_services_pb2.LeaveResponse(status="success", message=f"{res.json()['leave_balance']} remaining")

    def ApplyLeave(self, request, context):
        res = requests.post("http://leave-api:8000/apply-leave", params={"user_id": request.user_id, "days": request.days})
        return hr_services_pb2.LeaveResponse(status="success", message=res.json()["message"])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hr_services_pb2_grpc.add_LeaveServiceServicer_to_server(LeaveService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()