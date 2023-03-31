breeds = {
    'Poodle': {'size': 'medium', 'activity': 'high', 'shedding': 'low'},
    'Labrador Retriever': {'size': 'large', 'activity': 'high', 'shedding': 'moderate'},
    'Chihuahua': {'size': 'small', 'activity': 'moderate', 'shedding': 'low'},
    'Golden Retriever': {'size': 'large', 'activity': 'high', 'shedding': 'high'},
    'Shih Tzu': {'size': 'small', 'activity': 'low', 'shedding': 'high'},
    'German Shepherd': {'size': 'large', 'activity': 'high', 'shedding': 'high'},
    'Boston Terrier': {'size': 'small', 'activity': 'moderate', 'shedding': 'low'},
    'Siberian Husky': {'size': 'medium', 'activity': 'high', 'shedding': 'high'},
    'Yorkshire Terrier': {'size': 'small', 'activity': 'moderate', 'shedding': 'low'},
    'Dalmatian': {'size': 'medium', 'activity': 'high', 'shedding': 'moderate'}
}

matches = []
size = input("What size of dog do you prefer? (small, medium, or large) ")
activity = input("How active do you want your dog to be? (low, moderate, or high) ")
shedding = input("What level of shedding can you tolerate? (low, moderate, or high) ")
email = input("What is your email address? ")
print()

for breed, traits in breeds.items():
    if traits['size'] == size and traits['activity'] == activity and traits['shedding'] == shedding:
        matches.append(breed)

if matches:
    print("Based on your preferences, we recommend the following breeds:")
    for breed in matches:
        print("- " + breed)
else:
    print("No breed can be selected")

print(matches)
