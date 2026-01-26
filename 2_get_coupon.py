import os
from pprint import pprint
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi

load_dotenv(override=True, dotenv_path=".env")
configuration = Configuration(access_token=os.getenv("CHANNEL_ACCESS_TOKEN"))
api_client = ApiClient(configuration) 
messaging_api = MessagingApi(api_client)

def get_coupon(coupon_id: str):
    
    try:
        coupon_list = messaging_api.list_coupon()
        print("Total coupons: {}\n".format(len(api_response_list.items)))
        print(coupon_list)
        api_response = messaging_api.get_coupon_detail(coupon_id=coupon_id)
        print("ข้อมูลคูปอง: {}\n".format(api_response))

    except Exception as e:
        print(f"Exception when calling MessagingApi->get_coupon: {e}\n")
        raise


if __name__ == "__main__":
    COUPON_ID = "01KFFCM1PBM7PD7M98VPGJYT98"
    get_coupon(COUPON_ID)
  
