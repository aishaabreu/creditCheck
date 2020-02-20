# creditCheck

This is a small personal credit availability check application.

[Download Latest Linux Version](https://github.com/feliperian/creditCheck/raw/master/dist/authorize)

## Script Usage
The data for each operation should be like this:
```
{ "transaction": { "id": 1, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-02-13T10:00:00.000Z"}}
```

The file must be passed as a parameter to the script as in the example:
```
python authorize.py operation
```

It is also possible to pass multiple files:
```
python authorize.py operationA operationB
```

## Dependences
Only python is needed:
[Python 3.7](https://www.python.org/downloads/)

## Running tests
Start unit tests using the following command:
```
python tests.py
```

## Compiling
Install python compile requirements:
```
pip install -r requirements.txt
```

And compile:
```
pyinstaller --onefile authorize.py
```

After compilation, the executable will be available on the path:
```
dist/authorize
```
