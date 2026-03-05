

import json

def json_to_dictionary(file_path):
    with open(file_path, "r") as file:
        dict_data = json.load(file)
    return dict_data

def extract_data(dict_data):
    restaurant_detail = {}
    restaurant_detail["restaurant_name"] = dict_data.get("data").get("title")
    restaurant_detail["restaurant_id"] = dict_data.get("data").get("uuid")
    restaurant_detail["image_url"] = []
    for data in dict_data.get("data").get("heroImageUrls"):
        restaurant_detail["image_url"].append(data.get("url"))
    location_value = dict_data.get("data").get("location")
    # print(location_value)
    restaurant_detail["location"] = {
        "address" : location_value.get("address"),
        "streetAddress" : location_value.get("streetAddress"),
        "city" : location_value.get("city"),
        "country" : location_value.get("country"),
        "postalCode" : location_value.get("postalCode"),
        "region" : location_value.get("region"),
        "latitude" : location_value.get("latitude"),
        "longitude" : location_value.get("longitude"),
    }



    restaurant_detail["timeing"] = []
    timeing = dict_data.get("data").get("hours")
    print(timeing)

    for data in timeing:
        dayRange = data.get("dayRange")
        restaurant_detail["timeing"].append({
            "dayRange": dayRange,
            "sectionHours": []
        })
        if not data.get("sectionHours"):
            continue
        for time_dict  in data.get("sectionHours"):
            temp_dict = {
                "startTime"  : round(time_dict.get("startTime") / 3600, 2),
                "endTime"  : round(time_dict.get("endTime") / 3600, 2)
            }
            restaurant_detail["timeing"][len(restaurant_detail["timeing"]) - 1].get("sectionHours").append(temp_dict)



    # this is categories data
    # data.catalogSectionsMap['0ad5db85-c10f-5ad6-897c-f8ef6bd5cc78']
    # data.catalogSectionsMap['0ad5db85-c10f-5ad6-897c-f8ef6bd5cc78'][0].catalogSectionUUID
    # data.catalogSectionsMap['0ad5db85-c10f-5ad6-897c-f8ef6bd5cc78'][0].payload.standardItemsPayload.title.text
    # data.catalogSectionsMap['0ad5db85-c10f-5ad6-897c-f8ef6bd5cc78'][0].payload.standardItemsPayload.catalogItems[0].uuid
    # data.catalogSectionsMap['0ad5db85-c10f-5ad6-897c-f8ef6bd5cc78'][0].payload.standardItemsPayload.catalogItems[
    #     0].imageUrl
    # data.catalogSectionsMap['0ad5db85-c10f-5ad6-897c-f8ef6bd5cc78'][0].payload.standardItemsPayload.catalogItems[
    #     0].title
    # data.catalogSectionsMap['0ad5db85-c10f-5ad6-897c-f8ef6bd5cc78'][0].payload.standardItemsPayload.catalogItems[
    #     0].itemDescription
    # data.catalogSectionsMap['0ad5db85-c10f-5ad6-897c-f8ef6bd5cc78'][0].payload.standardItemsPayload.catalogItems[
    #     0].priceTagline.text

    print(restaurant_detail)






    # swiggy_base_url = "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_600/"
    # swiggy_data = []
    # cards_list = dict_data["data"]["cards"]
    # for cards_dict in cards_list:
    #     if cards_dict.get("card").get("card").get("gridElements"):
    #         items_list = cards_dict["card"]["card"]["gridElements"]["infoWithStyle"]["items"]
    #         for items_dict in items_list:
    #             product_dict = {}
    #             product_dict["product_name"] = items_dict["displayName"]
    #             product_dict["product_id"] = items_dict["productId"]
    #             product_dict["price"] = float(items_dict["variations"][0]["price"]["offerPrice"]["units"])
    #             product_dict["quantity"] = str(items_dict["variations"][0]["quantityDescription"])
    #             product_dict["image_url"] = [swiggy_base_url + url for url in items_dict["variations"][0]["imageIds"]]
    #             Discount = items_dict["variations"][0]["price"]["offerApplied"]["listingDescription"].split("%")
    #             for num in Discount:
    #                 if num.isdigit():
    #                     Discount = int(num)
    #             product_dict["discount_percentage"] = Discount
    #             product_dict["product_mrp"] = float(items_dict["variations"][0]["price"]["mrp"]["units"])
    #             product_dict["is_available"] = items_dict["isAvail"]
    #             swiggy_data.append(product_dict)
    # print(swiggy_data)
    # return swiggy_data

# def convert_dict_to_json_data(extract_list):
#     path = "C:/Users/vishal.kushvanshi/PycharmProjects/swiggy_json_data/" + "Extract_data.json"
#     with open(path,"w") as file:
#         json.dump(extract_list,file, indent=4)


file_path = "C:/Users/vishal.kushvanshi/PycharmProjects/uber_eats/000a5dc6-cf5f-5967-b29a-d581e8f39339.json"

print(file_path)
dict_data = json_to_dictionary(file_path)
# print(dict_data)
print(type(dict_data))
extract_data(dict_data)
# convert_dict_to_json_data(extract_list)