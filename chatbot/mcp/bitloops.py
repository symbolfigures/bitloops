from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

# initialize FastMCP server
mcp = FastMCP('bitloops')

BITCALC_API_BASE = 'https://symbolfigures.io/api/bitloops/calc'
USER_AGENT = 'bitloops-app/1.0'


# helper functions to query and format data from bitloops API

async def make_bitcalc_request(url: str) -> dict[str, Any] | None:
	'''make a request to the Bitcalc API with proper error handling'''
	headers = {'User-Agent': USER_AGENT, 'Accept': 'application/json'}
	async with httpx.AsyncClient() as client:
		try:
			response = await client.get(url, headers=headers, timeout=30.0)
			response.raise_for_status()
			return response.json()
		except Exception:
			return None


def format_response(response: dict) -> str:
	'''format response into a readable string'''
	return f'''
Properties of the given bitstring and its respective bitloop, tree, chain, and graph:

Bitstring:
- Number of bits: {response['bs_num_bits']}
- Parity: {response['bs_parity']}
- Inverse: {response['bs_inverse']}
- Reverse: {response['bs_reverse']}
- Pattern: {response['bs_pattern']}

Bitloop:
- Symmetry: {response['bl_symmetry']}
- Link: {response['bl_link']}
- Sublink: {response['bl_sublink']}
- Minimum value rotation: {response['bl_mvrot']}

Tree:
- Root: {response['tr_root']}
- Structure: {response['tr_structure']}
- Number of levels: {response['tr_num_levels']}
- Number of bitloops: {response['tr_num_bl']}
- Number of bitstrings: {response['tr_num_bs']}
- Bitloops: {response['tr_ls_bl']}

Chain:
- Number of trees: {response['ch_num_trees']}
- Roots: {response['ch_ls_roots']}
- Minimum value rotation: {response['ch_mvroo']}

Graph:
- Number of bitstrings: {response['gr_num_bs']}
- Number of bitloops: {response['gr_num_bl']}
- Number of symmetric chains: {response['gr_num_sym_chains']}
- Symmetric chains: {response['gr_ls_sym_chains']}
- Number of asymmetric chains: {response['gr_num_asym_chains']}
- Asymmetric chains: {response['gr_ls_asym_chains']}
- Number of graphs: {response['gr_num_graphs']}
- Graphs: {response['gr_ls_graphs']}
'''


# tool execution handler

@mcp.tool()
async def get_properties(state: str) -> str:
	"""Get properties of a given bitstring.

	Args:
		bitstring: String of consecutive 1's and 0's (example: 1100101)
	"""
	url = f'{BITCALC_API_BASE}?bitstring={state}'
	response = await make_bitcalc_request(url)

	if not response:
		return 'unable to fetch bitstring properties'

	properties = format_response(response)
	return properties#'\n---\n'.join(properties)


# research execution handler

@mcp.resource('research://bitloops-paper')
async def get_paper() -> str:
	async with httpx.AsyncClient(timeout=30.0) as client:
		#response = await client.get('https://symbolfigures.io/bitloops.html')
		response = await client.get('https://symbolfigures.io/bitloops/bitloops.yml')
		return response.text


# initialize and run server

def main():
	mcp.run(transport='stdio')


if __name__ == '__main__':
	main()













































