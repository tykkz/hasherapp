test:
	python test_algorithm.py

codeclimate:
	coverage run test_algorithm.py
	coverage report --omit test_algorithm
	coverage html --omit test_algorithm
	codeclimate-test-reporter
