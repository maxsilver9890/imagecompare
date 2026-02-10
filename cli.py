import argparse
from database import register_image, search_image, deregister_image


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="CLI Image Registration System"
    )
    subparsers = parser.add_subparsers(dest="command")
    
    # List images
    list_cmd = subparsers.add_parser("list")

    # Register
    reg = subparsers.add_parser("register")
    reg.add_argument("--name", required=True)
    reg.add_argument("--image", required=True)

    # Search
    search = subparsers.add_parser("search")
    search.add_argument("--image", required=True)

    # Deregister
    dereg = subparsers.add_parser("deregister")
    # dereg.add_argument("--name", required=True)  #Delete by name only
    group = dereg.add_mutually_exclusive_group(required=True)
    group.add_argument("--name", help="Image name to deregister")
    group.add_argument("--id", type=int, help="Image ID to deregister")

    return parser.parse_args()
