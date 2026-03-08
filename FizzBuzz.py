class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        kq = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                kq.append("FizzBuzz")
            elif i % 3 == 0:
                kq.append('Fizz')
            elif i % 5 == 0:
                kq.append('Buzz')
            else:
                kq.append(str(i))
        return kq