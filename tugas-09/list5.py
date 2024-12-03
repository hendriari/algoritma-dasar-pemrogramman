def inputs():
    inputter = input("Masukkan Kalimat : ")
    return inputter

def outputs(inputs):
    # LOOPING REVERSE STRING
    # index = len(inputs)
    # result = []
    # while index > 0:
    #     result += inputs[index - 1]
    #     index -= 1
    # return result
    result = inputs
    return result[::-1]

print(outputs(inputs()))