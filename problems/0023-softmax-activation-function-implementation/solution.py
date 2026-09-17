import math


def softmax(scores: list[float]) -> list[float]:
    if not scores:
        return []

    max_score = max(scores)

    exp_scores = [math.exp(a - max_score) for a in scores]

    total_sum = sum(exp_scores)
    
    return [exp_val / total_sum for exp_val in exp_scores]