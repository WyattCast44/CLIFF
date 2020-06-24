class YoloCommand:

    signature = "yolo"

    def __init__(self, application):

        self.application = application

    def handle(self, params=None):

        self.application.config().set('env', 'prod')

        print(self.application.config().items())
