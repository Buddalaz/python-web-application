from flask import Flask, request, render_template

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

    # addition of incoming request string values and convert to integer and return the sum
    result = int(number_one)+int(number_two)

    return f"{result}"  # we can't pass directly the int value


@app.route("/prism")  # http://127.0.0.1:5000/prism?area_of_base=10&height=5
def cal_prism():
    b = request.args["area_of_base"]
    h = request.args["height"]
    v = int(b)*int(h)
    return f"{v}"


# http://127.0.0.1:5000/prism2/10/2
@app.route("/prism2/<area_of_base>/<height>")  # path parameters
def cal_prism2(area_of_base, height):
    v = int(area_of_base)*int(height)
    return f"{v}"

# send json response
# http://127.0.0.1:5000/json_res/10/2


@app.route("/json_res/<area_of_base>/<height>")
def send_json_resp(area_of_base, height):
    v = int(area_of_base)*int(height)
    response_data = {
        "result": v
    }
    print(type(response_data))  # <class 'dict'>
    return response_data


# send html content as response
@app.route("/view")
def view():
    return "<h1>Hello World</h1>"

# second method access root .html files and pass it as response


@app.route("/view_index")
def view_from_file():
    # response_view = open("index.html").read() access root .html files
    response_view = open("templates/index.html").read()
    return response_view

# thired method is we can use inbuild render_template in Flask to pass .html file as response in the templates folder


@app.route("/view_index2")
def view_from_file2():
    return render_template("index.html")


# replacing html file content with file opening
@app.route("/view_index3")
def view_from_file3():
    name = request.args["name"]
    age = request.args["age"]
    response_view = open("templates/index.html").read()
    response_view = response_view.replace("{{name}}", name)
    response_view = response_view.replace("{{age}}", age)
    return response_view

# replacing html file content with Flask renderTeamplate


@app.route("/view_index4")
def view_from_file4():
    name = request.args["name"]
    age = request.args["age"]
    return render_template("index.html", name=name, age=age)

# get value from form post method ekata deafult allow karanne nahh save button eka click karama get eke wage
# api kiyanna ona mona method ekada ganna ona kiyala
# capital simple unata kamak nahh
@app.route("/view_index5", methods=["GET", "POST"])
def view_from_file5():

    # print(request.method)  # can access what method is requesting

    name = "Empty"
    age = "Empty"

    # if request.method == "POST":
    #     print(request.form) # get form data
    #     if "name" in request.args:
    #         name = request.args["name"]
    #     if "age" in request.args:
    #         age = request.args["age"]

    if request.method == "POST":
        if "name" in request.form:
            name = request.form["name"]
        if "age" in request.form:
            age = request.form["age"]

    return render_template("index.html", name=name, age=age)


print(app_scope)

if __name__ == "__main__":
    app.run(debug=True)
