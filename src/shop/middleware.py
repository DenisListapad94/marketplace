from datetime import datetime

path_file = "C:/Users/Denis/py_61_django/src/log.txt"

def simple_middleware(get_response):


    def middleware(request):

        request_path = request.path
        response = get_response(request)
        with open(file=path_file,mode="a") as file:

            now = datetime.now()
            date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
            from time import sleep
            sleep(0.5)
            log_message = request_path +" "+ str(response.status_code) + " " + date_time + "\n"
            file.write(log_message)

        return response

    return middleware