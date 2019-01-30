from flask import *
import pandas as pd
import numpy as np
import time
import inputs

app = Flask(__name__)

@app.route("/")
def show_tables():
    data = pd.read_csv('a.csv')
    data = data.sort_values('Magnitude', ascending=False)
    data = data[data['Magnitude'] >= 3.6]
    data.insert(0, 'rank', pd.Series(np.arange(1, data.shape[0] + 1, dtype=np.int), index=data.index))
    # data.set_index(['Name'], inplace=True)
    # data.index.name=None
    # females = data.loc[data.Gender=='f']
    # males = data.loc[data.Gender=='m']
    return render_template('view.html',tables=[data.to_html(classes='female', index=False)],
    titles = ['na'])

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    data = pd.read_csv('a.csv')
    pads = inputs.devices.gamepads

    if len(pads) == 0:
        raise Exception("Couldn't find any Gamepads!")

    t_end = time.time() + 2
    x = []
    while time.time() < t_end:
        events = inputs.get_gamepad()
        for event in events:
            x.append(event.state)
            # print(1)
            # print(event.ev_type)
            # print(2)
            # print(event.code)
            # print(3)
            # print(type(event.state))
            # print('########################')
    x = np.array(x)
    data = data.append(pd.DataFrame([[processed_text, x.max()]], columns=['Name', 'Magnitude']))
    data.to_csv('a.csv', index=False)
    return show_tables()

@app.route("/")
def timer():
    return render_template('timer.html')

@app.route('/r', methods=['RELOAD'])
def reload():
    return reload_r()

@app.route('/r')
def reload_r():
    return show_tables()



if __name__ == "__main__":
    app.run(debug=True)