import argparse
import time
import re
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# 🔥 human-like scrolling
def slow_scroll(driver):
    for _ in range(10):
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(0.5)


def get_flipkart_reviews(url, max_reviews=100):
    options = Options()

    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1200,900")

    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    )

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(url)
    time.sleep(5)

    # ❌ close login popup
    try:
        driver.find_element(By.XPATH, "//button[text()='✕']").click()
    except:
        pass

    reviews = []
    seen = set()

    for _ in range(25):  # increase if needed
        print(f"\n🔄 Scrolling... collected: {len(reviews)}")

        # ✅ auto scroll
        slow_scroll(driver)

        # 🔥 expand "... more"
        more_buttons = driver.find_elements(By.XPATH, "//span[contains(text(),'more')]")
        for btn in more_buttons:
            try:
                driver.execute_script("arguments[0].click();", btn)
            except:
                pass

        # 🔥 exact selector from your inspect
        elements = driver.find_elements(
            By.XPATH,
            "//div[@dir='auto' and contains(@class,'css-146c3p1')]"
        )

        print(f"👉 Found {len(elements)} review elements")

        for el in elements:
            text = el.text.strip()
            text = clean_text(text)

            # ❌ skip header
            if text.lower().startswith("review for"):
                continue

            # ❌ skip short junk
            if len(text.split()) < 6:
                continue

            if text in seen:
                continue

            seen.add(text)
            reviews.append(text)

            print(f"✅ Added: {text[:60]}...")

            if len(reviews) >= max_reviews:
                break

        if len(reviews) >= max_reviews:
            break

    driver.quit()
    return reviews


def save_reviews(reviews, filename):
    df = pd.DataFrame({"review_text": reviews})
    df.to_csv(filename, index=False, encoding="utf-8-sig")
    print(f"\n✅ Saved {len(reviews)} reviews to {filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--max", type=int, default=100)
    parser.add_argument("--output", default="reviews.csv")

    args = parser.parse_args()

    reviews = get_flipkart_reviews(args.url, args.max)
    save_reviews(reviews, args.output)