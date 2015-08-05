import os
import yelp

yelp_api = yelp.Api(
    consumer_key=os.environ['YELP_CONSUMER_KEY'],
    consumer_secret=os.environ['YELP_CONSUMER_SECRET'],
    access_token_key=os.environ['YELP_ACCESS_TOKEN'],
    access_token_secret=os.environ['YELP_ACCESS_TOKEN_SECRET'])



def yelp_to_salon_list_SF(search_term, yelp_ids_dict):
    search_results = yelp_api.Search(term=search_term, location="San Francisco, CA", radius_filter=6000, categories="beautysvc,othersalons")
    total_results = search_results.total

    offset = total_results % 20 - 1

    while offset < total_results:
        search_results_expanded = yelp_api.Search(term=search_term, offset=offset, location="San Francisco, CA", radius_filter=6000, categories="beautysvc,othersalons")
        for business in search_results_expanded.businesses:
            if business.name not in yelp_ids_dict:
                yelp_ids_dict[business.name] = business.id
                print business.name, business.id
        offset = offset + 20


    return yelp_ids_dict

yelp_ids_empty = {}
# yelp_ids_manicures = yelp_to_salon_list_SF('manicure', yelp_ids_empty)
# yelp_ids_manicures_nail_salons = yelp_to_salon_list_SF('nail salon', yelp_ids_manicures)
yelp_ids_manicures_nail_salons = yelp_to_salon_list_SF('nail salon', yelp_ids_empty)

print 'RETURNED THIS MANY MANICURES NAIL SALON PLACES WITHIN 6000m of San Francisco:'
print len(yelp_ids_manicures_nail_salons)











