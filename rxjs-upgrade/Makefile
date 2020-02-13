search-scope-check:
	src actions scope-query -f action.json

build:
	docker image pull node:13-alpine
	docker image build -t rxjs-upgrade:latest .

exec:
	src actions exec -timeout 15m -keep-logs -f action.json > diffs.json

campaign-plan:
	cat diffs.json | src campaign plan create-from-patches

upgrade-rxjs-docker-command:
	git clone https://github.com/sourcegraph/codeintellify.git
	cat rxjs-upgrade.sh | docker container run \
		--name rxjs-upgrade \
		--rm \
		-i \
		--workdir /work \
		-v $(PWD)/codeintellify:/work \
		node:13-alpine sh
	cd codeintellify && git --no-pager diff
	rm -fr codeintellify
