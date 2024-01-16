#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool is_non_zero_digit(char elem) {
  return ('1' <= elem) && (elem <= '9');
}

bool is_digit(char elem) {
  return ('0' <= elem) && (elem <= '9');
}

bool contains_2_digit_number(const char* text) {
  int pos = 0;
  for (;;) {
    while ((text[pos] != '\0') && !is_non_zero_digit(text[pos])) {pos++;}
    if (text[pos] == '\0') {break;} // если дошли до конца текста
    int start = pos; // дошли до ненулевой цифры
    pos++; // пропускаем первую цифру
    while (is_digit(text[pos])) {pos++;} // пропускаем остальные цифры
    int digits_count = pos - start;
    if (digits_count == 2) {
      return true;
    }
  }
  return false;
}

int main() {
  ifstream file("data.txt");
  if (file.fail()) {
    cerr << "Cannot open file." << endl;
    return 1;
  }
  while (!file.eof()) {
    string line;
    getline(file, line);
    if (contains_2_digit_number(line.c_str())) {
      cout << line << endl;
    }
  }
  return 0;
}