search-scope-check:
	src actions scope-query -f action.json

build:
	docker image pull node:13-alpine
	docker image build -t rxjs-upgrade .

exec:
	src actions exec -keep-logs -f action.json > diffs.json

campaign-plan:
	cat diffs.json | src campaign plan create-from-patches