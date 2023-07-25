# Запуск проекта
- Сборка: `docker compose --env-file=.env.template build`
- Запуск миграций: `docker compose --env-file=.env.template run backend alembic upgrade head`
- Запуск бэкенда: `docker compose --env-file=.env.template up -d`
- Импорт `menu app.postman_collection.json` и `menu app.postman_environment.json` в Postman
- Запускаем тесты (без папки api)
