

def analyze_top_tracks(top_tracks):
    """
    Analyze the given top tracks and compute metrics.
    Args:
        top_tracks (list): List of top tracks fetched from Spotify API.
    Returns:
        dict: Analysis results like average BPM, valence, etc.
    """
    if not top_tracks:
        return {"error": "No tracks to analyze"}

    total_duration = sum(track['duration_ms'] for track in top_tracks)
    total_popularity = sum(track['popularity'] for track in top_tracks)
    average_duration = total_duration / len(top_tracks)
    average_popularity = total_popularity / len(top_tracks)

    return {
        "average_duration": ms_to_minutes_seconds(average_duration),
        "average_popularity": average_popularity
    }

def ms_to_minutes_seconds(ms):
    minutes = int(ms // 60000)  # 60,000 ms in a minute
    seconds = int((ms % 60000) // 1000)  # Remaining seconds after converting to minutes
    return f"{minutes} minutes and {seconds} seconds"
