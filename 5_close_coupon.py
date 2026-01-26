import os
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi

load_dotenv(override=True, dotenv_path=".env")
configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = ApiClient(configuration) 
messaging_api = MessagingApi(api_client)

def close_coupon(coupon_id: str):
    try:
        api_response = messaging_api.close_coupon(coupon_id=coupon_id)
        print("The response of MessagingApi->delete_coupon:\n")
        print(api_response)

    except Exception as e:
        print(f"Exception when calling MessagingApi->delete_coupon: {e}\n")
        raise

if __name__ == "__main__":
    COUPON_ID = "01KFNS2Y3EB5S79S9Z86MQHGTH"
    close_coupon(COUPON_ID)
