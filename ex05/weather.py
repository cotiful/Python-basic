
class Weather:
    def __init__(self, tm, totalCityName, doName, cityName, cityAreaId, kmaTci, TCI_GRADE):
        self.tm = tm
        self.totalCityName = totalCityName
        self.doName = doName
        self.cityName = cityName
        self.cityAreaId = cityAreaId
        self.kmaTci = kmaTci
        self.TCI_GRADE = TCI_GRADE

    @staticmethod
    def dictToEntity(data):
        weather = Weather(
            data["tm"],
            data["totalCityName"],
            data["doName"],
            data["cityName"],
            data["cityAreaId"],
            data["kmaTci"],
            data["TCI_GRADE"]
        )
        return weather
