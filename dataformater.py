from os import path


def FormatData(destination, source, numColumns):
  s = open(source, 'r')
  contents = s.read()
  contentslist = contents.split()

  
  contentscleaned = [];
  stringcleaned = "";
  for string in contentslist:
    for letter in string:
      if ( letter != '' and letter != ','):
        stringcleaned += letter;
    contentscleaned.append(stringcleaned)
    stringcleaned = "";

  s.close()

  d = open(destination, 'w')

  
  for i in range(len(contentscleaned)):
    if(i % numColumns == 0):
      d.write('\n');
    d.write(contentscleaned[i] + ',');


  d.close()
  


if __name__ == '__main__':
  source = 'D:\\scottsdocs\\sourcecode\\dataformatter\\francebirthratesbyyear.csv'
  destination = 'D:\\scottsdocs\\sourcecode\\dataformatter\\francebirthratesbyyearformatted.csv'

  FormatData(destination, source, 4)


  
  

