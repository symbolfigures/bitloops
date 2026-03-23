class Role:
	'''represents a role with a name, prompt template, and query template'''
	def __init__(self, name: str, prompt_template: str, query_template: str):
		self.name = name
		self.prompt_template = prompt_template
		self.query_template = query_template


first_responder = Role(
	name='first_responder',
	prompt_template='''You are the First Responder. Your role is to provide an initial analysis and answer to the query based on the research paper provided. Provide a clear, direct answer to the user's question, citing relevant sections from the paper.''',
	query_template='{query}'
)


skeptic = Role(
	name='skeptic',
	prompt_template='''You are the Skeptic. Your role is to critically examine the first responder's answer and identify potential flaws, missing considerations, or alternative interpretations. Challenge assumptions, point out gaps in reasoning, and suggest areas that need further consideration.''',
	query_template='''Original query: {query}

First Responder's answer:
{first_response}

Provide your critical analysis.'''
)


arbiter = Role(
	name='arbiter',
	prompt_template='''You are the Arbiter. Your role is to synthesize the first responder's answer and the skeptic's critique into a balanced, well-reasoned final response. Weigh the arguments, acknowledge valid concerns, and provide a comprehensive answer that addresses the original query.''',
	query_template='''Original query: {query}

First Responder's answer:
{first_response}

Skeptic's critique:
{skeptic_response}

Provide your final balanced response.'''
)


judge = Role(
	name='judge',
	prompt_template='''You have received three independent analyses of the same query, each produced by a deliberation process. Your task is to determine which responses are accurate, and provide your own answer to the query.''',
	query_template='''Original query: {query}

Response from Deliberation 1:
{deliberation_1}

Response from Deliberation 2:
{deliberation_2}

Response from Deliberation 3:
{deliberation_3}

DO NOT mention the deliberations. Only provide your own answer.'''
)
