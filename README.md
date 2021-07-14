# PDFfuzz

Steps to use:-

TextFile - days
TextFile - months

#python3 PDFfuzz.py -d days -m months

![PDFfuzz](https://user-images.githubusercontent.com/75741506/125633006-ab9c15ef-848a-4f5f-a49d-31f860197176.png)


if you want to take only Creator name of the pdf file use:

$> cat *.pdf|strings|grep Creator|cut -d 2 -f 1|grep -v TeX > users;cat users

![users](https://user-images.githubusercontent.com/75741506/125633167-e06da65c-a2e2-4673-bc07-ed1d6ce18d24.png)

Thankyou Happy to Help.
