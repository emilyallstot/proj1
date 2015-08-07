import os
import yelp
import csv
import phonenumbers

yelp_api = yelp.Api(
    consumer_key=os.environ['YELP_CONSUMER_KEY'],
    consumer_secret=os.environ['YELP_CONSUMER_SECRET'],
    access_token_key=os.environ['YELP_ACCESS_TOKEN'],
    access_token_secret=os.environ['YELP_ACCESS_TOKEN_SECRET'])

def address_formatted(raw_address):
    address_string = ""
    for line in raw_address:
        address_string = address_string + line + ' '
    return address_string

def phone_formatted(raw_phone):
    phone_string = ""
    if raw_phone:
        phone_string = phonenumbers.parse(raw_phone, "US")
        phone_string = phonenumbers.format_number(phone_string, phonenumbers.PhoneNumberFormat.NATIONAL)
    return phone_string


def yelp_to_salon_list_SF(search_term, yelp_ids_dict):
    search_results = yelp_api.Search(term=search_term, location="San Francisco, CA", radius_filter=6000, categories="beautysvc,othersalons")
    total_results = search_results.total

    offset = total_results % 20 - 1

    while offset < total_results:
        search_results_expanded = yelp_api.Search(term=search_term, offset=offset, location="San Francisco, CA", radius_filter=6000, categories="beautysvc,othersalons")
        for business in search_results_expanded.businesses:
            if business.name not in yelp_ids_dict:
                yelp_ids_dict[business.name] = { \
                'yelp_id': business.id, \
                'bus_lat': business.location.coordinate[u'latitude'], \
                'bus_long': business.location.coordinate[u'longitude'], \
                'address': address_formatted(business.location.address), \
                'phone': phone_formatted(business.phone)}
                print yelp_ids_dict[business.name]['phone']
        offset = offset + 20

    return yelp_ids_dict

yelp_ids_empty = {}
# yelp_ids_manicures = yelp_to_salon_list_SF('manicure', yelp_ids_empty)
# yelp_ids_manicures_nail_salons = yelp_to_salon_list_SF('nail salon', yelp_ids_manicures)
yelp_ids_manicures_nail_salons = yelp_to_salon_list_SF('nail salons', yelp_ids_empty)

print 'RETURNED THIS MANY MANICURES NAIL SALON PLACES WITHIN 6000m of San Francisco:'
print len(yelp_ids_manicures_nail_salons)

x = yelp_ids_manicures_nail_salons
with open('yelp_data.csv', 'wb') as f:
    writer = csv.writer(f, delimiter='|')
    for key, value in yelp_ids_manicures_nail_salons.items():
        writer.writerow([key.encode('ascii', 'ignore'), \
            value['yelp_id'].encode('ascii', 'ignore'), \
            value['bus_lat'], \
            value['bus_long'], \
            value['address'], \
            value['phone'].encode('ascii', 'ignore')])










