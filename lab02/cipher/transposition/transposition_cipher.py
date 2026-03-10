class TranspositionCipher:

    def encrypt(self, text, key):
        cipher = [''] * key

        for col in range(key):
            pointer = col

            while pointer < len(text):
                cipher[col] += text[pointer]
                pointer += key

        return ''.join(cipher)


    def decrypt(self, cipher_text, key):
        numOfColumns = int(len(cipher_text) / key)
        numOfRows = key
        numOfShadedBoxes = (numOfColumns * numOfRows) - len(cipher_text)

        plain = [''] * numOfColumns

        col = 0
        row = 0

        for symbol in cipher_text:
            plain[col] += symbol
            col += 1

            if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
                col = 0
                row += 1

        return ''.join(plain)