def evaluate_conditions(data):
    alerts = []
    if data['temperature'] > 30:
        alerts.append("High temperature detected, consider increasing irrigation.")
    if data['humidity'] < 50:
        alerts.append("Low humidity levels might affect crop growth.")

    return alerts
