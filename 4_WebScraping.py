import requests
from bs4 import BeautifulSoup
import csv
import tkinter as tk
from tkinter import messagebox

def scrape_eCommerce(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        products = soup.find_all('div', class_='product')

        with open('products.csv', 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Name', 'Price', 'Rating'])

            for product in products:
                name = product.find('h2', class_='product-name').text.strip()
                price = product.find('span', class_='product-price').text.strip()
                rating = product.find('span', class_='product-rating').text.strip()

                csv_writer.writerow([name, price, rating])

        messagebox.showinfo("Scraping Completed", "Scraping was completed successfully. Data saved to products.csv")
        read_csv_file('products.csv')
    else:
        messagebox.showerror("Error", "Unable to retrieve data from the website")

def start_scraping():
    url = url_entry.get()
    if url:
        scrape_eCommerce(url)
    else:
        messagebox.showerror("Error", "Please enter a URL")

def read_csv_file(filename):
    results_text.delete('1.0', tk.END)  # Clear previous results
    with open(filename, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        for row in csv_reader:
            results_text.insert(tk.END, ', '.join(row) + '\n')

def paste_url(event):
    clipboard_data = root.clipboard_get()
    url_entry.delete(0, tk.END)
    url_entry.insert(0, clipboard_data)

root = tk.Tk()
root.title("Web Scraper")

url_label = tk.Label(root, text="Enter Website URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

scrape_button = tk.Button(root, text="Scrape", command=start_scraping)
scrape_button.pack()

root.bind('<<Paste>>', paste_url)

results_label = tk.Label(root, text="Scraped Products:")
results_label.pack()

results_text = tk.Text(root, width=80, height=20)
results_text.pack()

root.mainloop()

root = tk.Tk()
root.title("Web Scraper")

url_label = tk.Label(root, text="Enter Website URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

url_entry.bind('<<Paste>>', paste_url)

scrape_button = tk.Button(root, text="Scrape", command=start_scraping)
scrape_button.pack()

results_label = tk.Label(root, text="Scraped Products:")
results_label.pack()

results_text = tk.Text(root, width=80, height=20)
results_text.pack()

root.mainloop()