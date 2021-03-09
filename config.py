from os import getenv
from dotenv import load_dotenv

load_dotenv()


SESSION_NAME = getenv("SESSION_NAME", "AQCRVvquYv948m6ZguzebkubBzlyrM-Pa7hkcyAIV7UNg4S_3B3kNakoRJ39ek-2IXCRd9u7c9VytV7v4bfOtcUaTaxAKLJzTxJZZvRH_EzYU2Lb1dyDXVCi59PLirlwjqkc-qfyV-fsCe_vvBJOG6ks40GEzvHrXh-baC8ZWwYTTpyn-WkV5KwRNT7AirulhFeFi5i4UgMYPlJi6Udesl3NJnC74QQ6TTQyi9yaeRNtaWA9ATJb5-HZVzQZy9oJlr_hGbmBxQTuU00xEUO23dOo6XJrgqGc9KE_hBmCyQ2HlB0vYmehGYUKM19Qr5qz6FP8Irzr7smLRqD8MgWmjCKNY1esqQA")
BOT_TOKEN = getenv("BOT_TOKEN", "1325820510:AAE1zmBnuBIQWsDISzf55Y8wubY2EbUMxAk")

API_ID = int(getenv("API_ID", 3764950))
API_HASH = getenv("API_HASH", "70de2eb11fc84e2092619255f6f51953")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
