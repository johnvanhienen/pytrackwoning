from frieslandhuurt_house_offer import FrieslandhuurtHouseOffer


def main():

    #     print(f'{house["street"]} {house["houseNumber"]} {house["city"]["name"]}')
    #     print(f'Aantal slaapkamers: {house["sleepingRoom"]["amountOfRooms"]}')
    #     print(f'Type woning: {house["dwellingType"]["localizedName"]}')
    #     print(f'Totale huur: {house["totalRent"]}')
    #     print(f'Is gepubliceerd: {house["isGepubliceerd"]}')

        # https://www.frieslandhuurt.nl/portal/object/frontend/getobject/format/json
        # form url encoded: id = 38292
        # "numberOfReactions"
        # "areaLivingRoom": 35,
        # "areaSleepingRoom": "8, 8, 11 en 11",
        # "remainingTimeUntilClosingDate"

        # if download_assets:
        #     self.__download_assets(house)

    frl = FrieslandhuurtHouseOffer(amount_of_rooms_wanted=4, download_assets=True)
    frl_houses = frl.get_houses()
    print(frl_houses)


main()


# r = requests.get("https://www.frieslandhuurt.nl/portal/object/frontend/getallobjects/format/json")
   # supply = json.loads(r.text)["result"]
   # supply_file = open("aanbod.json", "r")
# supply = json.loads(supply_file.read())["result"]
# frl = Frieslandhuurt(amount_of_rooms=3)
# frl.retrieve_houses(True)
