import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to get all image URLs from a website
def get_image_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    image_urls = []
    for img_tag in soup.find_all("img"):
        img_url = img_tag.get("src")
        if img_url:
            full_url = urljoin(url, img_url)  # Convert relative URL to absolute
            image_urls.append(full_url)
    
    return image_urls

# Function to download images
def download_images(image_urls, folder="Vitiligo images"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    for i, img_url in enumerate(image_urls):
        try:
            response = requests.get(img_url, stream=True)
            if response.status_code == 200:
                img_path = os.path.join(folder, f"image_{i+1}.jpg")
                with open(img_path, "wb") as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                print(f"Downloaded: {img_url}")
            else:
                print(f"Failed to download: {img_url}")
        except Exception as e:
            print(f"Error downloading {img_url}: {e}")

# Main execution
if __name__ == "__main__":
    website_url = input("Enter website URL: ")
    image_urls = get_image_urls(website_url)
    
    if image_urls:
        print(f"Found {len(image_urls)} images. Downloading...")
        download_images(image_urls)
        print("Download completed!")
    else:
        print("No images found on the page.")
