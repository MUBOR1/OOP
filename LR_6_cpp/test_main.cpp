#include <cassert>
#include <sstream>

struct data 
{
    int day;
    int mon;
    int year;
};

struct file 
{
  char name[20];
  data date;
  int kol;
  void in() 
  {
    cin>>date.day;
    cin>>date.mon;
    cin>>date.year;
  }

  void out() 
  {
    cout<<date.day<<" ";
    cout<<date.mon<<" ";
    cout<<date.year<<" ";
  }
};

int main() 
{
  file test_file;
  test_file.name = "test_file_name";
  test_file.date.day = 12;
  test_file.date.mon = 11;
  test_file.date.year = 2022;
  test_file.kol = 5;

  // Тестирование функции in()
  std::stringstream in_stream("12 11 2022");
  std::streambuf* old_cin = std::cin.rdbuf(in_stream.rdbuf());
  test_file.in();
  std::cin.rdbuf(old_cin);
  assert(test_file.date.day == 12);
  assert(test_file.date.mon == 11);
  assert(test_file.date.year == 2022);

  // Тестирование функции out()
  std::stringstream out_stream;
  std::streambuf* old_cout = std::cout.rdbuf(out_stream.rdbuf());
  test_file.out();
  std::cout.rdbuf(old_cout);
  assert(out_stream.str() == "12 11 2022 ");

  cout << "All tests passed!" << endl;

  return 0;
}
