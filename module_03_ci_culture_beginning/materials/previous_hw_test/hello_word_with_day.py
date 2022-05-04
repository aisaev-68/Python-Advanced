import datetime

from flask import Flask

app = Flask(__name__)

day_to_word_map = {
    0: "Хорошего понедельника",
    1: "Хорошего вторника",
    2: "Хорошей среды",
    3: "Хорошего четверга",
    4: "Хорошей пятницы",
    5: "Хорошей суббота",
    6: "Хорошего воскресенья",
}


@app.route("/hello-world/<username>")
def hello_world(username: str) -> str:
    current_day = datetime.datetime.today().weekday()
    greetings = day_to_word_map[current_day]
    return f"Привет {username}. {greetings}!"


if __name__ == "__main__":
    app.run(debug=True)
