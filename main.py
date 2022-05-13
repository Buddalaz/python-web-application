from flask import Flask, request

app = Flask(__name__)

app_scope = "TEST APP scope"


@app.route("/")
def index():

    # request_scope = "Test REQ scope"
    # print(request_scope)

    # print(request)  # request is a class
    # print(request.args)  # accessing request arguments in url
    # print(request.args["test"])  # accessing request arguments by given the key in url http://127.0.0.1:5000/?test=1TEST%20TEST

    value = request.args["test"]
    print(type(value))  # type is <class 'str'>

    print("Hello world 3")
    return "Hello world with debug"


@app.route("/calc")  # http://127.0.0.1:5000/calc?number_1=12&number_2=5
def calc():
    number_one = request.args["number_1"]
    number_two = request.args["number_2"]

    result = int(number_one)+int(number_two) #addition of incoming request string values and convert to integer and return the sum 

    return f"{result}" # we can't pass directly the int value


print(app_scope)

if __name__ == "__main__":
    app.run(debug=True)
