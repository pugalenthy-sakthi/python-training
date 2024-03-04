class ResponseBuilder():
    def __init__(self,http_status,msg,data):
        self.http_status = http_status
        self.msg = msg
        self.data = data

    def getResponse(self):
        return {
            "http_status":self.http_status,
            "msg":self.msg,
            "data":self.data
        }