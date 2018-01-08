from uuid import uuid4

from random import randint


__author__ = "Devin Markham"


def _default_a_b_handler(a, b):
    return a, b


class MathGame(object):
    def __init__(self, operator, operation, n_questions=20, min_num=0, max_num=10, handle_a_b=_default_a_b_handler):
        # handle_a_b is a function telling us what to do with to random ints between min_num and max_num
        # we could for instance do "if a < b => a, b else => b, a" and in the case of subtraction
        # (3, 7) => (7, 3) so that we can work with "7 - 3 = ___" and the answer is not negative
        self._n_questions = n_questions
        self._min_num = min_num
        self._max_num = max_num
        self._operator = operator
        self._operation = operation
        self._handle_a_b = handle_a_b

    def _generate_a_b(self):
        num_pairs = list()
        for ix in range(self._n_questions):
            a, b = self._handle_a_b(randint(self._min_num, self._max_num), randint(self._min_num, self._max_num))
            num_pairs.append((a, b))

        return num_pairs

    def _build_question_string(self, a, b):
        return "{A} {OP} {B} =".format(A=a, OP=self._operator, B=b)

    def make_game(self):
        question_nums = self._generate_a_b()
        questions = dict()
        for item in question_nums:
            questions[str(uuid4())] = {
                    "a": item[0],
                    "b": item[1],
                    "c": self._operation(item[0], item[1]),
                    "question_str": self._build_question_string(item[0], item[1])
                }

        return questions
