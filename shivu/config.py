class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5630057244"
    sudo_users = "5630057244"
    GROUP_ID = -1002190382416
    TOKEN = "6617412135:AAFc7F-H7xoNbDMHTO8y-MrKWiurymgGwT8"
    mongo_url = "mongodb+srv://darkth0ughtss00:loniko0908@music.njvuzcz.mongodb.net/?retryWrites=true&w=majority&appName=Music"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "DominosXD"
    UPDATE_CHAT = "DominosXd"
    BOT_USERNAME = "testinght_bot"
    CHARA_CHANNEL_ID = "-1002190382416"
    api_id = 20028561
    api_hash = "0f3793daaf4d3905e55b0e44d8719cad"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
