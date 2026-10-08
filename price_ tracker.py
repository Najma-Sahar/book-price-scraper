import csv
import requests
from bs4 import BeautifulSoup


def scarpe_books():
   url = "https://books.toscrape.com/"
   headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"}
   try:
       response = requests.get(url,headers=headers)
       response.encoding = "utf-8"

       if response.status_code != 200:
          return
       soup = BeautifulSoup(response.text, "html.parser")
       books = soup.find_all("article",class_="product_pod")
       with open("books.csv","w", newline="",encoding="utf-8") as file:
         writer =csv.writer(file)
         writer.writerow(["Book Title","price"])
         for book in books:
            title = book.find("h3").find("a")["title"]
            price = book.find("p", class_ ="price_color").text.strip()
            print('book title',title)
            print("book price", price)
            writer.writerow([title,price])
         print(f"Successfully scarped{len(books)} books to 'books.csv' !")
   except Exception as e:
      print(f"an error occured:{e}")
if __name__=="__main__":
   scarpe_books()

      