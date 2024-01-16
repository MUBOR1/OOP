#include <cassert>

bool is_non_zero_digit(char elem) {
  return ('1' <= elem) && (elem <= '9');
}

void test_is_non_zero_digit() {
  assert(is_non_zero_digit('0') == false);
  assert(is_non_zero_digit('5') == true);
  assert(is_non_zero_digit('9') == true);
}

int main() {
  test_is_non_zero_digit();
  return 0;
}
