{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f539b0ef-172c-4952-9aad-f31094aeeb54",
   "metadata": {},
   "source": [
    "# File Handling\n",
    "### Calculator Program 2.0\n",
    "*** OLALEKAN P ELEBUTE ***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "b4ad3b3b-ce4a-4a91-9df7-8b09b96d0065",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "\n",
    "class Calculator:\n",
    "    def __init__(self):\n",
    "        self.operations = {\n",
    "            '+': self.add,\n",
    "            '-': self.subtract,\n",
    "            '*': self.multiply,\n",
    "            '/': self.divide\n",
    "        }\n",
    "\n",
    "    def add_operation(self, symbol, function):\n",
    "        self.operations[symbol] = function\n",
    "\n",
    "    def calculate(self, num1, operation, num2):\n",
    "        if operation not in self.operations:\n",
    "            raise ValueError(f\"Operation '{operation}' is not supported.\")\n",
    "        \n",
    "        if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):\n",
    "            raise ValueError(\"Both inputs must be numbers.\")\n",
    "        \n",
    "        return self.operations[operation](num1, num2)\n",
    "\n",
    "    def add(self, a, b):\n",
    "        return a + b\n",
    "\n",
    "    def subtract(self, a, b):\n",
    "        return a - b\n",
    "\n",
    "    def multiply(self, a, b):\n",
    "        return a * b\n",
    "\n",
    "    def divide(self, a, b):\n",
    "        if b == 0:\n",
    "            raise ValueError(\"Cannot divide by zero.\")\n",
    "        return a / b\n",
    "\n",
    "def exponentiate(a, b):\n",
    "    return a ** b\n",
    "\n",
    "def square_root(a, _):\n",
    "    if a < 0:\n",
    "        raise ValueError(\"Cannot take the square root of a negative number.\")\n",
    "    return math.sqrt(a)\n",
    "\n",
    "def logarithm(a, _):\n",
    "    if a <= 0:\n",
    "        raise ValueError(\"Logarithm undefined for non-positive values.\")\n",
    "    return math.log(a)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "866330b7-628f-4ccc-9cfc-c65a5090a7f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the first number (or type 'exit' to quit):  8\n",
      "Enter the operation (+, -, *, /, ^, sqrt, log):  *\n",
      "Enter the second number:  119\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The result of 8.0 * 119.0 is: 952.0\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the first number (or type 'exit' to quit):  exit\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Exiting...\n"
     ]
    }
   ],
   "source": [
    "# Implementing the main loop\n",
    "def main():\n",
    "    calc = Calculator()\n",
    "    calc.add_operation('^', exponentiate)\n",
    "    calc.add_operation('sqrt', square_root)\n",
    "    calc.add_operation('log', logarithm)\n",
    "\n",
    "    while True:\n",
    "        try:\n",
    "            num1 = float(input(\"Enter the first number (or type 'exit' to quit): \"))\n",
    "        except ValueError:\n",
    "            print(\"Exiting...\")\n",
    "            break\n",
    "\n",
    "        operation = input(\"Enter the operation (+, -, *, /, ^, sqrt, log): \")\n",
    "\n",
    "        if operation in ['sqrt', 'log']:\n",
    "            num2 = 0  # Placeholder as these operations only need one operand\n",
    "        else:\n",
    "            try:\n",
    "                num2 = float(input(\"Enter the second number: \"))\n",
    "            except ValueError:\n",
    "                print(\"Exiting...\")\n",
    "                break\n",
    "\n",
    "        try:\n",
    "            result = calc.calculate(num1, operation, num2)\n",
    "            print(f\"The result of {num1} {operation} {num2 if operation not in ['sqrt', 'log'] else ''} is: {result}\")\n",
    "        except Exception as e:\n",
    "            print(f\"Error: {e}\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "79206f1c-dcd1-4492-b289-7101ff643415",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
