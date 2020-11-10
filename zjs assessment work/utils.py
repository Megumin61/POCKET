#utils.py
#存放公共函数
class HttpError(Exception):
    def __init__(self,status_code,message):
        super().__init__()
        self.status_code=status_code
        self.message=message
    def to_dict(self):
        return{
            'status':self.status_code,
            'msg':self.message
        }