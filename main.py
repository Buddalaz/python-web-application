from flask import Flask, request

app = Flask(__name__)

app_scope = "TEST APP scope"


@app.route("/")
def index():

    # print(request)  # request is a class
    print(request.args)  # accessing request arguments in url
    print(request.args["test"])  # accessing request arguments by given the key in url http://127.0.0.1:5000/?test=1TEST%20TEST

    request_scope = "Test REQ scope"
    print(request_scope)
    print("Hello world 3")
    return "Hello world with debug"


print(app_scope)

if __name__ == "__main__":
    app.run(debug=True)
