from static import motoboys
from helpers import send_orders, check_motoboys_orders, get_motoboy_by_id


def main():
    send_orders()
    while True:
        motoboy_id = input(
            "Send motoboy_id or 0 to get all or ctrl+c to exit:")
        if(int(motoboy_id) == 0):
            check_motoboys_orders(motoboys)
        else:
            motoboy = get_motoboy_by_id(motoboy_id)
            if(motoboy is not None):
                check_motoboys_orders([motoboy])


if __name__ == "__main__":
    main()
