from ClashRoyaleOneKFinder import ClashRoyaleOneKFinder


def main():
    client = ClashRoyaleOneKFinder('clashroyale.cfg', debug=True)
    client.find_open_1k_tournaments()


if __name__ == "__main__":
    main()
