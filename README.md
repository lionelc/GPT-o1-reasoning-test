# Testing the reasoning capability for OpenAI o1 model

## Background and Introduction
There have been debates on LLM's reasoning capabilities. While there are always voices on "LLM cannot really reason", backed by recent papers [Procedural Knowledge in Pretraining Drives Reasoning in LLMs](https://arxiv.org/pdf/2411.12580) and [Do LLMs Really Think Step-by-step In Implicit Reasoning?](https://arxiv.org/abs/2411.15862), others consider this is solvable by adding extra steps to model training. Also, [Chain-of-thoughts](https://arxiv.org/abs/2201.11903) does enable LLMs to tackle complex reasoning tasks.

Notably, OpenAI releases its o1 model and the [results](https://openai.com/index/learning-to-reason-with-llms/) shows significant improvement over gpt-4o in solving competition math and programming contests. 

In this test, we feed such 2 logic puzzles to o1-preview and o1-mini (while o1 is accessible to premium customers only) via API: [Apple Thief Puzzle](https://math.stackexchange.com/questions/2019892/guess-who-is-the-apple-thief) and [Zebra Puzzle](https://en.wikipedia.org/wiki/Zebra_Puzzle) (also called Einstein's Puzzle).

While o1-preview/o1-mini can crack the easier apple thief puzzle correctly every time, it shows unstability for the more difficult Zebra Puzzle. Moreover, when we swap a couple of feature names in the Zebra Puzzle (which doesn't change the nature or difficulty at all), o1-preview's correctness rate drops considerably.  

As the Zebra Puzzle is well-known enough to be included in training data, does that mean LLM still tries to retrieve the original question from its "memory"? Normally, we would assume a logical computer model can solve every problem the same way, or a competent person who doesn't know this puzzle before should always find the correct answer. The test results show that LLM, or models like o1 that can reason, don't fit this type but have bias -- it even came up with the same answer as if those names were not swapped at all. 

## How to run it
It's basically a simple call on OpenAI API, and each puzzle and the variants (after name swapping) are specified in json files as input.

When you have all the python packages installed, run it like

`python o1_reason_test.py zebra_puzzle_swap1.json`

## Results

| Puzzle                        |  Model     |  Correctness      |
| ------------------------------| ---------- |  ---------------- |
|  Apple thief original         | o1-mini    |     10/10         |
|  Apple thief swapped          | o1-mini    |     10/10         |
|  Zebra original (2 questions) | o1-preview |     10/10         |
|  Zebra original (2 questions) | o1-mini    |     10/10         |
|  Zebra original (4 questions) | o1-preview |      8/10         |
|  Zebra original (4 questions) | o1-mini    |      9/10         |
|  Zebra swapped  (4 questions) | o1-preview |      4/10         |
|  Zebra swapped  (4 questions) | o1-mini    |      3/10         |

