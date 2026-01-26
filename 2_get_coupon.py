import os
from pprint import pprint
from dotenv import load_dotenv
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi

load_dotenv()

CHANNEL_ACCESS_TOKEN = os.environ.get("CHANNEL_ACCESS_TOKEN")
if not CHANNEL_ACCESS_TOKEN:
    raise ValueError("CHANNEL_ACCESS_TOKEN environment variable is not set")

# Configure Bearer authorization
configuration = Configuration(access_token=CHANNEL_ACCESS_TOKEN)
api_client = ApiClient(configuration)
messaging_api = MessagingApi(api_client)

def get_coupon(coupon_id: str):
    
    try:
        api_response_list = messaging_api.list_coupon()
        print("Total coupons:", len(api_response_list.items))
        print(api_response_list)
        api_response = messaging_api.get_coupon_detail(coupon_id=coupon_id)
        print("ข้อมูลคูปอง:")
        pprint(api_response)

    except Exception as e:
        print(f"Exception when calling MessagingApi->get_coupon: {e}\n")
        raise


if __name__ == "__main__":
    COUPON_ID = "01KFFCM1PBM7PD7M98VPGJYT98"
    
    try:
        response = get_coupon(COUPON_ID)
        print("\nดึงข้อมูลคูปองสำเร็จ!")
    except Exception as e:
        print(f"\nเกิดข้อผิดพลาด: {e}")
  
