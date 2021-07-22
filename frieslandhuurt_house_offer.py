import requests
import json

from utils import request_functions
from house_offer import HouseOffer


class FrieslandhuurtHouseOffer(HouseOffer):
    def __init__(self, amount_of_rooms_wanted, download_assets):
        super().__init__(amount_of_rooms_wanted, download_assets)
        self.domainname = "https://www.frieslandhuurt.nl"
        self.allobjects_endpoint = "/portal/object/frontend/getallobjects/format/json"
        self.singleobject_endpoint = "/portal/object/frontend/getobject/format/json"

    def get_house_details(self, house_id):
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        body = {"id": house_id}
        r = requests.post(
            self.domainname + self.singleobject_endpoint, headers=header, data=body)
        return json.loads(r.text)["result"]

    def update_houses(self):
        r = requests.get(self.domainname + self.allobjects_endpoint)
        houses = json.loads(r.text)["result"]
        # houses_file = open("aanbod.json", "r")
        # houses = json.loads(houses_file.read())["result"]

        for house in houses:
            amount_of_rooms = house["sleepingRoom"]["amountOfRooms"]
            object_category = house["dwellingType"]["categorie"]
            house_category = house["dwellingType"]["localizedName"]
            unique_house_name = house["urlKey"]

            if not self.is_house_compliant(amount_of_rooms, object_category, house_category):
                continue

            if self.download_assets:
                print(f"Downloading assets for {unique_house_name}")
                uris = self.__get_uris(house)
                request_functions.download_asset(uris, unique_house_name)

            detailed_info = self.get_house_details(house["id"])
            data = self.__prepare_house_data(house, detailed_info)
            self.house_offers.append(data)

        return self.house_offers

    def __get_uris(self, house):
        uris = []
        uri_locations = house["pictures"] + house["floorplans"]

        for entry in uri_locations:
            uris.append(self.domainname + entry["uri"])

        return uris

    def __prepare_house_data(basic_info, detailed_info):
        unique_house_name = basic_info["urlKey"]
        data = {
            "address": f'{basic_info["street"]} {basic_info["houseNumber"]} {basic_info["city"]["name"]}',
            "amountOfRooms": basic_info["sleepingRoom"]["amountOfRooms"],
            "houseCategory": basic_info["dwellingType"]["localizedName"],
            "numberOfReactions": detailed_info["numberOfReactions"],
            "areaLivingRoom": detailed_info["areaLivingRoom"],
            "areaSleepingRoom": detailed_info["areaSleepingRoom"],
            "remainingTimeUntilClosingDate": detailed_info["remainingTimeUntilClosingDate"]
        }
        return {unique_house_name: data}
