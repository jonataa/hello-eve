from eve import Eve

def add_people_fullname(response):
    for item in response['_items']:
        item['fullname'] = item['firstname'] + " " + item['lastname']

app = Eve()
app.on_fetched_resource_people += add_people_fullname
app.run(debug=True)
