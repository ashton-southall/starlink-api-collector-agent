import os
import requests

####
# Function Definitions
####

def get_starlink_env():
    try:
        starlink_dish_IP = os.environ['STARLINK_DISH_IP']
    except exception as exception:
        print(exception)
    finally:
        return starlink_dish_IP


def get_starlink_status(starlink_dish_IP):
    # Send the GET request
    HTTP_RESPONSE = requests.get(starlink_dish_IP)

    # Check if the request was successful
    if HTTP_RESPONSE.status_code == 200:
        # Print the response content to log
        print(HTTP_RESPONSE.content)
    else:
        print(f'Failed to retrieve data: {HTTP_RESPONSE.status_code}')

def main():
    starlink_dish_IP = get_starlink_env()
    get_starlink_status(starlink_dish_IP)

####
# Main
####

if __name__ == "__main__":
    main()