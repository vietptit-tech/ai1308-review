THRESHOLD = 0.5
def predict(scores):
    """Nhãn có điểm cao nhất trong dict {nhãn: điểm}."""
    return max(scores, key=scores.get)