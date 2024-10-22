def generate_reports():
    reports = []
    
    # Function to create static records
    def create_record(first_name, last_name, age, gender, dob):
        return {'first_name': first_name, 'last_name': last_name, 'age': age, 'gender': gender, 'dob': dob}
    
    # Predefined static records for each case
    static_data = [
        {
            'code': 'EC01',
            'description': 'Edge Case 1',
            'records': [
                create_record('John', 'Doe', 23, 'Male', '25/10/1997'),
                create_record('Alice', 'Brown', 30, 'Female', '05/02/1994'),
                create_record('Charlie', 'Wilson', 27, 'Male', '12/08/1997')
            ]
        },
        {
            'code': 'EC02',
            'description': 'Edge Case 2',
            'records': [
                create_record('Lucas', 'Green', 38, 'Male', '12/03/1986'),
                create_record('Olivia', 'Scott', 22, 'Female', '08/09/2001'),
                create_record('Henry', 'Adams', 31, 'Male', '25/06/1993')
            ]
        },
        {
            'code': 'EC03',
            'description': 'Edge Case 3',
            'records': [
                create_record('James', 'Hughes', 40, 'Male', '10/05/1983'),
                create_record('Lily', 'Morgan', 27, 'Female', '18/09/1996'),
                create_record('Jack', 'Wright', 35, 'Male', '07/12/1988')
            ]
        },
        # Add static data for remaining cases EC04 to EC13...
    ]
    
    # Loop to generate reports with records1, records2, etc.
    for case in static_data:
        report = {
            'code': case['code'],
            'description': case['description'],
            'col1': True,  # You can adjust this logic based on specific cases
            'col2': False,
            'col3': True,
            'firstMatched': True,
            'secondMatched': False,
            'thirdMatched': True,
            'records1': case['records'],
            'records2': case['records'],  # Same data for records2
            'records3': case['records'],  # Same data for records3
            'records4': case['records'],  # Same data for records4
            'records5': case['records'],  # Same data for records5
            'records6': case['records']   # Same data for records6
        }
        
        reports.append(report)
    
    return reports

# Call the function to generate the reports
report = generate_reports()
