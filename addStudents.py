import requests

# Example student data
student_1 = {
    "username":"ArnavJyo0",
    "full_name": "Arnav Jyotshi",
    "age": 20,
    "address": {"city": "Gurgaon", "country": "India"},
    "interests": ["Reading", "Music"]
}
student_2 = {
    "username":"Yash1011",
    "full_name": "Yash Nigam",
    "age": 22,
    "address": {"city": "Nagpur", "country": "India"},
    "interests": ["Sports", "Travel"]
}
student_3 = {
    "username":"Parth1023",
    "full_name": "Parth Vyas",
    "age": 23,
    "address": {"city": "Mumbai", "country": "India"},
    "interests": ["Sports", "Cooking","Finance"]
}
student_4 = {
    "username":"Guddu1",
    "full_name": "Shreeyanshu Swain",
    "age": 19,
    "address": {"city": "Kurukshetra", "country": "India"},
    "interests": [ "Cooking","Cars"]
}
student_4 = {
    "username":"Shashank1233",
    "full_name": "Shashank Goel",
    "age": 23,
    "address": {"city": "Gurgaon", "country": "India"},
    "interests": ["Finance","Cars","Travel"]
}
student_5 = {
    "username":"Kavi0",
    "full_name": "Kavish Jyotshi",
    "age": 12,
    "address": {"city": "Gurgaon", "country": "India"},
    "interests": ["Finance","Cars","Football","Games"]
}
student_6 = {
    "username":"Jai0",
    "full_name": "Jai Garg",
    "age": 20,
    "address": {"city": "Palwal", "country": "India"},
    "interests": ["Programming","Geopolitics","History"]
}
student_7 = {
    "username":"Chetan12",
    "full_name": "Chetan Dixit",
    "age": 24,
    "address": {"city": "Palwal", "country": "India"},
    "interests": ["Theatre","Movies","Selfhelp"]
}

student_8 = {
    "username":"Naman123",
    "full_name": "Naman Jain",
    "age": 25,
    "address": {"city": "Hisar", "country": "India"},
    "interests": ["Movies","Nature","Pets"]
}
student_9 = {
    "username":"Varun123",
    "full_name": "Varun Singla",
    "age": 21,
    "address": {"city": "Faridabad", "country": "India"},
    "interests": ["Movies","Cars","Bikes"]
}
student_10 = {
    "username":"Saransh12",
    "full_name": "Saransh Vats",
    "age": 21,
    "address": {"city": "Delhi", "country": "India"},
    "interests": ["Movies","Selfhelp"]
}



# URL for the post request
url = "http://127.0.0.1:8000/students"

# Make the post request to create a new student
response_1 = requests.post(url, json=student_1)
response_2 = requests.post(url, json=student_2)
response_3 = requests.post(url, json=student_3)
response_4 = requests.post(url, json=student_4)
response_5 = requests.post(url, json=student_5)
response_6 = requests.post(url, json=student_6)
response_7 = requests.post(url, json=student_7)
response_8 = requests.post(url, json=student_8)
response_9 = requests.post(url, json=student_9)
response_10 = requests.post(url, json=student_10)

# Print the response
print("Response 1:", response_1.json())
print("Response 2:", response_2.json())
print("Response 3:", response_3.json())
print("Response 4:", response_4.json())
print("Response 5:", response_5.json())
print("Response 6:", response_6.json())
print("Response 7:", response_7.json())
print("Response 8:", response_8.json())
print("Response 9:", response_9.json())
print("Response 10:", response_10.json())
