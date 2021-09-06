# get years
```python
from datetime import datetime
post = Post.query.order_by(Post.id.desc()).all()
year = []
for post in posts:
    year.append(post.timestamp.strftime('%Y'))
```

year
```bash
output: ['2020', '2021', '2021', '2021']
```
# get unique years
```python
unique_set = set()
for year in years:
  unique_set.add(year)
  
unique_set_list = list(unique_set)
```
## Run a for loop and if statement to get years and months

```python
for post in posts:
  if post.timestamp.strftime('%Y') == "2020" and post.timestamp.strftime('%B') == "April": 
          print(post.body)
```
```
