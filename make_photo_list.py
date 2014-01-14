import glob
import json

photo_list = {
    "photos": glob.glob("photos/*.jpg")
}
out_file = open("photos/list.json", "w")
json.dump(photo_list, out_file, indent=4)

