import math

from flask import Flask, render_template, request

app = Flask(__name__)


def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier + 0.5) / multiplier


def bmi(waga: int, wzrost: int):
    """
    :param waga: waga w kg np.: 75
    :param wzrost: wzrost w cm np.: 176
    :return: (bmi_liczbowo, bmi_słownie) np.: (24.2, "Waga normalna")
    """
    bmi_liczbowo = round_half_up(waga / (wzrost * wzrost / 10000), 1)
    bmi_slownie = ""
    if (bmi_liczbowo <= 18.4):
        bmi_slownie = "Niedowaga"
    elif (bmi_liczbowo >= 18.5 and bmi_liczbowo <= 24.9):
        bmi_slownie = "Waga normalna"
    elif (bmi_liczbowo >= 25 and bmi_liczbowo <= 29.9):
        bmi_slownie = "Nadwaga"
    else:
        bmi_slownie = "Otyłość"
    return (bmi_liczbowo, bmi_slownie)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        wzrost = "176"
        waga = "75"
        (bmi_liczbowo, bmi_slownie) = bmi(int(waga), int(wzrost))
        return render_template('index.html', wzrost=wzrost, waga=waga,
                               bmi_liczbowo=bmi_liczbowo, bmi_slownie=bmi_slownie)

    if request.method == 'POST':
        wzrost = request.form.get("wzrost")
        waga = request.form.get("waga")
        (bmi_liczbowo, bmi_slownie) = bmi(int(waga), int(wzrost))
        return render_template('index.html', wzrost=wzrost, waga=waga,
                               bmi_liczbowo=bmi_liczbowo, bmi_slownie=bmi_slownie)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
