# PDFfuzz

Steps to use:-

TextFile - days
TextFile - months

#python3 PDFfuzz.py -d days -m months

![github](https://user-images.githubusercontent.com/75741506/125202071-a1578400-e28f-11eb-8790-d98bdb60d7de.png)


if you want to take only Creator name of the pdf file use:

$> cat *.pdf|strings|grep Creator|cut -d 2 -f 1|grep -v TeX > users;cat users

![user](https://user-images.githubusercontent.com/75741506/125202317-b54fb580-e290-11eb-8f81-99b4837d9f8a.png)

Thankyou Happy to Help.
