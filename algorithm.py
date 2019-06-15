import hashlib

def hash_list():
	return str(hashlib.algorithms_guaranteed)

def hash_text(algorithm_array, text, pass_count):
	result_dict = {}
	# Type checking
	if type(pass_count) is not int:
		return [False, {"error": "Pass count should be of 'integer' type."}]
	elif type(text) not in [str, unicode]:
		return [False, {"error": "Text should be of 'string' type."}]
	elif type(algorithm_array) is not list:
		return [False, {"error": "Algorithm list should be of 'list' type."}]
	# Bounds checking
	avail_alg_set = set(algorithm_array) & set(hashlib.algorithms_guaranteed)
	if pass_count > 1000000 or pass_count <= 0:
		return [False, {"error": "Pass count should be larger than 0 and smaller than 1000000."}]
	elif len(avail_alg_set) is 0:
		return [False, {"error": "None of these hash algorithms are available."}]
	# There is no error case; do the hash computations for every function
	for function in avail_alg_set:
		hash_val = text
		for _ in xrange(pass_count):
			hash_val = getattr(hashlib, function)(hash_val).hexdigest()
		result_dict[function] = hash_val
	return [True, result_dict]
