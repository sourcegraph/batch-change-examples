install-cli-latest-macos:
	curl -L https://sourcegraph.com/.api/src-cli/src_darwin_amd64 -o /usr/local/bin/src
	chmod +x /usr/local/bin/src

clear-cache-macos:
	rm -fr $(HOME)/Library/Caches/sourcegraph-src/action-exec
