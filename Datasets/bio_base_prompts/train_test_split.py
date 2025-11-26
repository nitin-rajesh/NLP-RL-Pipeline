import json

with open("rlhf_output.json", mode='r') as f:
    rlhf_dict = json.loads(f.read())

train_dict = []
test_dict = []

for elem in rlhf_dict:
    if len(train_dict) < len(rlhf_dict)*0.85:
        train_dict.append(elem)

    else:
        test_dict.append(elem)

print("Total rows: ", len(rlhf_dict))
print("Train rows: ", len(train_dict))
print("test rows: ", len(test_dict))


with open("rlhf_train.json", mode='w') as fp:
    json.dump(train_dict, fp)

with open("rlhf_test.json", mode='w') as fp:
    json.dump(test_dict, fp)