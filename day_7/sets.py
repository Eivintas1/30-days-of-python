it_companies = {"Google", "Amazon", "Facebook", "Apple"}
eng_companies = {"IBM", "Intel", "Cisco", "Apple"}
print(it_companies)

len_it_companies = len(it_companies)
print("Number of IT companies:", len_it_companies)
it_companies.add("Microsoft")
it_companies.add("Netflix")

print ("Updated IT companies:", it_companies)

it_companies.remove("Facebook")
print("After removing Facebook:", it_companies)

#diffrence between remove and discard is that remove will raise an error if the item is not found, while discard will not raise an error.
it_companies.discard("Microsoft")  # No error if Microsoft is not found
print("After discarding Microsoft (no error if not found):", it_companies)

joint = it_companies.union(eng_companies)
print("Union of IT and Engineering companies:", joint)

joint.intersection(it_companies)
print("Intersection of joint and IT companies:", joint.intersection(it_companies))