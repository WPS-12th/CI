## CI

[![codecov](https://codecov.io/gh/WPS-12th/CI/branch/master/graph/badge.svg)](https://codecov.io/gh/WPS-12th/CI)

### Django기본 테스트

```
python manage.py test
```



### [Coverage.py](https://coverage.readthedocs.io/en/coverage-5.0.3/)

테스트 코드를 실행했을 때, 전체 소스 코드 중 몇%가 실행되었는지 확인

```
poetry add coverage
```

**설정파일 (`.coveragerc`)**

```
[run]
# app폴더안의 내용을 검사
source =
    app

# 지정한 경로는 리포트에서 제외
omit =
    app/manage.py
    app/config/asgi.py
    app/config/wsgi.py
```



### pytest, pytest-django

Django기본 테스트 대신, pytest를 사용

```
poetry add pytest pytest-django
pytest app
```



### codecov

codecov.io에 테스트 리포트를 쉽게 업로드 할 수 있도록 도와주는 라이브러리

### pytest-cov

pytest를 사용해서 codecov.io에 업로드 할 리포트를 만들어주는 라이브러리

```
poetry add codecov pytest-cov
pytest --cov app
CODECOV_TOKEN=<codecov.io Token> codecov
```

