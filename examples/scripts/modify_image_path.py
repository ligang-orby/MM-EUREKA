import json

data_path = '/MM-Eureka-Dataset/dataset.jsonl'
out_data_path = '/MM-Eureka-Dataset/new_dataset.jsonl'

with open(out_data_path, 'w') as of:
    with open(data_path, 'rb') as f:
        for l in f:
            example = json.loads(l)
            image_urls = example['image_urls']
            new_urls = ['file:///MM-Eureka-Dataset/' + url for url in image_urls]
            images = [{"type": "image", "image": url} for url in new_urls]
            message = example['conversations']
            message = [m for m in message if m['role'] == 'user']
            message = [{"type": "text", "text": m['content'].replace('<image>', '').strip()} for m in message]
            message = images + message
            message = [{'role': 'user', 'content': message}]            
            example['message'] = json.dumps(message)
            del example['image_urls']
            del example['conversations']
            of.write(json.dumps(example) + '\n')


