{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "0bb3256b-9070-4f9e-afa9-b6d8f11382de",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter an number :  10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number is positive\n"
     ]
    }
   ],
   "source": [
    "#if statements\n",
    "num = int (input(\"enter an number : \"))\n",
    "if num >0:\n",
    "    print (\"number is positive\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "19a1553c-a259-453d-8865-45915f612ffe",
   "metadata": {},
   "outputs": [],
   "source": [
    "text = \"hello\"\n",
    "if len(text)==0:\n",
    "    print(\"string is empty\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "37de9808-e634-417a-a7ef-8d9417c450e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "positivie number\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"Enter a number: \"))\n",
    "if num >0:\n",
    "    print (\"positivie number\" )\n",
    "if num <0:\n",
    "           print(\"Negative number\")\n",
    "if num==0:\n",
    "    print(\"number is zero\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "82e550ff-986b-4d62-b70b-c74a239d54e6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enetr a number :  15\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "multiple of both 3 and 5\n"
     ]
    }
   ],
   "source": [
    "num = int(input(\"enetr a number : \"))\n",
    "if num%3==0 and num%5==0:\n",
    "    print(\"multiple of both 3 and 5\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "7240dfb8-0593-45f6-b96b-09b5a9c87ccc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a number :  6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "multiple of both 2 and 3 \n"
     ]
    }
   ],
   "source": [
    "num = int(input (\"enter a number : \"))\n",
    "if num %2==0 and num%3==0:\n",
    "    print (\"multiple of both 2 and 3 \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "373aafb7-3022-4fd0-a180-6858fd8e79d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter a number:  8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number is multiple by 4\n"
     ]
    }
   ],
   "source": [
    "num = int (input(\"enter a number: \"))\n",
    "if num%4==0:\n",
    "    print (\"number is multiple by 4\")\n",
    "                 \n",
    "                 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "9aabdebb-cb2f-41a4-b608-fe8298fd92f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "leap year\n"
     ]
    }
   ],
   "source": [
    "#if-else statements\n",
    "\n",
    "year = 2024\n",
    "if (year%400==0) or (year%4==0 and year%100!=0):\n",
    "    print(\"leap year\")\n",
    "else:\n",
    "    print(\"not a leap year\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "3d1bef9d-5cf2-4e25-98d7-39e3d912af18",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "consonant\n"
     ]
    }
   ],
   "source": [
    "ch = \"kalyan\"\n",
    "if ch in \"aeiouAEIOU\":\n",
    "    print(\"vowel\")\n",
    "else:\n",
    "    print(\"consonant\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "2204f1b1-f00c-441d-af3f-73d61f7e5b68",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "century year\n"
     ]
    }
   ],
   "source": [
    "year = 1900\n",
    "if year%100==0:\n",
    "    print(\"century year\")\n",
    "else:\n",
    "    print(\"not a century year\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "6cb94a5a-5f7f-48cc-91aa-979b6db1c9fe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number:  10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "positive number\n"
     ]
    }
   ],
   "source": [
    "num= int(input(\"Enter a number: \"))\n",
    "if num>0:\n",
    "    print('positive number')\n",
    "else:\n",
    "    ('non-positive number')\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "bfa1b4d7-070f-4524-9a20-92dd5d548226",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "not eligible to vote\n"
     ]
    }
   ],
   "source": [
    "age = 17\n",
    "if age >=18:\n",
    "    print(\"eligible to vote\")\n",
    "else:\n",
    "    print(\"not eligible to vote\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "448b3955-a5dd-4754-84cd-b36e1db851f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "prime number\n"
     ]
    }
   ],
   "source": [
    "n=7\n",
    "is_prime = True\n",
    "if n<=1:\n",
    "    is_prime =False\n",
    "else:\n",
    "    for i in range(2,n):\n",
    "        if n%i == 0:\n",
    "           is_prime = False\n",
    "           break\n",
    "if is_prime:\n",
    "    print(\"prime number\")\n",
    "else:\n",
    "    print(\"not a prime number\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "685b2ceb-20d8-4710-b410-455990085478",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1ebd19d7-9e8a-4e89-a315-7762940487e5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d2197158-36a8-4d7a-8500-481ae065c89b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "46250e38-920a-43f5-bc54-904951960e10",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
