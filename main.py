from clash_royale_one_k_finder import ClashRoyaleOneKFinder


def main():
    client = ClashRoyaleOneKFinder('clashroyale.cfg',
                                   debug=True,
                                   disable_cache=True,
                                   use_clashroyale_mock=True,
                                   use_notification_service_mock=True)
    client.find_open_1k_tournaments()


if __name__ == "__main__":
    main()
