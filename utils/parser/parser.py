import re


def parse_text(text):
    # replace newlines and spaces with empty string
    flat_text = text.replace("\n", "").replace(" ", "").replace("(", "").replace(")", "")
    print(flat_text)

    # Define regex patterns for variables and equations
    variable_pattern = r"Variables:{(.*)}"
    equation_pattern = r"Constraints:{(.*)}"

    # Check if the patterns match in the text
    if not re.search(variable_pattern, flat_text, re.DOTALL):
        raise ValueError("Could not find variables in the text")

    if not re.search(equation_pattern, flat_text, re.DOTALL):
        raise ValueError("Could not find equations in the text")

    # Extract the variables and equations from the text
    variables_text = re.search(variable_pattern, flat_text.split('Constraints')[0]).group(1)
    equations_text = re.search(equation_pattern, 'Constraints' + flat_text.split('Constraints')[1]).group(1)

    return variables_text, equations_text


def format_variables(variables_text):
    print('-------')
    print(variables_text)

    variables = {}
    for variable_match in re.findall(r"(\w+):{(.+?)}", variables_text):
        variable_name = variable_match[0]
        variable_text = "{" + variable_match[1] + "}"
        variable = eval(variable_text)
        variables[variable_name] = variable

    variables_array = [variable for variable in variables.values()]
    return variables_array


def format_constraints(equations_text):
    equation_array = eval("{" + equations_text + "}")
    equation_array = [equation for equation in equation_array.values()]
    print(equation_array)

    # Operators
    operators = ["*", "+", "/", "-", "<", ">", "<=", ">=", "=", "!="]
    relations = ["<", ">", "<=", ">=", "=", "!="]

    # Create empty list for storing formatted equations
    formatted_equations = []

    for equation in equation_array:
        equation_parts = []
        current_part = ""

        for char in equation:
            if char in operators:
                if current_part != "":
                    equation_parts.append(current_part)
                current_part = ""
                equation_parts.append(char)
            else:
                current_part += char

        if current_part != "":
            equation_parts.append(current_part)

            # Determine left and right parts of the equation based on the first relation found
            left_part = []
            right_part = []
            relation = None

            for part in equation_parts:
                if relation:
                    right_part.append(part.strip())
                elif part in relations:
                    relation = part
                else:
                    left_part.append(part.strip())

            # PAS TESTÉ - START
            parts_list = []
            temp = []
            for part in equation_parts:
                if part.startswith("Var"):
                    var_name = part.split("_")[1]
                    var_coeff = float(temp.pop()) if temp else 1
                    parts_list.append((var_coeff, var_name))
                else:
                    temp.append(part)
            if temp:
                parts_list.append(("".join(temp),))

            print("++++++")
            print(equation)
            print(left_part)
            print(right_part)
            print(relation)
            # PAS TESTÉ - END




    for equation_string in equation_array:
        equation = {}
        equation_string = equation_string.strip()
        equation_parts = []
        part = ""

        for char in equation_string:
            if char in operators:
                equation_parts.append(part.strip())
                part = char
            else:
                part += char

        equation_parts.append(part.strip())
        print(equation_parts)


        # Determine left and right parts of the equation based on the first relation found
        left_part = []
        right_part = []
        relation = None

        for part in equation_parts:
            if relation:
                right_part.append(part.strip())
            elif part in relations:
                relation = part
            else:
                left_part.append(part.strip())

        print("++++++")
        print(equation_string)
        print(left_part)
        print(right_part)
        print(relation)

        # Split the left and right parts into variable/coefficient pairs and operators/constants
        left_vars = []
        left_consts = []
        left_op = None

        for part in left_part:
            if part in operators:
                left_op = part
            else:
                if left_op:
                    left_consts.append(int(part))
                else:
                    var_name = part.split("_")[0]
                    var_coeff = int(part.split("_")[1])
                    left_vars.append((var_coeff, var_name))

        right_vars = []
        right_consts = []
        right_op = None

        for part in right_part:
            if part in operators:
                right_op = part
            else:
                if right_op:
                    right_consts.append(int(part))
                else:
                    var_name = part.split("_")[0]
                    var_coeff = int(part.split("_")[1])
                    right_vars.append((var_coeff, var_name))

        # Format the equation dictionary with the left and right parts
        equation["left"] = {
            "vars": left_vars,
            "op": left_op,
            "consts": left_consts
        }

        equation["right"] = {
            "vars": right_vars,
            "op": right_op,
            "consts": right_consts
        }

        equation["relation"] = relation

        formatted_equations.append(equation)

    return formatted_equations
