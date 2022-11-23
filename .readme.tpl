# [xpubsub](https://pypi.org/project/xpubsub)
A basic pubsub module for communications within an app.

This project is an excercise to help me develop skills relating to:

+ writing a Python module
+ publishing modules on pypi
+ using:
	+ [git](https://pypi.org/project/git)
	+ [pytest](https://pypi.org/project/pytest)
	+ [pyenv](https://pypi.org/project/pyenv)
	+ [poetry](https://pypi.org/project/poetry)
	+ [mypy](https://pypi.org/project/mypy)
	+ [tox](https://pypi.org/project/tox)

You would probably be better off using [PyPubSub](https://pypi.org/project/PyPubSub/)

## Interface
```python
from xpubsub import PubSub
pub = PubSub()

HashOrList = Union[Hashable, list[Hashable]]

pub.add(topic_list: HashOrList, callback: Callable):
pub.remove(topic_list: HashOrList, callback: Callable):
pub.send(topic_list: HashOrList, message: Any):
```

## Example: example.py
```python
{%I example.py
```
Output
```
{%R example.py
```



