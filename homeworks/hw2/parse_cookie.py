#!/usr/bin/env python3
def parse_cookie(query: str) -> dict:
    result = {}
    
    if 'name=' in query:
        query = query.split(';')

        try:
            for i in query:
                key, value = i.split('=', 1)
                if value:
                    result[key] = value
        except ValueError:
            pass

        if not (result.get('age')).isdigit():
            result.pop('age')
              
    return result

if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=***;') == {'name': '***'}
    assert parse_cookie('name=;age=;') == {}
    assert parse_cookie('name=Dima=User;age=28=10;') == {'name': 'Dima=User'}
    assert parse_cookie('=////====') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
