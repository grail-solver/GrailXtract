## GrailXtract
GrailXtract is a Python library that uses the GPT-3 model to extract important information from plain text, such as variables, constraints, and domains. It serves as the first layer of the 'gail-cp-solver' package, and can create a CP (constraint programming) model from the extracted data and solve it. The library makes it easy to extract data from plain text and format it according to a predefined protocol.

### Usage
To use the GrailXtract library, you can simply import the grail_extractor function from core.helper and pass your text problem as a string to the function. An example of how to use the library is shown below:

```python
# sample.py

from xtractor.core.helper import grail_extractor

problem = """
A farmer has $1000. With the $1000, he wishes to buy 100 animals of different species: 
chicks, pigs, and cows. It is assumed that a chick costs $5, a pig costs $50, and a cow 
costs $100. He wants to have at least 1 animal of each species and wants to spend all of 
the $1000 he has. How many chicks, pigs, and cows should he buy?
"""

if __name__ == '__main__':
    output = grail_extractor(problem)
    print(output)
```

### Ouput
The library first uses utils.protocol.prompt_builder to create a prompt describing the output format, task to be performed, and the problem statement. It then utilizes utils.llm.gpt to process the prompt using the GPT model. Finally, it uses utils.parser to ensure that the data is properly formatted and returns the resulting JSON string as shown below.

```json
{
  "llm_status": "success",
  "constraints": [
    {
      "left_part": [[1, "Var_1"], "+", [1, "Var_2"], "+", [1, "Var_3"]],
      "relation": "=",
      "right_part": [100]
    },
    {
      "left_part": [[5, "Var_1"], "+", [50, "Var_2"], "+", [100, "Var_3"]],
      "relation": "=",
      "right_part": [1000]
    },
    {
      "left_part": [[1, "Var_1"]],
      "relation": ">=",
      "right_part": [1]
    },
    {
      "left_part": [[1, "Var_2"]],
      "relation": ">=",
      "right_part": [1]
    },
    {
      "left_part": [[1, "Var_3"]],
      "relation": ">=",
      "right_part": [1]
    }
  ],
  "variables": [
    {"id": 1, "name": "chicks", "type": "Integer", "domaine_type": "INTERVAL", "domaine_values": "[1,100]"},
    {"id": 2, "name": "pigs", "type": "Integer", "domaine_type": "INTERVAL", "domaine_values": "[1,100]"},
    {"id": 3, "name": "cows", "type": "Integer", "domaine_type": "INTERVAL", "domaine_values": "[1,100]"}
  ]
}
```

### Common Error
The status of the LLM (Language Model) request will be "success" in the JSON file if it is executed without errors, otherwise it will be "fail". In case of a failure, you can access the "llm_trace" index to get more information about the error.

* Success:
```json
{
  "llm_status": "success",
  "constraints": [],
  "variables": []
}
```

* Error:
```json
{
  "llm_status": "fail",
  "llm_trace": "Error: Could not find variables in the text"
}
```

### Installation
* Clone this repository.
* cd into GrailXtract folder
* Install dependencies using:
```bash
pip install -r requirements.txt
```
* Create your env file by running:
```bash
cp .env.sample .env
```
* Set up your GPT api key (OPENAI_API_KEY) in the .env file 
* You can import the helper method in any python file of your project and start using the library


### Dependencies
- python
- openai 
- dotenv
- json

### Library Structure
```
GrailXtract/xtract
.
├── README.md
├── requirements.txt
├── .env.sample
├── .env
├── core
│   ├── __init__.py
│   └── helper.py
├── utils
│   │   ├── llm
│   │   │   ├── __init__.py
│   │   │   └── gpt.py
│   │   ├── parser
│   │   │   ├── parser.py
│   │   │   └── equation.py
│   │   └── protocol
│   │       ├── __init__.py
│   │       ├── prompt_builder.py
│   │       ├── constraints
│   │       │   ├── pconstraint_1.txt
│   │       │   └── constraint_2.txt
│   │       └── variables
│   │           └── variable_1.txt
└── test
    ├── case
    ├── test.py
```

### Contribution
Contributions are welcome and encouraged! If you find a bug or have an idea for a new feature, please feel free to create a pull request. 
If you're new to contributing to open source projects, don't worry! We welcome contributors of all skill levels and will do our best to provide guidance and support throughout the process.

Here are some ways you can contribute:

- Report bugs or suggest new features by opening an issue on GitHub
- Submit a pull request to fix a bug or add a new feature
- Help improve the documentation by suggesting changes or additions

If you're not sure where to start or how you can help, feel free to reach out to us! We're always happy to answer questions and provide guidance.

With love, GrailSolver Team