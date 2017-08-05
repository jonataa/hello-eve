http localhost:5000/emails
http POST localhost:5000/emails author=5985513dd8004489a5393c7f subject='Hello World' body='This is a hello world'
http localhost:5000/emails embedded=='{"author": 1}'