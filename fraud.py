import random

def CalFraud(request):
    fraud_score = random.randint(0, 100)
    request['fraud_score'] = fraud_score
    if fraud_score >= 50:
        request['fraud'] = 1
    else:
        request['fraud'] = 0
    return request   
