from flask import Flask, redirect, session, request
from google_auth_oauthlib.flow import Flow
import os

app = Flask(__name__)
app.secret_key = "phishguard"

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

flow = Flow.from_client_secrets_file(
    "client_secret.json",
    scopes=["https://www.googleapis.com/auth/gmail.readonly"],
    redirect_uri="https://phishguardenterprise.xyz/callback"
)

@app.route("/login")
def login():
    auth_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(auth_url)

@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)
    return "Login Successful"

app.run()
