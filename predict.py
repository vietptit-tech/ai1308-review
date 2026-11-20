THRESHOLD = 0.5
def predict(scores):
    """Nhãn có điểm cao nhất trong dict {nhãn: điểm}, hoặc 'unknown' nếu dưới ngưỡng."""
    best_label = max(scores, key=scores.get)
    if scores[best_label] < THRESHOLD:
        return "unknown"
    return best_label