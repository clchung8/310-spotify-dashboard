import requests

SPOTIFY_API_URL = "https://api.spotify.com/v1"

def get_user_top_tracks(token):
    """
    Fetch user's top tracks.
    """
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{SPOTIFY_API_URL}/me/top/tracks", headers=headers, params={"limit": 10})
    return response.json()

def get_user_recent_tracks(token):
    """
    Fetch user's recently played tracks.
    """
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{SPOTIFY_API_URL}/me/player/recently-played", headers=headers, params={"limit": 10})
    return response.json()
