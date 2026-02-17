import os
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi

load_dotenv(override=True, dotenv_path=".env")
configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = ApiClient(configuration) 
messaging_api = MessagingApi(api_client)

def close_coupon(coupon_id: str):
    try:
        messaging_api.close_coupon(coupon_id=coupon_id)
        print(f"The response of MessagingApi->close_coupon: {coupon_id}\n")

    except Exception as e:
        print(f"Exception when calling MessagingApi->close_coupon: {e}\n")
        raise

if __name__ == "__main__":
    COUPON_ID = "01KHNHV8N25BT8CAX8DC3EVBYN"
    close_coupon(COUPON_ID)
