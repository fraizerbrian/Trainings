#one.py

def func():
    print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")
# def func():
#     pass
#
# def func2():
#     pass

if __name__ == '__main__':
    print('ONE.PY is being run directly!')
else:
    print('ONE.PY has been imported!')
    # run the script
    # func2()
    # func()
