http POST localhost:5000/people firstname=John # lastname missing error
http POST localhost:5000/people firstname=John lastname=Doe
http POST localhost:5000/people firstname=Fizz lastname=Buzz role:='["copy", "author"]'
echo '{"firstname": "Foo", "lastname": "Bar", "role": ["author"]}' | http POST localhost:5000/people
http localhost:5000/people max_results==1
http localhost:5000/people where=='{"firstname": "John"}'
