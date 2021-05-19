def parser(data):
    results = []
    for center in data['centers']:
        for session in center['sessions']:
            if session['min_age_limit'] == 18:
                temp = {
                    'age': '18+',
                    'address': center['address'],
                    'availability': session['available_capacity'],
                    'vaccine': session['vaccine'],
                    'pincode': center['pincode'],
                    'date': session['date'],
                    'center_id': center['center_id']
                }
                #print(temp)
                results.append(temp)
    return results
