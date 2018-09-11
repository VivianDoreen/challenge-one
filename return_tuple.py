def countVowels(string):
  vowel = "aeiou"
  final = [each for each in string if each in vowel]
  final_tuple = tuple(final)
  print(final_tuple)

  dup1 = [letter for letter in string if string.count(letter) > 1]
  print(dup1)
  print(len(dup1))

countVowels('dahdah')