from cli import parse_arguments
from db_view import list_images
from database import deregister_image_by_id

from database import (
    init_db,
    register_image,
    search_image,
    deregister_image
)


def main():
    init_db()
    args = parse_arguments()

    try:
        if args.command == "register":
            register_image(args.name, args.image)
            print(f"✅ Image '{args.name}' registered successfully")

        elif args.command == "search":
            name, distance = search_image(args.image)
            if name:
                print(f"🔍 Match found: {name} (distance={distance})")
            else:
                print(f"❌ No matching image found (closest distance={distance})")
        #deregister by name only process
        # elif args.command == "deregister":
        #     deleted = deregister_image(args.name)
        #     if deleted:
        #         print(f"🗑️ Image '{args.name}' deregistered")
        #     else:
        #         print("⚠️ Image not found")
        elif args.command == "deregister":
            if args.name:
                deleted = deregister_image(args.name)
                key = args.name
            else:
                deleted = deregister_image_by_id(args.id)
                key = args.id

            if deleted:
                print(f"🗑️ Image '{key}' deregistered")
            else:
                print("⚠️ Image not found")


        elif args.command == "list":
            rows = list_images()
            if not rows:
                print("📂 Database is empty")
            else:
                print("\n📸 Registered Images:")
                print("-" * 40)
                for img_id, name, path in rows:
                    print(f"ID: {img_id} | Name: {name} | Path: {path}")

        else:
            print("❗ Please provide a valid command")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
