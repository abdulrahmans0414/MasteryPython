# Undestanding the Offset and Appending items to lists

indian_states = [
    'Andhra Pradesh',
    'Arunachal Pradesh',
    'Assam',
    'Bihar',
    'Chhattisgarh',
    'Goa',
    'Gujarat',
    'Haryana',
    'Himachal Pradesh',
    'Jharkhand',
    'Karnataka',
    'Kerala',
    'Madhya Pradesh',
    'Maharashtra',
    'Manipur',
    'Meghalaya',
    'Mizoram',
    'Nagaland',
    'Odisha',
    'Punjab',
    'Rajasthan',
    'Sikkim',
    'Tamil Nadu',
    'Telangana',
    'Tripura',
    'Uttar Pradesh',
    'Uttarakhand',
    'West Bengal',
    'Andaman and Nicobar Islands',
    'Chandigarh',
    'Dadra and Nagar Haveli and Daman and Diu',
    'Delhi',
    'Lakshadweep',
    'Puducherry'
]
print(indian_states)

# at index 1
print(indian_states[1])

# change at index 2
indian_states[2] ="AP"
print(indian_states[2])

# add list using append in new state
indian_states.append("pok")
print(indian_states)

# in extend we as add list  indian states
indian_states.extend(['pakitan', 'khalistan','afganistan','bangladesh'])
print(indian_states)