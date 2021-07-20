import requests
import json

from utils import request_functions
from house_offer import HouseOffer


class FrieslandhuurtHouseOffer(HouseOffer):
    def __init__(self, amount_of_rooms_wanted, download_assets):
        super().__init__(amount_of_rooms_wanted, download_assets)
        self.domainname = "https://www.frieslandhuurt.nl"
        self.allobjects_endpoint = "/portal/object/frontend/getallobjects/format/json"

    def get_house(self):
        pass

    def get_houses(self):
        r = requests.get(self.domainname + self.allobjects_endpoint)
        houses = json.loads(r.text)["result"]
        # houses_file = open("aanbod.json", "r")
        # houses = json.loads(houses_file.read())["result"]

        for house in houses:
            amount_of_rooms = house["sleepingRoom"]["amountOfRooms"]
            category = house["dwellingType"]["categorie"]
            house_category = house["dwellingType"]["localizedName"]
            unique_house_name = house["urlKey"]

            if not self.is_house_compliant(amount_of_rooms, category, house_category):
                continue

            if self.download_assets:
                print(f"Downloading assets for {unique_house_name}")
                uris = self.__get_uris(house)
                request_functions.download_asset(uris, unique_house_name)

    def __get_uris(self, house):
        uris = []
        uri_locations = house["pictures"] + house["floorplans"]

        for entry in uri_locations:
            uris.append(self.domainname + entry["uri"])

        return uris
