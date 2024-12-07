from flask import Flask, redirect, render_template, request, session
from services.auth import get_auth_url, exchange_code_for_token
from services.spotify_api import get_user_top_tracks
from services.analysis import analyze_top_tracks

app = Flask(__name__)
app.secret_key = "your-secret-key"

@app.route("/")
def index():
    auth_url = get_auth_url()
    return render_template("index.html", auth_url=auth_url)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    token_info = exchange_code_for_token(code)
    session["token"] = token_info["access_token"]
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    token = session.get("token")
    if not token:
        return redirect("/")
    top_tracks = get_user_top_tracks(token)["items"]
    analysis = analyze_top_tracks(top_tracks)
    return render_template("dashboard.html", top_tracks=top_tracks, analysis=analysis)

if __name__ == "__main__":
    app.run(debug=True)
