from static.staticData import typeofChoices, originChoices
import random
import datetime

def generateContainerData():
    return {
        "typeof": random.choice(typeofChoices),
        "origin": random.choice(originChoices),
        "receivedDate": datetime.datetime.utcnow().isoformat(),
        "peso": round(random.uniform(50, 1000), 2)
    }