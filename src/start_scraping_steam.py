from core.steam_spider_handler import SteamSpiderExecutor
from core.steam_const import OS


if __name__ == '__main__':

    SETTING = {
        'is_on_sale': True,
        'platform': OS.MAC,
        'filepath': 'static/steam_img',
        'control_number': 30
    }

    test = SteamSpiderExecutor.run(**SETTING)

