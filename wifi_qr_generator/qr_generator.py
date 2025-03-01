import argparse

import qrcode
import qrcode.constants


def generate_qr(name, password, password_enc):
    # Create the qr code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add your wifi data
    qr.add_data(f"WIFI:S:{name};T:{password_enc};P:{password};;")
    qr.make(fit=True)

    # Export the qr to an image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("wifi_qr.png")
    
    print("Your QR image has been generated! ")


def create_argument_parser():
    # Create the Argument Parser
    parser = argparse.ArgumentParser(
        prog="WIFI QR Generator",
        description="This scripts generates a wifi qr code to be used by your friends/clients",
    )

    # Add arguments
    parser.add_argument(
        "-n", "--name", required=True, help="Wifi name/SSID you are connecting to"
    )
    parser.add_argument(
        "-p", "--password", required=True, help="Wifi password you use to connect"
    )
    parser.add_argument(
        "-t",
        "--password-enc",
        default="WPA2",
        choices=["WEP", "WPA", "WPA2", "WPA3"],
        help="Password encryption to be use. Default: WPA2",
    )

    return parser


def main():
    args = create_argument_parser().parse_args()
    generate_qr(args.name, args.password, args.password_enc)


if __name__ == "__main__":
    main()
