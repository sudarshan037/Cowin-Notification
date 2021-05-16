def parser(data):
    results = []
    for center in data['centers']:
        for session in center['sessions']:
            if session['min_age_limit'] == 18:
                temp = {
                    'age': '18+',
                    'address': center['address'],
                    'availablity': session['available_capacity'],
                    'vaccine': session['vaccine']
                }
                results.append(temp)   
    return results