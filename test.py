import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()


# print("hello")
# # Fibonacci numbers module

# def fib(n):    # write Fibonacci series up to n
#     a, b = 0, 1
#     while b < n:
#         print(b, end=' ')
#         a, b = b, a+b
#     print()

# def fib2(n):   # return Fibonacci series up to n
#     result = []
#     a, b = 0, 1
#     while b < n:
#         result.append(b)
#         a, b = b, a+b
#     return result

# # comment

# import pygame
# pygame.init()

# drum = pygame.mixer.sound("samples/drum_tom_mid_hard.wav")
