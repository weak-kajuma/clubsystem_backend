# clubsystem_backend

このソフトはClubsystemのバックエンドをなしています

## Deployの方法

```
$ docker-compose build
$ docker-compose run --entrypoint "poetry install" clubsystem
$ docker-compose up -d --build
```
