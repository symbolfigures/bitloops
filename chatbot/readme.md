# Bitloops Chatbot

A chatbot that answers questions about bitloops using the research paper and bitloop calculator.

It uses Model Context Protocol to let a LLM use these resources. 

![figure_1](figures/figure_1.drawio.png)

## Overview

The overal request flow is as follows:

1. The user asks a question using a chatbot interface.
2. An orchestrator sends the question to Anthropic Claude via AWS Bedrock API.
3. Claude makes a tool call if it thinks the resulting information will help answer the question.
4. The MCP client make the tool call to the MCP server.
5. The MCP server retrieves information from the available tools.

The path then continues in reverse, sending the information back to Claude, which provides a final answer.

![figure_2](figures/figure_2.drawio.png)

## Orchestration

The Orchestrator may call Claude several times as though multiple LLMs worked together as a group to figure out the right answer.

1. The Orchestrator initiates three identical sequences in parallel. Each sequence has a trio of responders.
2. The First Responder simply answers the question as one would expect, using tools as needed.
3. The Skeptic is asked to read the answer and point out anything it finds is incorrect.
4. The Arbiter reads both answers and synthesizes them into its own answer.
5. The Judge reads three answers and decides which one is the best, and returns it to the Orchestrator.

The Bedrock API includes a system prompt to define these [roles](mcp/roles.py).

### Performance

Here is an example question and a common outcome:

`Take the bitloop '1100101'. Is this bitloop equal to its link?`

The First Responder always gets this wrong. It uses the Bitloop Calculator to find the link of `1100101`, which is `0010111`, and says these bitstrings are not equal, hence the given bitloop is not equal to its link.

The Skeptic recognizes that a bitloop may be represented by any member of its rotation class, and both bitstrings `1100101` and `0010111` belong to the same rotation class. Therefore the bitloop is equal to its link.

The Arbiter agrees with the Skeptic and writes its own answer.

This only works about two thirds of the time. Hence three runs are executed, and a Judge compares them to determine what is the correct answer.

The system returns the correct answer for 80 of 100 trials.

Method|LLM calls|Accuracy
---|---|---
First Responder|1|0%
Trio (FR, Skeptic, Arbiter)|3|66%
Judge over three trios|10|80%

### Efficiency

The research paper is read by each LLM. Reading it once consumes about 30,000 tokens. Including cachePoint in the Bedrock API call caches this part of the system prompt, reducing input token usage by nearly 90%.

Another 70% of tokens (input and output) would be dropped if a single trio could get the question right 80% of the time. Of the remaining 30%, 20% of that would be dropped if the First Responder could get the question right 80% of the time.

### Next steps

Restructure research paper in a more LLM-friendly format, to help improve its interpretation of the content.


