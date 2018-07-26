from clash_royale_one_k_finder import ClashRoyaleOneKFinder


def main():
    client = ClashRoyaleOneKFinder('clashroyale.cfg')
    client.find_open_1k_tournaments()


if __name__ == "__main__":
    main()
