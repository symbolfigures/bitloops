import asyncio
import sys
import json
import re
from datetime import datetime
from main import MCPClient

QUESTION = "Take the bitloop '1100101'. Is this bitloop equal to its link?"
NUM_ITERATIONS = 10
RESULTS_FILE = 'test_results_t={temperature}.json'


def extract_answer(response_text):
	'''extract first occurrence of "yes" or "no"'''
	if not response_text:
		return None
	match = re.search(r'\b(yes|no)\b', response_text, re.IGNORECASE)
	if match:
		return match.group(1).lower()
	return None


async def run_test(temperature):
	'''run orchestrate_layer_2 NUM_ITERATIONS times and save results as JSON.'''

	# init MCP client
	client = MCPClient(temperature)
	await client.connect_to_server('bitcalc.py')

	test_start_time = datetime.now()

	results = {
		'question': QUESTION,
		'num_iterations': NUM_ITERATIONS,
		'temperature': temperature,
		'iterations': []
	}

	# run iterations
	for i in range(1, NUM_ITERATIONS + 1):
		print(f'\nTEMPERATURE: {temperature}\nITERATION NUMBER: {i}/{NUM_ITERATIONS}\n', file=sys.stderr)

		start_time = datetime.now()
		iteration_result = {
			'iteration': i
		}

		try:
			response = await client.orchestrate_layer_2(QUESTION)
			iteration_result['response'] = response
			iteration_result['success'] = True

			# extract and log answer
			answer = extract_answer(response)
			iteration_result['answer'] = answer

		except Exception as e:
			iteration_result['error'] = str(e)
			iteration_result['success'] = False
			iteration_result['answer'] = None

		end_time = datetime.now()
		iteration_result['duration_seconds'] = round((end_time - start_time).total_seconds(), 2)
		results['iterations'].append(iteration_result)

	test_end_time = datetime.now()
	results['avg_duration_seconds'] = round((test_end_time - test_start_time).total_seconds() / NUM_ITERATIONS, 2)

	# calculate percentage of yes answers
	yes_count = 0
	for n in range(NUM_ITERATIONS):
		if results['iterations'][n]['answer'] == 'yes':
			yes_count += 1
	yes_percentage = (yes_count / NUM_ITERATIONS * 100)
	results['accuracy'] = round(yes_percentage, 2)

	# save results
	with open(RESULTS_FILE.format(temperature=temperature), 'w') as f:
		json.dump(results, f, indent=2)

	# cleanup
	await client.cleanup()


async def simple():
	client = MCPClient()
	await client.connect_to_server('bitcalc.py')
	response = await client.orchestrate_layer_2(QUESTION)
	await client.cleanup()


def compare_temperatures():
	for i in range(1, 11, 1):
		temperature = i / 10
		asyncio.run(run_test(temperature))


if __name__ == '__main__':
	simple()
	#compare_temperatures()












