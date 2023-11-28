build:
	docker build -t fl_test .
run:
	docker run -d --name fl_test_cont -v ./proj:/proj fl_test

debug:
	docker exec -it fl_test_cont /bin/bash

clean:
	docker kill fl_test_cont
	docker image rm -f fl_test
	docker container rm -f fl_test_cont
	docker image prune -a; docker system prune -a --volumes;