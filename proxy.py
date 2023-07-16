class Subject:
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling request.")

class Proxy(Subject):
    def __init__(self):
        self.real_subject = None

    def request(self):
        if self.real_subject is None:
            self.real_subject = RealSubject()
        self.real_subject.request()

# Create a proxy object and make a request
proxy = Proxy()
proxy.request()  # Output: RealSubject: Handling request.
