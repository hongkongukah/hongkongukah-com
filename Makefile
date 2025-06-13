# SPDX-FileCopyrightText: 2025 HongKongukah.com
# SPDX-License-Identifier: MIT

.PHONY: start-prod
start-prod:
	docker compose -f docker/prod-docker-compose.yaml up -d --build

# TODO: Use NGINX container and app container
.PHONY: start-test
start-test:
	python manage.py runserver 127.0.0.1:8004

.PHONY: stop-prod
stop-prod:
	docker compose -f docker/prod-docker-compose.yaml down prod-hongkongukah --volumes

.PHONY: lint
lint:
	pre-commit run ruff --all-files

.PHONY: format
format:
	pre-commit run ruff-format --all-files

.PHONY: check
check:
	pre-commit run --all-files
