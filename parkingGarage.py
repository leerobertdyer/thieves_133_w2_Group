class ParkingGarage():
    def __init__(self):
        self.yourTicket = ''
        self.tickets = {
            "1": {
                "available": False,
                "paid": True},
            "2": {
                "available": False,
                "paid": False},
            "3": {
                "available": True,
                "paid": False},
            "4": {
                "available": True,
                "paid": False},
            "5": {
                "available": True,
                "paid": False},
            "6": {
                "available": True,
                "paid": False},
            "7": {
                "available": True,
                "paid": False},
            "8": {
                "available": True,
                "paid": False},
            "9": {
                "available": True,
                "paid": False},
            "10": {
                "available": True,
                "paid": False},
            }
    def takeTicket(self):
        for key,value in self.tickets.items():
            if value["available"]:
                self.yourTicket = key
                value["available"] = False
                break
    def payForParking(self):
        pass
    def leaveGarage(self):
        pass
    def runner(self):
        pass
    