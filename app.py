from application import app, mqtt_client
from flask import render_template
import random
import config as c


@app.route("/")
def index():
    # You could load real data here instead of random
    temps = [random.randint(18, 25) for _ in range(24)]  # Example: 24 hours
    return render_template("index.html", temps=temps)


if __name__ == "__main__":
    mqtt_client.loop_start()
    app.run(host=c.FLASK_HOST, port=c.FLASK_PORT)
