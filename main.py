from frieslandhuurt_house_offer import FrieslandhuurtHouseOffer


def main():
    frl = FrieslandhuurtHouseOffer(amount_of_rooms_wanted=4, download_assets=True)
    frl_houses = frl.update_houses()
    print(frl_houses)


if __name__ == '__main__':
    main()
