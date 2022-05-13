from flask import Flask, request

app = Flask(__name__)

app_scope = "TEST APP scope"


@app.route("/")
def index():
    request_scope = "Test REQ scope"
    print(request_scope)
    print("Hello world 3")
    return "Hello world with debug"


print(app_scope)

if __name__ == "__main__":
    app.run(debug=True)
