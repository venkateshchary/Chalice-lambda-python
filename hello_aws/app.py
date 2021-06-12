from chalice import Chalice

app = Chalice(app_name='hello_aws')


@app.route('/')
def index():
    return """welcome to world of Chalice"""



def process():
    return "processing cron jobs"


