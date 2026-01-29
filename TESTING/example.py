def check_weather(temp):
    if temp > 20:
        return "hot"
    if temp <=0:
        return "super_cold"
    return "cold"
