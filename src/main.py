import server
import sys

if __name__ == '__main__':
   if 0 > 1: file_path = sys.argv[1]
   else: file_path = raw_input("Enter a file path to share: ")
   server.run_with_file(file_path)
