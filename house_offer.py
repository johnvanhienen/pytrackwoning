class HouseOffer:
    def __init__(self, amount_of_rooms_wanted, download_assets):
        self.amount_of_rooms_wanted = str(amount_of_rooms_wanted)
        self.download_assets = download_assets

    def is_house_compliant(self, amount_of_rooms, category, house_category):
        if not amount_of_rooms == self.amount_of_rooms_wanted:
            return False
        if not category == "woning":
            return False
        if "Appartement" in house_category:
            return False
        return True
