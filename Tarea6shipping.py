shipping_cost_per_kg = 1.20
customer_basket_cost = 34
customer_basket_weight = 44
if(customer_basket_cost >= 100):
    print("Free shipping")
else:
    shipping_cost = customer_basket_weight * shipping_cost_per_kg
    customer_cost = shipping_cost + customer_basket_cost

print ("total basket cost incluidin shipping is" + str(customer_cost))
# https://www.figma.com/proto/w9fhJf3WYddTLNtUtjPfcY/primer-diagrama?node-id=3%3A2&scaling=min-zoom&page-id=0%3A1