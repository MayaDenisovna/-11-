"""Task 11"""
def sort_output(met):
    def wrapper(*arg):
        res = met(*arg)
        st = set(res)
        st = sorted(st)
        return st
    return wrapper

@sort_output
def get_words() -> list:
    return input().split(" ")

"""Task 12"""
def freq_analysis(met):
    def wrap(*args):
        fre = {}
        words = list(met(*args).split(" "))

        for word in words:
            if not word in fre:
                fre[word] = 1
            else:
                fre[word] += 1

        return fre
    return wrap

@freq_analysis
def get_text() -> str:
    return input().strip().lower()

