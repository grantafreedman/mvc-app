from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        number = request.form.get("number")

        validation_result = model.validate_input(number)

        if validation_result["is_valid"]:
            result = model.check_odd_even(int(number))
            model.store_data(number, result)
            return render_template("index.html", result=result, error=None)
        else:
            model.store_error(number, validation_result["error_message"])
            return render_template("index.html", result=None, error=validation_result["error_message"])

    return render_template("index.html", result=None, error=None)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
