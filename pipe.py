import win32file


class Pipe:

    pipe_name: str

    def __init__(self, pipe_name: str) -> None:
        self.pipe_name = pipe_name
        self.connect_to_pipe()

    def connect_to_pipe(self):
        self.handle = win32file.CreateFile(self.pipe_name, 
                                      win32file.GENERIC_READ | win32file.GENERIC_WRITE, 
                                      0, 
                                      None, 
                                      win32file.OPEN_EXISTING, 
                                      0, 
                                      None)
    
    def send_data(self, data: bytes):
        win32file.WriteFile(self.handle, data)
    
    def send_string(self, string: str):
        self.send_data(string.encode())