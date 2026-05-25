data = [
{
    "id": 6482,
    "country": "Spain",
    "items": 42,
},
{
    "id": 5632,
    "country": "Portugal",
    "items": 23,
}]

demand = int(input('Give me the id of the shipment:\n'))

def getShipment(data, shipment_id):
    for shipment in data:
        if shipment_id == shipment['id']:
            print("ID: " + str(shipment["id"]))
            print("Country: " + shipment["country"])
            print("Items: " + str(shipment["items"]))
            return
            
    print('Invalid ID of shipment.')


getShipment(data, demand)
