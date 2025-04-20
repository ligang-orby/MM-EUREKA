import json

data_path = '/MM-Eureka-Dataset/dataset.jsonl'
out_data_path = '/MM-Eureka-Dataset/new_dataset.jsonl'

with open(out_data_path, 'w') as of:
    with open(data_path, 'rb') as f:
        for l in f:
            example = json.loads(l)
            image_urls = example['image_urls']
            new_urls = ['file:///MM-Eureka-Dataset/' + url for url in image_urls]
            example['image_urls'] = new_urls
            example['message'] = example['conversations']
            of.write(json.dumps(example) + '\n')


