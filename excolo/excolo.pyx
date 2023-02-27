import time

def main() -> None:
    cdef float start = time.time()
    cdef int j = 1
    for i in range(1, 100):
        for k in range(1, 1000):
            for x in range(1, 1000):
                j += 1
    cdef float end = time.time()
    print(f"number: {j}, took {end-start} seconds")

main()

# def main() -> None:
#     start = time.time()
#     j = 1
#     for i in range(1, 100):
#         for k in range(1, 1000):
#             for x in range(1, 1000):
#                 j += 1
#     end = time.time()
#     print(f"number: {j}, took {end-start} seconds")

# if __name__ == "__main__":
#     main()
