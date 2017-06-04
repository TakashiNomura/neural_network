# coding:UTF-8

# ニューロン
class Neuron:
    input_sum = 0.0

    def setInput(self, inp):
        self.input_sum += inp
        print(self.input_sum)

