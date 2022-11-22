# Communion_api

You can test the api as it is running right now on a server.

```
import requests
import json
base = 'http://ec2-44-211-170-250.compute-1.amazonaws.com:5000/productquery'
data = {
        'product_type':'Cosmetics', 'threshold': '0.5', 'query':'I am looking for a deeply hydrate, condition and lockin moisture.'
        }
response = requests.post(url=base, data= json.dumps(data))
print(response.text)
```


```
import requests
import json
base = 'http://ec2-44-211-170-250.compute-1.amazonaws.com:5000/productquery'
data = {
        'product_type':'Moshka', 'threshold': '0.5', 'query':'I am looking for fidget ring.'
        }
response = requests.post(url=base, data= json.dumps(data))
```

with threshold is the cutoff whether there is a result or not. The reply payload should look like this.

```
{"Product": {"Anxiety Fidget Ring": "WHAT IS A FIDGET RING? We developed an anxiety ring and fidget tool to help ease your anxiety by givingyou something to fidget with. The ring distracts you from constant worries bykeeping you grounded and providing a distraction from negativethoughts. Meditation rings can have calming effects for stress and anxietyrelief while serving as an aesthetic piece of jewelry that won't tarnish, rust,or corrode. According to Niru Ahmed, PhD and behavioral psychologist, 'ananxiety ring can be useful in providing a tool for that repetitive action andprovide a distraction for the hands.'Material Grade 316 Stainless Steel Dimension  Adjustable Sizing CoatingHypoallergenic"}, "status": "success"}
```


If you want to host it yourself, you can either:
```
python app.py
```
or use gunicorn replacing port with whatever port you want.
```
gunicorn app:app -b 0.0.0.0:port
```
